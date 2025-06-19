# ================= 用户配置 =================
SCRIPT_NAME = "DaVinci TTS "
SCRIPT_VERSION = "3.3"
SCRIPT_AUTHOR = "HEIBA"

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
X_CENTER = (SCREEN_WIDTH - WINDOW_WIDTH) // 2
Y_CENTER = (SCREEN_HEIGHT - WINDOW_HEIGHT) // 2

SCRIPT_KOFI_URL="https://ko-fi.com/heiba"
SCRIPT_WX_URL = "https://mp.weixin.qq.com/s?__biz=MzUzMTk2MDU5Nw==&mid=2247484626&idx=1&sn=e5eef7e48fbfbf37f208ed9a26c5475a&chksm=fabbc2a8cdcc4bbefcb7f6c72a3754335c25ec9c3e408553ec81c009531732e82cbab923276c#rd"
AIRANSLATOR_KOFI_URL         = ""
AIRANSLATOR_TAOBAO_URL       = ""

OPENAI_FM = "https://openai.fm"
MINIMAX_PREW_URL = "https://www.minimax.io/audio/voices"
MINIMAXI_PREW_URL = "https://www.minimaxi.com/audio/voices"

import os
import sys
import platform
import re
import time
import wave
import json
import webbrowser

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util import Retry
    import azure.cognitiveservices.speech as speechsdk
    import edge_tts
except ImportError:
    # 1. 获取脚本所在目录（备用）
    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    # 2. 根据不同平台设置 Lib 目录为绝对路径
    system = platform.system()
    if system == "Windows":
        # Windows 下 C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\TTS\Lib
        program_data = os.environ.get("PROGRAMDATA", r"C:\ProgramData")
        lib_dir = os.path.join(
            program_data,
            "Blackmagic Design",
            "DaVinci Resolve",
            "Fusion",
            "HB",
            "DaVinci TTS",
            "Lib"
        )
    elif system == "Darwin":
        # macOS 下 /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/TTS/Lib
        lib_dir = os.path.join(
            "/Library",
            "Application Support",
            "Blackmagic Design",
            "DaVinci Resolve",
            "Fusion",
            "HB",
            "DaVinci TTS",
            "Lib"
        )
    else:
        # 其他平台（Linux 等），回退到相对路径
        lib_dir = os.path.normpath(
            os.path.join(script_path, "..", "..", "..", "TTS", "Lib")
        )

    # 3. 规范化一下路径（去掉多余分隔符或 ..）
    lib_dir = os.path.normpath(lib_dir)
    # —— 二、插入到 sys.path —— 
    if os.path.isdir(lib_dir):
        # 放到最前面，确保优先加载
        sys.path.insert(0, lib_dir)
    else:
        # 如果路径不对，可打印日志帮助调试
        print(f"Warning: TTS/Lib 目录不存在：{lib_dir}", file=sys.stderr)

    try:
        import requests
        from requests.adapters import HTTPAdapter
        from urllib3.util import Retry
        import azure.cognitiveservices.speech as speechsdk
        import edge_tts
        print(lib_dir)
    except ImportError as e:
        print("依赖导入失败，请确保所有依赖已打包至 Lib 目录中：", lib_dir, "\n错误信息：", e)

from xml.dom import minidom
import xml.etree.ElementTree as ET

from typing import Dict, Any, List, Optional

script_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# 创建带重试机制的 session（放在模块初始化，整个脚本共享）
session = requests.Session()
retries = Retry(
    total=3,                 # 最多重试3次
    backoff_factor=0.5,       # 每次重试等待时间逐步增加
    status_forcelist=[500, 502, 503, 504],  # 服务器错误才重试
    allowed_methods=["GET", "POST"]         # 限定方法
)
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))

try:
    import DaVinciResolveScript as dvr_script
    from python_get_resolve import GetResolve
    print("DaVinciResolveScript from Python")
except ImportError:
    
    if platform.system() == "Darwin": 
        resolve_script_path1 = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Examples"
        resolve_script_path2 = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"
    elif platform.system() == "Windows": 
        resolve_script_path1 = os.path.join(os.environ['PROGRAMDATA'], "Blackmagic Design", "DaVinci Resolve", "Support", "Developer", "Scripting", "Examples")
        resolve_script_path2 = os.path.join(os.environ['PROGRAMDATA'], "Blackmagic Design", "DaVinci Resolve", "Support", "Developer", "Scripting", "Modules")
    else:
        raise EnvironmentError("Unsupported operating system")

    sys.path.append(resolve_script_path1)
    sys.path.append(resolve_script_path2)

    try:
        import DaVinciResolveScript as dvr_script
        from python_get_resolve import GetResolve
        print("DaVinciResolveScript from DaVinci")
    except ImportError as e:
        raise ImportError("Unable to import DaVinciResolveScript or python_get_resolve after adding paths") from e

def check_or_create_file(file_path):
    if os.path.exists(file_path):
        pass
    else:
        try:
            with open(file_path, 'w') as file:
                json.dump({}, file)  
        except IOError:
            raise Exception(f"Cannot create file: {file_path}")
def load_resource(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} missing – check resources folder")
    # 用标准的 open 读取
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

config_dir = os.path.join(script_path, 'config')
settings_file = os.path.join(config_dir, 'TTS_settings.json')
script_info_cn  = load_resource(os.path.join(config_dir, "script_info_cn.html"))
script_info_en  = load_resource(os.path.join(config_dir, "script_info_en.html"))
script_clone_info_cn = load_resource(os.path.join(config_dir, "script_clone_info_cn.html"))
script_clone_info_en = load_resource(os.path.join(config_dir, "script_clone_info_en.html"))

check_or_create_file(settings_file)

def load_settings(settings_file):
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as file:
            content = file.read()
            if content:
                try:
                    settings = json.loads(content)
                    return settings
                except json.JSONDecodeError as err:
                    print('Error decoding settings:', err)
                    return None
    return None

def save_settings(settings, settings_file):
    with open(settings_file, 'w') as file:
        content = json.dumps(settings, indent=4)
        file.write(content)

saved_settings = load_settings(settings_file) 

default_settings = {
    "Path": "",
    "UNUSE_API":False,
    "API_KEY": '',
    "REGION": '',
    "LANGUAGE": 0,
    "TYPE": 0,
    "NAME": 0,
    "RATE": 1.0,
    "PITCH": 1.0,
    "VOLUME": 1.0,
    "STYLE": 0,
    "BREAKTIME":50,
    "STYLEDEGREE": 1.0,
    "OUTPUT_FORMATS":2,

    "minimax_API_KEY": "",
    "minimax_GROUP_ID": "",
    "minimax_intlCheckBox":False,

    "minimax_Model": 0,
    "minimax_Voice": 0,
    "minimax_Language": 0,
    "minimax_SubtitleCheckBox":False,
    "minimax_Emotion": 0,
    "minimax_Rate": 1.0,
    "minimax_Volume": 1.0,
    "minimax_Pitch": 0,
    "minimax_Format": 0,
    "minimax_Break":50,

    "OpenAI_API_KEY": "",
    "OpenAI_BASE_URL": "",
    "OpenAI_Model": 0,
    "OpenAI_Voice": 0,
    "OpenAI_Rate": 1.0,
    "OpenAI_Format": 0,
    "OpenAI_Instruction":"",
    "OpenAI_Preset":0,
    
    "CN":True,
    "EN":False,


}
status_file = os.path.join(config_dir, 'status.json')

class STATUS_MESSAGES:
    pass
with open(status_file, "r", encoding="utf-8") as file:
    status_data = json.load(file)
# 把 JSON 中的每一项都设置为 STATUS_MESSAGES 的类属性
for key, (en, zh) in status_data.items():
    setattr(STATUS_MESSAGES, key, (en, zh))
    
project_manager = resolve.GetProjectManager()
current_project = project_manager.GetCurrentProject()
current_timeline = current_project.GetCurrentTimeline()

def get_first_empty_track(timeline, start_frame, end_frame, media_type):
    """获取当前播放头位置的第一个空轨道索引"""
    track_index = 1
    while True:
        items = timeline.GetItemListInTrack(media_type, track_index)
        if not items:
            return track_index
        
        # 检查轨道上是否有片段与给定的start_frame和end_frame重叠
        is_empty = True
        for item in items:
            if item.GetStart() <= end_frame and start_frame <= item.GetEnd():
                is_empty = False
                break
        
        if is_empty:
            return track_index
        
        track_index += 1
        
def render_audio_by_marker(output_dir):
    """
    使用当前Project、当前Timeline的第一个Marker，导出相应区段的音频（单一剪辑模式）。
    导出完成后，返回可能的音频文件完整路径（字符串）。
    若没有Marker则返回None。
    """
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()
    timeline_start_frame = current_timeline.GetStartFrame()
    current_project.SetCurrentRenderMode(1)
    current_mode = current_project.GetCurrentRenderMode()
    markers = current_timeline.GetMarkers()
    
    if current_mode != 1:
        print("渲染模式切换失败，无法继续。")
        return None
    
    if not markers:
        print("请先使用Mark点标记参考音频范围！")
        show_warning_message(STATUS_MESSAGES.insert_mark)

        return None
        
    first_frame_id = sorted(markers.keys())[0]
    marker_info = markers[first_frame_id]

    local_start = int(first_frame_id)
    local_end   = local_start + int(marker_info["duration"]) - 1

    frame_rate = float(current_project.GetSetting("timelineFrameRate"))
    duration_frames = int(marker_info["duration"])
    duration_seconds = duration_frames / frame_rate
    if duration_seconds < 10 or duration_seconds > 300:
        show_warning_message(STATUS_MESSAGES.duration_seconds)
        return None

    mark_in  = timeline_start_frame + local_start
    mark_out = timeline_start_frame + local_end
    
    filename = f"clone_{current_timeline.GetUniqueId()}"
    #current_project.LoadRenderPreset("Audio Only")
    render_settings = {
        "SelectAllFrames": False,
        "MarkIn": mark_in,
        "MarkOut": mark_out,
        "TargetDir": output_dir,
        "CustomName": filename,
        "UniqueFilenameStyle": 1,   # 1 => 序号添加在后缀
        "ExportVideo": False,
        "ExportAudio": True,
        "AudioCodec": "mp3",
        "AudioBitDepth": 32,        # 32-bit 浮点数若不被支持, 可尝试改成 16 或 24
        "AudioSampleRate": 48000,
        #"Format": "mp3",           # 容器格式
    }
    minimax_clone_items["minimaxCloneStatus"].Text = "Start..."
    current_project.SetRenderSettings(render_settings)
    job_id = current_project.AddRenderJob()
    render_result = current_project.StartRendering([job_id])
    update_status(STATUS_MESSAGES.render_audio)
    clone_filename = f"{filename}.mp3"
    clone_file_path = os.path.join(output_dir, clone_filename)

    return clone_file_path



def add_to_media_pool_and_timeline(start_frame, end_frame, filename):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    media_pool = current_project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()
    tts_folder = None

    # 查找或创建"TTS"文件夹
    folders = root_folder.GetSubFolderList()
    for folder in folders:
        if folder.GetName() == "TTS":
            tts_folder = folder
            break

    if not tts_folder:
        tts_folder = media_pool.AddSubFolder(root_folder, "TTS")

    if tts_folder:
        print(f"TTS folder is available: {tts_folder.GetName()}")
    else:
        print("Failed to create or find TTS folder.")
        return False

    # 加载音频到媒体池
    media_pool.SetCurrentFolder(tts_folder)
    imported_items = media_pool.ImportMedia([filename])
    
    if not imported_items:
        print(f"Failed to import media: {filename}")
        return False

    selected_clip = imported_items[0]
    print(f"Imported clip: {selected_clip.GetName()}")

    # 获取当前时间线
    current_timeline = current_project.GetCurrentTimeline()
    frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
    clip_duration_frames = timecode_to_frames(selected_clip.GetClipProperty("Duration"), frame_rate)

    # 查找当前播放头位置的第一个空轨道
    track_index = get_first_empty_track(current_timeline, start_frame, end_frame, "audio")

    # 创建clipInfo字典
    clip_info = {
        "mediaPoolItem": selected_clip,
        "startFrame": 0,
        "endFrame": clip_duration_frames - 1,
        "trackIndex": track_index,
        "recordFrame": start_frame,  # 在字幕的起始位置添加
        "stereoEye": "both"  # 设置为立体声
    }

    # 将剪辑添加到时间线
    timeline_item = media_pool.AppendToTimeline([clip_info])
    if timeline_item:
        print(f"Appended clip: {selected_clip.GetName()} to timeline at frame {start_frame} on track {track_index}.")
        update_status(STATUS_MESSAGES.loaded_to_timeline)
    else:
        print("Failed to append clip to timeline.")

def import_srt_to_timeline(srt_path):
    """
    将指定 .srt 文件导入并追加到当前时间线。
    返回 True 表示成功，False 表示失败。
    """
    # 1. 获取 Resolve、ProjectManager、Project、Timeline
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    if current_project is None:
        print("错误：未找到当前项目")
        return False

    timeline = current_project.GetCurrentTimeline()
    if timeline is None:
        print("错误：未找到当前时间线")
        return False

    # 2. 删除所有“subtitle”轨道中的片段
    sub_count = timeline.GetTrackCount("subtitle")
    for ti in range(1, sub_count + 1):
        items = timeline.GetItemListInTrack("subtitle", ti)
        if items:
            timeline.DeleteClips(items)  # 删除指定轨道上的片段&#8203;:contentReference[oaicite:6]{index=6}&#8203;:contentReference[oaicite:7]{index=7}

    # 3. 导入 .srt 到媒体池
    media_pool = current_project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()
    media_pool.SetCurrentFolder(root_folder)

    # 可选：删除媒体池中同名旧条目，避免重复
    file_name = os.path.basename(srt_path)
    for clip in root_folder.GetClipList():
        if clip.GetName() == file_name:
            media_pool.DeleteClips([clip])
            break

    imported = media_pool.ImportMedia([srt_path])  # 导入 .srt&#8203;:contentReference[oaicite:8]{index=8}&#8203;:contentReference[oaicite:9]{index=9}
    if not imported:
        print(f"错误：字幕文件导入失败 -> {srt_path}")
        return False

    # 4. 将导入的字幕追加到时间线
    new_clip = imported[0]
    success = media_pool.AppendToTimeline([new_clip])  # 追加到时间线&#8203;:contentReference[oaicite:10]{index=10}&#8203;:contentReference[oaicite:11]{index=11}
    if not success:
        print("错误：将字幕添加到时间线失败")
        return False

    print(f"字幕已成功加载到时间线: {file_name}")
    return True

ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)

win = dispatcher.AddWindow({
    "ID": "MainWin", 
    "WindowTitle": SCRIPT_NAME+SCRIPT_VERSION, 
    "Geometry": [X_CENTER, Y_CENTER, WINDOW_WIDTH, WINDOW_HEIGHT],
    "Spacing": 10,
    "StyleSheet": """
        * {
            font-size: 14px; /* 全局字体大小 */
        }
    """
    },
    [
        ui.VGroup([
            ui.TabBar({"Weight": 0.0, "ID": "MyTabs"}), 
            ui.Stack({"Weight": 1.0, "ID": "MyStack"}, [
                ui.VGroup({"ID": "Azure TTS", "Weight": 1}, [
                    ui.HGroup({"Weight": 0.7}, [
                        ui.VGroup({"Weight": 1}, [
                            ui.TextEdit({"ID": "AzureTxt", "Text": "","PlaceholderText": "", "Weight": 0.9, "Font": ui.Font({"PixelSize": 15})}),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Button({"ID": "GetSubButton", "Text": "从时间线获取字幕", "Weight": 0.7}),
                                ui.SpinBox({"ID": "BreakSpinBox", "Value": 50, "Minimum": 0, "Maximum": 5000, "SingleStep": 50, "Weight": 0.1}),
                                ui.Label({"ID": "BreakLabel", "Text": "ms", "Weight": 0.1}),
                                ui.Button({"ID": "BreakButton", "Text": "停顿", "Weight": 0.1}),
                                
                            ])
                        ]),
                        ui.VGroup({"Weight": 1}, [
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Button({"ID": "AlphabetButton", "Text": "发音", "Weight": 1}),
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "LanguageLabel", "Text": "语言", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "LanguageCombo", "Text": "", "Weight": 0.8}),
                                ui.Label({"ID": "NameTypeLabel", "Text": "类型", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "NameTypeCombo", "Text": "", "Weight": 0.8})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "NameLabel", "Text": "名称", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "NameCombo", "Text": "", "Weight": 0.8}),
                                ui.Button({"ID": "PlayButton", "Text": "播放预览"}),
                                ui.Label({"ID": "MultilingualLabel", "Text": "语言技能", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "MultilingualCombo", "Text": "", "Weight": 0.2})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "StyleLabel", "Text": "风格", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "StyleCombo", "Text": "", "Weight": 0.8})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "StyleDegreeLabel", "Text": "风格强度", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.Slider({"ID": "StyleDegreeSlider", "Value": 100, "Minimum": 0, "Maximum": 200, "Orientation": "Horizontal", "Weight": 0.5}),
                                ui.DoubleSpinBox({"ID": "StyleDegreeSpinBox", "Value": 1.0, "Minimum": 0.0, "Maximum": 2.0, "SingleStep": 0.01, "Weight": 0.3})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "RateLabel", "Text": "语速", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.Slider({"ID": "RateSlider", "Value": 100, "Minimum": 0, "Maximum": 300, "Orientation": "Horizontal", "Weight": 0.5}),
                                ui.DoubleSpinBox({"ID": "RateSpinBox", "Value": 1.0, "Minimum": 0.0, "Maximum": 3.0, "SingleStep": 0.01, "Weight": 0.3})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "PitchLabel", "Text": "音高", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.Slider({"ID": "PitchSlider", "Value": 100, "Minimum": 50, "Maximum": 150, "Orientation": "Horizontal", "Weight": 0.5}),
                                ui.DoubleSpinBox({"ID": "PitchSpinBox", "Value": 1.0, "Minimum": 0.5, "Maximum": 1.5, "SingleStep": 0.01, "Weight": 0.3})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "VolumeLabel", "Text": "音量", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.Slider({"ID": "VolumeSlider", "Value": 100, "Minimum": 0, "Maximum": 150, "Orientation": "Horizontal", "Weight": 0.5}),
                                ui.DoubleSpinBox({"ID": "VolumeSpinBox", "Value": 1.0, "Minimum": 0, "Maximum": 1.5, "SingleStep": 0.01, "Weight": 0.3})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "OutputFormatLabel", "Text": "输出格式", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                                ui.ComboBox({"ID": "OutputFormatCombo", "Text": "Output_Format", "Weight": 0.8})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Button({"ID": "FromSubButton", "Text": "朗读当前字幕"}),
                                ui.Button({"ID": "FromTxtButton", "Text": "朗读文本框"}),
                                ui.Button({"ID": "ResetButton", "Text": "重置"})
                            ]),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Label({"ID": "StatusLabel", "Text": " ", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}})
                            ])
                        ])
                    ])
                ]),
                ui.VGroup({"ID": "Minimax TTS", "Weight": 1}, [
                    ui.HGroup({"Weight": 0.7}, [
                        ui.VGroup({"Weight": 1}, [
                            ui.TextEdit({"ID": "minimaxText", "PlaceholderText": ""}),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Button({"ID": "minimaxGetSubButton", "Text": "从时间线获取字幕", "Weight": 0.7}),
                                ui.SpinBox({"ID": "minimaxBreakSpinBox", "Value": 50, "Minimum": 1, "Maximum": 9999, "SingleStep": 50, "Weight": 0.1}),
                                ui.Label({"ID": "minimaxBreakLabel", "Text": "ms", "Weight": 0.1}),
                                ui.Button({"ID": "minimaxBreakButton", "Text": "停顿", "Weight": 0.1})
                            ])
                        ]),
                        ui.VGroup({"Weight": 1}, [
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxModelLabel","Text": "模型:", "Weight": 0}),
                                ui.ComboBox({"ID": "minimaxModelCombo", "Text": "选择模型"}),
                                ui.Label({"ID": "minimaxLanguageLabel","Text": "语言:", "Weight": 0}),
                                ui.ComboBox({"ID": "minimaxLanguageCombo", "Text": "选择语言"})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxVoiceLabel","Text": "音色:", "Weight": 0}),
                                ui.ComboBox({"ID": "minimaxVoiceCombo", "Text": "选择人声","Weight": 1}),
                               
                            ]),
                            ui.HGroup({}, [
                               
                                ui.Button({"ID": "minimaxPreviewButton", "Text": "试听","Weight": 0.1}),
                                ui.Button({"ID": "ShowMiniMaxClone", "Text": "","Weight": 0.1}),
                                ui.Button({"ID": "minimaxDeleteVoice", "Text": "","Weight": 0.1}),
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxEmotionLabel","Text": "情绪:", "Weight": 0}),
                                ui.ComboBox({"ID": "minimaxEmotionCombo", "Text": "选择情绪"})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxRateLabel","Text": "速度:", "Weight": 0.2}),
                                ui.Slider({"ID": "minimaxRateSlider", "Minimum": 50, "Maximum": 200, "Value": 100, "SingleStep": 1, "Weight": 0.6}),
                                ui.DoubleSpinBox({"ID": "minimaxRateSpinBox", "Minimum": 0.50, "Maximum": 2.00, "Value": 1.00, "SingleStep": 0.01, "Decimals": 2, "Weight": 0.2})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxVolumeLabel","Text": "音量:", "Weight": 0.2}),
                                ui.Slider({"ID": "minimaxVolumeSlider", "Minimum": 10, "Maximum": 1000, "Value": 100, "SingleStep": 1, "Weight": 0.6}),
                                ui.DoubleSpinBox({"ID": "minimaxVolumeSpinBox", "Minimum": 0.10, "Maximum": 10.00, "Value": 1.00, "SingleStep": 0.01, "Decimals": 2, "Weight": 0.2})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxPitchLabel","Text": "音调:", "Weight": 0.2}),
                                ui.Slider({"ID": "minimaxPitchSlider", "Minimum": -1200, "Maximum": 1200, "SingleStep": 1, "Weight": 0.6}),
                                ui.SpinBox({"ID": "minimaxPitchSpinBox", "Minimum": -12, "Maximum": 12, "Value": 0, "SingleStep": 1, "Weight": 0.2})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxFormatLabel","Text": "格式:", "Weight": 0}),
                                ui.ComboBox({"ID": "minimaxFormatCombo", "Text": "选择格式"}),
                                ui.CheckBox({"ID": "minimaxSubtitleCheckBox", "Text": "生成字幕", "Checked": False, "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                            ]),
                            ui.HGroup({}, [
                                ui.Button({"ID": "minimaxFromSubButton", "Text": "朗读当前字幕"}),
                                ui.Button({"ID": "minimaxFromTxtButton", "Text": "朗读文本框"}),
                                ui.Button({"ID": "minimaxResetButton", "Text": "重置"})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "minimaxStatusLabel", "Text": " ", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}})
                            ])
                        ])
                    ])
                ]),
                ui.VGroup({"ID": "OpenAI TTS", "Weight": 1}, [
                    ui.HGroup({"Weight": 0.7}, [
                        ui.VGroup({"Weight": 0.5}, [
                            ui.TextEdit({"ID": "OpenAIText", "PlaceholderText": ""}),
                            ui.HGroup({"Weight": 0.1}, [
                                ui.Button({"ID": "OpenAIGetSubButton", "Text": "从时间线获取字幕", "Weight": 0.7}),
                            ])
                        ]),
                        ui.VGroup({"Weight": 0.5}, [
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIModelLabel","Text": "模型:", "Weight": 0}),
                                ui.ComboBox({"ID": "OpenAIModelCombo", "Text": "选择模型"}),
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIVoiceLabel","Text": "音色:", "Weight": 0}),
                                ui.ComboBox({"ID": "OpenAIVoiceCombo", "Text": "选择人声"}),
                                ui.Label({"ID": "OpenAIPresetLabel","Text": "预设:", "Weight": 0}),
                                ui.ComboBox({"ID": "OpenAIPresetCombo", "Text": "预设"}),
                                ui.Button({"ID": "OpenAIPreviewButton", "Text": "试听"})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIInstructionLabel","Text": "指令:", "Weight": 0}),
                                ui.TextEdit({"ID": "OpenAIInstructionText", "PlaceholderText": ""}),
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIRateLabel","Text": "速度:", "Weight": 0.2}),
                                ui.Slider({"ID": "OpenAIRateSlider", "Minimum": 25, "Maximum": 400, "Value": 100, "SingleStep": 1, "Weight": 0.6}),
                                ui.DoubleSpinBox({"ID": "OpenAIRateSpinBox", "Minimum": 0.25, "Maximum": 4.00, "Value": 1.00, "SingleStep": 0.01, "Decimals": 2, "Weight": 0.2})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIFormatLabel","Text": "格式:", "Weight": 0}),
                                ui.ComboBox({"ID": "OpenAIFormatCombo", "Text": "选择格式"}),
                            ]),
                            ui.HGroup({}, [
                                ui.Button({"ID": "OpenAIFromSubButton", "Text": "朗读当前字幕"}),
                                ui.Button({"ID": "OpenAIFromTxtButton", "Text": "朗读文本框"}),
                                ui.Button({"ID": "OpenAIResetButton", "Text": "重置"})
                            ]),
                            ui.HGroup({}, [
                                ui.Label({"ID": "OpenAIStatusLabel", "Text": " ", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}})
                            ])
                        ])
                    ])
                ]), 
                ui.HGroup({"ID": "Config", "Weight": 1}, [
                    ui.VGroup({"Weight": 0.5, "Spacing": 10}, [
                        ui.HGroup({"Weight": 1}, [
                            ui.TextEdit({"ID": "infoTxt", "Text": "", "ReadOnly": True, "Font": ui.Font({"PixelSize": 14})})
                        ])
                    ]),
                    ui.VGroup({"Weight": 0.5, "Spacing": 10,}, [
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"ID": "PathLabel", "Text": "保存路径", "Alignment": {"AlignLeft": True}, "Weight": 0.2}),
                            ui.LineEdit({"ID": "Path", "Text": "", "PlaceholderText": "", "ReadOnly": False, "Weight": 0.6}),
                            ui.Button({"ID": "Browse", "Text": "浏览", "Weight": 0.2}),
                        ]),
                        
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"Text": "Azure API", "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                            ui.Button({"ID": "ShowAzure", "Text": "配置","Weight": 0.1,}),
                        ]),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"Text": "MiniMax API", "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                            ui.Button({"ID": "ShowMiniMax", "Text": "配置","Weight": 0.1}),
                            
                        ]),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"Text": "OpenAI API", "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                            ui.Button({"ID": "ShowOpenAI", "Text": "配置","Weight": 0.1}),
                            
                        ]),
                        ui.Label({"ID":"MoreScriptLabel","Text":"","Weight":0.1,"Alignment": {"AlignHCenter": True, "AlignVCenter": True}}),
                        ui.Button({"ID":"AITranslatorButton","Text":"AI字幕翻译插件","Weight":0.1}),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.CheckBox({"ID": "LangEnCheckBox", "Text": "EN", "Checked": True, "Alignment": {"AlignRight": True}, "Weight": 0}),
                            ui.CheckBox({"ID": "LangCnCheckBox", "Text": "简体中文", "Checked": False, "Alignment": {"AlignRight": True}, "Weight": 1}),
                            ui.Button({"ID": "openGuideButton", "Text": "教程","Weight": 0.1}),
                        ]),
                        ui.Button({
                            "ID": "CopyrightButton", 
                            "Text": "关注公众号：游艺所\n\n>>>点击查看更多信息<<<\n\n© 2024, Copyright by HB.",
                            "Alignment": {"AlignHCenter": True, "AlignVCenter": True},
                            "Font": ui.Font({"PixelSize": 12, "StyleName": "Bold"}),
                            "Flat": True,
                            "TextColor": [0.1, 0.3, 0.9, 1],
                            "BackgroundColor": [1, 1, 1, 0],
                            "Weight": 0.8
                        })
                    ])
                ])
            ])
        ])
    ]
)

# azure配置窗口
azure_config_window = dispatcher.AddWindow(
    {
        "ID": "AzureConfigWin",
        "WindowTitle": "Azure API",
        "Geometry": [900, 400, 400, 200],
        "Hidden": True,
        "StyleSheet": """
        * {
            font-size: 14px; /* 全局字体大小 */
        }
    """
    },
    [
        ui.VGroup(
            [
                ui.Label({"ID": "AzureLabel","Text": "填写Azure API信息", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}}),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"ID": "RegionLabel", "Text": "区域", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                    ui.LineEdit({"ID": "Region", "Text": "", "Weight": 0.8}),
                ]),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"ID": "ApiKeyLabel", "Text": "密钥", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                    ui.LineEdit({"ID": "ApiKey", "Text": "", "EchoMode": "Password", "Weight": 0.8}),
                    
                ]),
                ui.CheckBox({"ID": "UnuseAPICheckBox", "Text": "停用 API", "Checked": True, "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                ui.HGroup({"Weight": 1}, [
                    ui.Button({"ID": "AzureConfirm", "Text": "确定","Weight": 1}),
                    ui.Button({"ID": "AzureRegisterButton", "Text": "注册","Weight": 1}),
                ]),
                
            ]
        )
    ]
)
# openai配置窗口
openai_config_window = dispatcher.AddWindow(
    {
        "ID": "OpenAIConfigWin",
        "WindowTitle": "OpenAI API",
        "Geometry": [900, 400, 400, 200],
        "Hidden": True,
        "StyleSheet": """
        * {
            font-size: 14px; /* 全局字体大小 */
        }
    """
    },
    [
        ui.VGroup(
            [
                ui.Label({"ID": "OpenAILabel","Text": "填写OpenAI API信息", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}}),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"ID": "OpenAIBaseURLLabel", "Text": "Base URL", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                    ui.LineEdit({"ID": "OpenAIBaseURL", "Text":"","PlaceholderText": "https://api.openai.com/v1", "Weight": 0.8}),
                ]),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"ID": "OpenAIApiKeyLabel", "Text": "密钥", "Alignment": {"AlignRight": False}, "Weight": 0.2}),
                    ui.LineEdit({"ID": "OpenAIApiKey", "Text": "", "EchoMode": "Password", "Weight": 0.8}),
                    
                ]),
                ui.HGroup({"Weight": 1}, [
                    ui.Button({"ID": "OpenAIConfirm", "Text": "确定","Weight": 1}),
                    ui.Button({"ID": "OpenAIRegisterButton", "Text": "注册","Weight": 1}),
                ]),
                
            ]
        )
    ]
)
# minimax配置窗口
minimax_config_window = dispatcher.AddWindow(
    {
        "ID": "MiniMaxConfigWin",
        "WindowTitle": "MiniMax API",
        "Geometry": [900, 400, 400, 200],
        "Hidden": True,
        "StyleSheet": """
        * {
            font-size: 14px; /* 全局字体大小 */
        }
    """
    },
    [
        ui.VGroup(
            [
                ui.Label({"ID": "minimaxLabel","Text": "填写MiniMax API信息", "Alignment": {"AlignHCenter": True, "AlignVCenter": True}}),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"Text": "GroupID", "Weight": 0.2}),
                    ui.LineEdit({"ID": "minimaxGroupID", "Weight": 0.8}),
                ]),
                ui.HGroup({"Weight": 1}, [
                    ui.Label({"ID": "minimaxApiKeyLabel","Text": "密钥", "Weight": 0.2}),
                    ui.LineEdit({"ID": "minimaxApiKey", "EchoMode": "Password", "Weight": 0.8})
                ]),
                ui.CheckBox({"ID": "intlCheckBox", "Text": "海外", "Checked": False, "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                ui.HGroup({"Weight": 1}, [
                    ui.Button({"ID": "MiniMaxConfirm", "Text": "确定","Weight": 1}),
                    ui.Button({"ID": "minimaxRegisterButton", "Text": "注册","Weight": 1}),
                ]),
                
            ]
        )
    ]
)

# minimax配置窗口
minimax_clone_window = dispatcher.AddWindow(
    {
        "ID": "MiniMaxCloneWin",
        "WindowTitle": "MiniMax Clone",
        "Geometry": [X_CENTER, Y_CENTER, 600, 420],
        "Hidden": True,
        "StyleSheet": """
        * {
            font-size: 14px; /* 全局字体大小 */
        }
    """
    },
    ui.VGroup( [
        ui.HGroup({"Weight": 0.1}, [
                        ui.Label({"ID": "minimaxCloneLabel","Text": "MiniMax 克隆音色", "Alignment": {"AlignHCenter": True, "AlignVCenter": True,"Weight": 0.1}}),
                        ]),
                        
        ui.HGroup({ "Weight": 1},
            [
                ui.VGroup({"Weight": 1, "Spacing": 10,},
                    [
                        
                        #ui.TextEdit({"ID": "minimaxCloneGuide", "Text": "", "ReadOnly": True, "Font": ui.Font({"PixelSize": 14})}),
                        
                        ui.CheckBox({"ID": "minimaxOnlyAddID", "Text": "已有克隆音色", "Checked": True, "Alignment": {"AlignRight": True}, "Weight": 0.1}),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"ID": "minimaxCloneVoiceNameLabel","Text": "Name", "Weight": 0.2}),
                            ui.LineEdit({"ID": "minimaxCloneVoiceName", "Weight": 0.8})
                        ]),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"ID": "minimaxCloneVoiceIDLabel","Text": "ID", "Weight": 0.2}),
                            ui.LineEdit({"ID": "minimaxCloneVoiceID", "Weight": 0.8}),
                        ]),
                        ui.HGroup({"Weight": 0.1}, [
                            ui.Label({"ID": "minimaxCloneFileIDLabel","Text": "File ID", "Weight": 0.2}),
                            ui.LineEdit({"ID": "minimaxCloneFileID", "Enabled" : False ,"Weight": 0.8}),
                        ]),
                    
                        ui.HGroup({"Weight": 0.1}, [
                            ui.CheckBox({"ID": "minimaxNeedNoiseReduction", "Text": "是否开启降噪", "Checked": False, "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                            ui.CheckBox({"ID": "minimaxNeedVolumeNormalization", "Text": "音量归一化", "Checked": False, "Alignment": {"AlignLeft": True}, "Weight": 0.1}),
                        ]),
                        ui.Label({"ID": "minimaxClonePreviewLabel","Text": "输入试听文本(限制300字以内)：", "Weight": 0.2}),
                        ui.TextEdit({"ID": "minimaxClonePreviewText", "Text": "", }),
                        
                           
                    ]
                ),
                ui.VGroup( {"Weight": 1, "Spacing": 10},
                    [
                        ui.HGroup({"Weight": 1}, [
                            ui.TextEdit({"ID": "minimaxcloneinfoTxt", "Text": script_clone_info_cn, "ReadOnly": True, "Font": ui.Font({"PixelSize": 14})})
                        ])
                    ]
                ),
            ]
        ),
        ui.HGroup({"Weight": 0.1}, [
                ui.Label({"ID": "minimaxCloneStatus","Text": "", "Weight": 0.2}),
        ]),
        ui.HGroup({"Weight": 0.1}, [
                            ui.Button({"ID": "MiniMaxCloneConfirm", "Text": "添加","Weight": 1}),
                            ui.Button({"ID": "MiniMaxCloneCancel", "Text": "取消","Weight": 1}),
                        ]),  

    ]
    )
)

translations = {
    "cn": {
        "Tabs": ["微软语音", "MiniMax语音", "OpenAI 语音","配置"],
        "GetSubButton": "从时间线获取字幕",
        "minimaxGetSubButton": "从时间线获取字幕",
        "OpenAIGetSubButton": "从时间线获取字幕",
        "BreakLabel": "ms",
        "minimaxBreakLabel": "ms",
        "BreakButton": "停顿",
        "minimaxBreakButton": "停顿",
        "AlphabetButton": "发音",
        "minimaxModelLabel": "模型",
        "OpenAIModelLabel": "模型",
        "minimaxLanguageLabel": "语言",
        "minimaxVoiceLabel": "音色",
        "OpenAIVoiceLabel": "音色",
        "OpenAIPresetLabel": "预设",
        "OpenAIPreviewButton": "试听",
        "OpenAIInstructionLabel": "指令",
        "minimaxPreviewButton":"试听",
        "LanguageLabel": "语言",
        "NameTypeLabel": "类型",
        "NameLabel": "名称",
        "MultilingualLabel": "语言技能",
        "StyleLabel": "风格",
        "minimaxEmotionLabel": "情绪",
        "StyleDegreeLabel": "风格强度",
        "RateLabel": "语速",
        "minimaxRateLabel": "语速",
        "OpenAIRateLabel": "语速",
        "PitchLabel": "音调",
        "minimaxPitchLabel": "音调",
        "VolumeLabel": "音量",
        "minimaxVolumeLabel": "音量",
        "OutputFormatLabel": "格式",
        "minimaxFormatLabel": "格式",
        "OpenAIFormatLabel": "格式",
        "PlayButton": "试听",
        "FromSubButton": "朗读当前字幕",
        "OpenAIFromSubButton": "朗读当前字幕",
        "minimaxFromSubButton": "朗读当前字幕",
        "FromTxtButton": "朗读文本框",
        "minimaxFromTxtButton": "朗读文本框",
        "OpenAIFromTxtButton": "朗读文本框",
        "ResetButton": "重置",
        "minimaxResetButton": "重置",
        "OpenAIResetButton": "重置",
        "PathLabel":"保存路径",
        "Browse":"浏览", 
        "ShowAzure":"配置",
        "ShowMiniMax": "配置",
        "openGuideButton":"使用教程",
        "ShowOpenAI": "配置",
        "ShowMiniMaxClone": "克隆",
        "minimaxDeleteVoice":"删除",
        "CopyrightButton":f"关注公众号：游艺所\n\n>>>点击查看更多信息<<<\n\n© 2025, Copyright by {SCRIPT_AUTHOR}.",
        "infoTxt":script_info_cn,
        "AzureLabel":"填写Azure API信息",
        "RegionLabel":"区域",
        "ApiKeyLabel":"密钥",
        "UnuseAPICheckBox":"停用 API",
        "minimaxSubtitleCheckBox":"生成srt字幕",
        "MoreScriptLabel":"\n———————————更多功能———————————",
        "AITranslatorButton":"AI字幕翻译插件",
        "AzureConfirm":"确定",
        "AzureRegisterButton":"注册",
        "minimaxLabel":"填写MiniMax API信息",
        "minimaxCloneLabel":"添加 MiniMaxAI 克隆音色",
        #"minimaxCloneGuide":"9.9元/音色。\n\n获得复刻音色时，不会立即收取音色复刻费用。\n\n音色的复刻费用将在首次使用此复刻音色进行语音合成时收取。",
        "minimaxCloneVoiceNameLabel":"音色名字",
        "minimaxCloneVoiceIDLabel":"音色 ID",
        "minimaxOnlyAddID":"已有克隆音色ID（在下方填入添加即可）",
        "minimaxCloneFileIDLabel":"音频 ID",
        "minimaxNeedNoiseReduction":"开启降噪",
        "minimaxNeedVolumeNormalization":"音量统一",
        "minimaxClonePreviewLabel":"输入试听文本(限制300字以内)：",
        "minimaxcloneinfoTxt":script_clone_info_cn,
        "minimaxApiKeyLabel":"密钥",
        "intlCheckBox": "海外",
        "MiniMaxConfirm":"确定",
        "MiniMaxCloneConfirm":"添加",
        "MiniMaxCloneCancel":"取消",
        "minimaxRegisterButton":"注册",
        "OpenAILabel":"填写OpenAI API信息",
        "OpenAIBaseURLLabel":"Base URL",
        "OpenAIApiKeyLabel":"密钥",
        "OpenAIConfirm":"确定",
        "OpenAIRegisterButton":"注册",

    },

    "en": {
        "Tabs": ["Azure TTS", "MiniMax TTS","OpenAI TTS", "Configuration"],
        "GetSubButton": "Timeline Subs",
        "minimaxGetSubButton": "Timeline Subs",
        "OpenAIGetSubButton": "Timeline Subs",
        "BreakLabel": "ms",
        "minimaxBreakLabel": "ms",
        "BreakButton": "Break",
        "minimaxBreakButton": "Break",
        "AlphabetButton": "Pronunciation",
        "minimaxModelLabel": "Model",
        "OpenAIModelLabel": "Model",
        "minimaxLanguageLabel": "Language",
        "minimaxVoiceLabel": "Voice",
        "OpenAIVoiceLabel": "Voice",
        "OpenAIPresetLabel": "Preset",
        "OpenAIPreviewButton": "Preview",
        "OpenAIInstructionLabel": "Instruction",
        "openGuideButton":"Usage Tutorial",
        "minimaxPreviewButton":"Preview",
        "LanguageLabel": "Language",
        "NameTypeLabel": "Type",
        "NameLabel": "Name",
        "MultilingualLabel": "Multilingual",
        "StyleLabel": "Style",
        "minimaxEmotionLabel": "Emotion",
        "StyleDegreeLabel": "Style Degree",
        "RateLabel": "Rate",
        "minimaxRateLabel": "Rate",
        "OpenAIRateLabel": "Rate",
        "PitchLabel": "Pitch",
        "minimaxPitchLabel": "Pitch",
        "VolumeLabel": "Volume",
        "minimaxVolumeLabel": "Volume",
        "OutputFormatLabel": "Format",
        "minimaxFormatLabel": "Format",
        "OpenAIFormatLabel": "Format",
        "PlayButton": "Preview",
        "FromSubButton": "Read Subs",
        "minimaxFromSubButton": "Read Subs",
        "OpenAIFromSubButton": "Read Subs",
        "FromTxtButton": "Read Textbox",
        "minimaxFromTxtButton": "Read Textbox",
        "OpenAIFromTxtButton": "Read Textbox",
        "ResetButton": "Reset",
        "minimaxResetButton": "Reset",
        "OpenAIResetButton": "Reset",
        "PathLabel":"Path",
        "Browse":"Browse", 
        "ShowAzure":"Config",
        "ShowMiniMax": "Config",
        "ShowOpenAI": "Config",
        "ShowMiniMaxClone": "Clone",
        "minimaxDeleteVoice":"Delete",
        "CopyrightButton":f"😊Buy Me A Coffe😊\n\n© 2025, Copyright by {SCRIPT_AUTHOR}.",
        "infoTxt":script_info_en,
        "AzureLabel":"Azure API",
        "RegionLabel":"Region",
        "ApiKeyLabel":"Key",
        "UnuseAPICheckBox":"Unuse API",
        "minimaxSubtitleCheckBox":"Subtitle Enable",
        "AzureConfirm":"OK",
        "AzureRegisterButton":"Register",
        "minimaxLabel":"MiniMax API",
        "minimaxCloneLabel":"Add MiniMax Clone Voice",
        "minimaxCloneVoiceNameLabel":"Voice Name",
        "MoreScriptLabel":"\n—————————MORE FEATURES—————————",
        "AITranslatorButton":"AI Subtitle Translator Script",
        #"minimaxCloneGuide":"$3 per voice. \n\nYou won’t be charged for cloning a voice right away \n\n the cloning fee will only be charged the first time you use that cloned voice for speech synthesis.",
        "minimaxCloneVoiceIDLabel":"Voice ID",
        "minimaxCloneFileIDLabel":"File ID",
        "minimaxOnlyAddID":"I already have a clone voice.(just fill in below).",
        "minimaxNeedNoiseReduction":"Noise Reduction",
        "minimaxNeedVolumeNormalization":"Volume Normalization",
        "minimaxClonePreviewLabel":"Input text for cloned voice preview:\n(Limited to 2000 characters. )",
        "minimaxApiKeyLabel":"Key",
        "minimaxcloneinfoTxt":script_clone_info_en,
        "intlCheckBox": "intl",
        "MiniMaxConfirm":"OK",
        "MiniMaxCloneConfirm":"Add",
        "MiniMaxCloneCancel":"Cancel",
        "minimaxRegisterButton":"Register",
        "OpenAILabel":"OpenAI API",
        "OpenAIBaseURLLabel":"Base URL",
        "OpenAIApiKeyLabel":"Key",
        "OpenAIConfirm":"OK",
        "OpenAIRegisterButton":"Register",
    }
}
items = win.GetItems()
azure_items = azure_config_window.GetItems()
minimax_items = minimax_config_window.GetItems()
openai_items = openai_config_window.GetItems()
minimax_clone_items = minimax_clone_window.GetItems()
items["StatusLabel"].Text = ""
items["MyStack"].CurrentIndex = 0

for tab_name in translations["cn"]["Tabs"]:
    items["MyTabs"].AddTab(tab_name)

def toggle_api_checkboxes(unuse_api_checked):
    azure_items["ApiKey"].Enabled = unuse_api_checked
    azure_items["Region"].Enabled = unuse_api_checked
    items["StyleCombo"].Enabled = unuse_api_checked
    items["MultilingualCombo"].Enabled = unuse_api_checked
    items["PlayButton"].Enabled = unuse_api_checked
    items["BreakButton"].Enabled = unuse_api_checked
    items["AlphabetButton"].Enabled = unuse_api_checked
    items["StyleDegreeSpinBox"].Enabled = unuse_api_checked
    items["StyleDegreeSlider"].Enabled = unuse_api_checked
    items["OutputFormatCombo"].Enabled = unuse_api_checked
    print("Using API" if unuse_api_checked else "Not Using API")


subtitle = ""
lang = ""
multilingual='Default'
ssml = ''
flag = True
voice_name = ""
style = None
rate = None
pitch = None
volume = None
style_degree = None
stream = None
minimax_voice_index_initialized = False

def show_warning_message(status_tuple):
    use_english = items["LangEnCheckBox"].Checked
    # 元组索引 0 为英文，1 为中文
    message = status_tuple[0] if use_english else status_tuple[1]
    msgbox = dispatcher.AddWindow(
        {
            "ID": 'msg',
            "WindowTitle": 'Warning',
            "Geometry": [750, 400, 350, 100],
            "Spacing": 10,
        },
        [
            ui.VGroup(
                [
                    ui.Label({"ID": 'WarningLabel', "Text": message}),
                    ui.HGroup(
                        {
                            "Weight": 0,
                        },
                        [
                            ui.Button({"ID": 'OkButton', "Text": 'OK'}),
                        ]
                    ),
                ]
            ),
        ]
    )

    def on_ok_button_clicked(ev):
        dispatcher.ExitLoop()
    msgbox.On.OkButton.Clicked = on_ok_button_clicked

    msgbox.Show()
    dispatcher.RunLoop()
    msgbox.Hide()
    
# 加载Voice
voice_file = os.path.join(config_dir, 'voices_list.json')
if not os.path.exists(voice_file):
    show_warning_message(STATUS_MESSAGES.voices_list)
with open(voice_file, "r", encoding="utf-8") as file:
    voices_data = json.load(file)

azure_voices = voices_data.get("azure_voice", {})
edgeTTS_voices = voices_data.get("edge_voice", {})
openai_voices = voices_data.get("openai_voice", {}).get("voices", [])
minimax_voices = voices_data.get("minimax_system_voice", [])
minimax_clone_voices = voices_data.get("minimax_clone_voices", [])

preset_file = os.path.join(config_dir, 'instruction.json')
if not os.path.exists(preset_file):
    preset_data = {
        "Custom": {
            "Description": ""
        }
    }
else:
    with open(preset_file, "r", encoding="utf-8") as file:
        preset_data = json.load(file)

for preset_name in preset_data:
    items["OpenAIPresetCombo"].AddItem(preset_name)

# 选项变更时触发的函数
def on_openai_preset_combo_changed(event):
    # 获取当前选中的 preset 名称
    selected_preset = items["OpenAIPresetCombo"].CurrentText
    if selected_preset in preset_data:
        description = preset_data[selected_preset]["Description"]
        items["OpenAIInstructionText"].Text = description
    else:
        items["OpenAIInstructionText"].Text = "（未找到对应的描述）"
win.On["OpenAIPresetCombo"].CurrentIndexChanged = on_openai_preset_combo_changed

# 将每个子列表转换为元组
def return_voice_name(name):
    for lang, data in azure_voices.items():
        for voice in data['voices']:
            voice_name = list(voice.keys())[0]
            if voice[voice_name].get("Name") == name:
                return voice_name
    return None


# 填充ComboBox
minimax_models = ["speech-02-hd","speech-02-turbo","speech-01-hd","speech-01-turbo", "speech-01-240228","speech-01-turbo-240228",]
for model in minimax_models:
    items["minimaxModelCombo"].AddItem(model)

openai_models = ["gpt-4o-mini-tts","tts-1", "tts-1-hd"]
for model in openai_models:
    items["OpenAIModelCombo"].AddItem(model)


# 将声音选项添加到 minimaxVoiceCombo
for voice in openai_voices:
    items["OpenAIVoiceCombo"].AddItem(voice)
  
if minimax_clone_voices:
    for voice in minimax_clone_voices:
        items["minimaxVoiceCombo"].AddItem(voice["voice_name"])

for voice  in minimax_voices:
    items["minimaxVoiceCombo"].AddItem(voice["voice_name"])  

        
minimax_language = [
    "中文（普通话）", "中文（粤语）", "English", "Japanese", "Korean",
    "Spanish", "Portuguese", "French", "Indonesian", "German", "Russian",
    "Italian", "Arabic", "Turkish", "Ukrainian", "Vietnamese", "Dutch"
]

# 将语言选项添加到 minimaxLanguageCombo
for lang in minimax_language:
    items["minimaxLanguageCombo"].AddItem(lang)  

def update_voice_list(ev):
    global minimax_voice_index_initialized
    # 当前选中语言
    selected_lang = items["minimaxLanguageCombo"].CurrentText
    # 清空语音下拉框
    items["minimaxVoiceCombo"].Clear()  # _README_WORKFLOW_20.txt](file-service://file-27aT4jFAer9mu7jVoLKdot)

    # 只添加与 selected_lang 匹配的条目
    for voice in minimax_clone_voices + minimax_voices:
        if voice.get("language") == selected_lang:
            items["minimaxVoiceCombo"].AddItem(voice["voice_name"])
    # 只在第一次设置
    if not minimax_voice_index_initialized:
        items["minimaxVoiceCombo"].CurrentIndex = saved_settings.get(
            "minimax_Voice",
            default_settings["minimax_Voice"]
        )
        minimax_voice_index_initialized = True
win.On["minimaxLanguageCombo"].CurrentIndexChanged = update_voice_list         


# 定义情绪选项
emotions = [
    ("默认", "Default"),
    ("高兴", "happy"),
    ("悲伤", "sad"),
    ("愤怒", "angry"),
    ("害怕", "fearful"),
    ("厌恶", "disgusted"),
    ("惊讶", "surprised"),
    ("中性", "neutral")
]

# 将情绪选项添加到 minimaxEmotionCombo
for cn, en in emotions:
    if items["LangEnCheckBox"].Checked:
        items["minimaxEmotionCombo"].AddItem(en)  # 选中时添加英文
    else:
        items["minimaxEmotionCombo"].AddItem(cn)  # 未选中时添加中文

# 填充格式选项
items["minimaxFormatCombo"].AddItem("mp3")
items["minimaxFormatCombo"].AddItem("wav")
#items["minimaxFormatCombo"].AddItem("pcm")
items["OpenAIFormatCombo"].AddItem("mp3")
items["OpenAIFormatCombo"].AddItem("wav")


# 模型选项切换逻辑
def on_minimax_model_combo_changed(event):
    selected_model = items["minimaxModelCombo"].CurrentText
    if selected_model in [ "speech-01-240228","speech-01-turbo-240228",]:
        items["minimaxEmotionCombo"].CurrentIndex = 0
        items["minimaxEmotionCombo"].Enabled = False  # 启用情绪选择
    else:
        items["minimaxEmotionCombo"].Enabled = True  # 禁用情绪选择
    if selected_model in [ "speech-01-hd","speech-01-turbo",]:
        items["minimaxSubtitleCheckBox"].Enabled = True
    else:
        items["minimaxSubtitleCheckBox"].Checked = False
        items["minimaxSubtitleCheckBox"].Enabled = False

win.On["minimaxModelCombo"].CurrentIndexChanged = on_minimax_model_combo_changed

def on_openai_model_combo_changed(event):
    selected_model = items["OpenAIModelCombo"].CurrentText
    if selected_model not in ["tts-1", "tts-1-hd"]:
        items["OpenAIInstructionText"].PlaceholderText = ""
        items["OpenAIInstructionText"].Enabled = True  
        items["OpenAIPresetCombo"].Enabled = True  
    else:
        items["OpenAIInstructionText"].PlaceholderText = "Does not work with tts-1 or tts-1-hd."
        items["OpenAIInstructionText"].Enabled = False
        items["OpenAIPresetCombo"].CurrentIndex = 0    
        items["OpenAIPresetCombo"].Enabled = False  

win.On["OpenAIModelCombo"].CurrentIndexChanged = on_openai_model_combo_changed
# 在启动时检查模型状态
on_minimax_model_combo_changed({"Index": items["minimaxModelCombo"].CurrentIndex})
on_openai_model_combo_changed({"Index": items["OpenAIModelCombo"].CurrentIndex})


# 汉化映射字典
StyleMapping = {
    "cheerful": "愉悦",
    "angry": "愤怒",
    "chat": "聊天",
    "customerservice": "客服",
    "empathetic": "同理心",
    "excited": "兴奋",
    "friendly": "友好",
    "hopeful": "有希望的",
    "narration-professional": "专业叙述",
    "newscast-casual": "新闻播报-休闲",
    "newscast-formal": "新闻播报-正式",
    "newscast": "新闻播报",
    "sad": "悲伤",
    "livecommercial":"实时广告",
    "story":"故事",
    "shouting": "喊叫",
    "terrified": "害怕",
    "unfriendly": "不友好",
    "whispering": "耳语",
    "whisper": "耳语",
    "affectionate": "撒娇",
    "calm": "平静",
    "disgruntled": "不满",
    "embarrassed": "尴尬",
    "fearful": "害怕",
    "gentle": "温柔",
    "serious": "严肃",
    "assistant": "助手",
    "chat-casual": "聊天-休闲",
    "lyrical": "抒情",
    "poetry-reading": "诗歌朗诵",
    "sorry": "抱歉",
    "advertisement-upbeat": "广告-积极",
    "depressed": "沮丧",
    "envious": "嫉妒",
    "documentary-narration": "纪录片叙述",
    "narration-relaxed": "叙述-放松",
    "sports-commentary": "体育评论",
    "sports-commentary-excited": "体育评论-兴奋"
}
NameTypeMapping = {
    "女性": "Female",
    "男性": "Male",
    "儿童": "Child",
    "中性": "Neutral"
}
def translate_styles_to_chinese(style_code):
    return StyleMapping.get(style_code, style_code)

def get_original_style(chinese_style):
    for eng, chi in StyleMapping.items():
        if chi == chinese_style:
            return eng
    return chinese_style

for cn, en in NameTypeMapping.items():
    if items["LangEnCheckBox"].Checked:
        items["NameTypeCombo"].AddItem(en)  # 选中时添加英文
    else:
        items["NameTypeCombo"].AddItem(cn)  # 未选中时添加中文

Multilinguals = {
    "Multilingual1": {
        "names": [
            "en-US-AndrewMultilingualNeural (Male)", "en-US-AvaMultilingualNeural (Female)", "en-US-BrianMultilingualNeural (Male)", 
            "en-US-EmmaMultilingualNeural (Female)", "en-GB-AdaMultilingualNeural (Female)", "en-GB-OllieMultilingualNeural (Male)", 
            "de-DE-SeraphinaMultilingualNeural (Female)", "de-DE-FlorianMultilingualNeural (Male)", "es-ES-IsidoraMultilingualNeural (Female)", 
            "es-ES-ArabellaMultilingualNeural (Female)", "fr-FR-VivienneMultilingualNeural (Female)", "fr-FR-RemyMultilingualNeural (Male)", 
            "it-IT-IsabellaMultilingualNeural (Female)", "it-IT-MarcelloMultilingualNeural (Male)", "it-IT-AlessioMultilingualNeural (Male)", 
            "ja-JP-MasaruMultilingualNeural (Male)", "pt-BR-ThalitaMultilingualNeural (Female)", "zh-CN-XiaoxiaoMultilingualNeural (Female)", 
            "zh-CN-XiaochenMultilingualNeural (Female)", "zh-CN-XiaoyuMultilingualNeural","zh-CN-YunyiMultilingualNeural (Male)","zh-CN-YunfanMultilingualNeural (Male)",
            "zh-CN-YunxiaoMultilingualNeural (Male)"
        ],
        "languages": {
            "af-ZA", "sq-AL", "am-ET", "ar-EG", "ar-SA", "hy-AM", "az-AZ", "eu-ES", "bn-IN", "bs-BA", "bg-BG", "my-MM", "ca-ES", "zh-HK", 
            "zh-CN", "zh-TW", "hr-HR", "cs-CZ", "da-DK", "nl-BE", "nl-NL", "en-AU", "en-CA", "en-HK", "en-IN", "en-IE", "en-GB", "en-US", 
            "et-EE", "fil-PH", "fi-FI", "fr-BE", "fr-CA", "fr-FR", "fr-CH", "gl-ES", "ka-GE", "de-AT", "de-DE", "de-CH", "el-GR", "he-IL", 
            "hi-IN", "hu-HU", "is-IS", "id-ID", "ga-IE", "it-IT", "ja-JP", "jv-ID", "kn-IN", "kk-KZ", "km-KH", "ko-KR", "lo-LA", "lv-LV", 
            "lt-LT", "mk-MK", "ms-MY", "ml-IN", "mt-MT", "mn-MN", "ne-NP", "nb-NO", "ps-AF", "fa-IR", "pl-PL", "pt-BR", "pt-PT", "ro-RO", 
            "ru-RU", "sr-RS", "si-LK", "sk-SK", "sl-SI", "so-SO", "es-MX", "es-ES", "su-ID", "sw-KE", "sv-SE", "ta-IN", "te-IN", "th-TH", 
            "tr-TR", "uk-UA", "ur-PK", "uz-UZ", "vi-VN", "cy-GB", "zu-ZA"
        }
    },
    "Multilingual2": {
        "names": [
            "en-US-AlloyMultilingualNeural (Male)", "en-US-EchoMultilingualNeural (Male)", "en-US-FableMultilingualNeural (Neutral)", 
            "en-US-OnyxMultilingualNeural (Male)", "en-US-NovaMultilingualNeural (Female)", "en-US-ShimmerMultilingualNeural (Female)", 
            "en-US-AlloyMultilingualNeuralHD (Male)", "en-US-EchoMultilingualNeuralHD (Male)", "en-US-FableMultilingualNeuralHD (Neutral)", 
            "en-US-OnyxMultilingualNeuralHD (Male)", "en-US-NovaMultilingualNeuralHD (Female)", "en-US-ShimmerMultilingualNeuralHD (Female)"
        ],
        "languages": {
            "af-ZA", "ar-EG", "hy-AM", "az-AZ", "be-BY", "bs-BA", "bg-BG", "ca-ES", "zh-CN", "hr-HR", "cs-CZ", "da-DK", "nl-NL", "en-US", 
            "et-EE", "fi-FI", "fr-FR", "gl-ES", "de-DE", "el-GR", "he-IL", "hi-IN", "hu-HU", "is-IS", "id-ID", "it-IT", "ja-JP", "kn-IN", 
            "kk-KZ", "ko-KR", "lv-LV", "lt-LT", "mk-MK", "ms-MY", "mr-IN", "mi-NZ", "ne-NP", "nb-NO", "fa-IR", "pl-PL", "pt-BR", "ro-RO", 
            "ru-RU", "sr-RS", "sk-SK", "sl-SI", "es-ES", "sw-KE", "sv-SE", "fil-PH", "ta-IN", "th-TH", "tr-TR", "uk-UA", "ur-PK", "vi-VN", 
            "cy-GB"
        }
    },
    "Multilingual3": {
        "names": ["en-US-JennyMultilingualNeural (Female)", "en-US-RyanMultilingualNeural (Male)"],
        "languages": {
            "ar-EG", "ar-SA", "ca-ES", "zh-HK", "zh-CN", "zh-TW", "cs-CZ", "da-DK", "nl-BE", "nl-NL", "en-AU", "en-CA", "en-HK", "en-IN", 
            "en-IE", "en-GB", "en-US", "fi-FI", "fr-BE", "fr-CA", "fr-FR", "fr-CH", "de-AT", "de-DE", "de-CH", "hi-IN", "hu-HU", "id-ID", 
            "it-IT", "ja-JP", "ko-KR", "nb-NO", "pl-PL", "pt-BR", "pt-PT", "ru-RU", "es-MX", "es-ES", "sv-SE", "th-TH", "tr-TR"
        }
    }
}

lang_translation = {
    "af-ZA": "南非语（南非）",
    "sq-AL": "阿尔巴尼亚语（阿尔巴尼亚）",
    "am-ET": "阿姆哈拉语（埃塞俄比亚）",
    "ar-EG": "阿拉伯语（埃及）",
    "ar-SA": "阿拉伯语（沙特阿拉伯）",
    "hy-AM": "亚美尼亚语（亚美尼亚）",
    "az-AZ": "阿塞拜疆语（阿塞拜疆）",
    "eu-ES": "巴斯克语（西班牙）",
    "bn-IN": "孟加拉语（印度）",
    "bs-BA": "波斯尼亚语（波斯尼亚和黑塞哥维那）",
    "bg-BG": "保加利亚语（保加利亚）",
    "my-MM": "缅甸语（缅甸）",
    "ca-ES": "加泰罗尼亚语（西班牙）",
    "zh-HK": "中文（香港）",
    "zh-CN": "中文（简体，中国）",
    "zh-TW": "中文（繁体，台湾）",
    "hr-HR": "克罗地亚语（克罗地亚）",
    "cs-CZ": "捷克语（捷克）",
    "da-DK": "丹麦语（丹麦）",
    "nl-BE": "荷兰语（比利时）",
    "nl-NL": "荷兰语（荷兰）",
    "en-AU": "英语（澳大利亚）",
    "en-CA": "英语（加拿大）",
    "en-HK": "英语（香港）",
    "en-IN": "英语（印度）",
    "en-IE": "英语（爱尔兰）",
    "en-GB": "英语（英国）",
    "en-US": "英语（美国）",
    "et-EE": "爱沙尼亚语（爱沙尼亚）",
    "fil-PH": "菲律宾语（菲律宾）",
    "fi-FI": "芬兰语（芬兰）",
    "fr-BE": "法语（比利时）",
    "fr-CA": "法语（加拿大）",
    "fr-FR": "法语（法国）",
    "fr-CH": "法语（瑞士）",
    "gl-ES": "加利西亚语（西班牙）",
    "ka-GE": "格鲁吉亚语（格鲁吉亚）",
    "de-AT": "德语（奥地利）",
    "de-DE": "德语（德国）",
    "de-CH": "德语（瑞士）",
    "el-GR": "希腊语（希腊）",
    "he-IL": "希伯来语（以色列）",
    "hi-IN": "印地语（印度）",
    "hu-HU": "匈牙利语（匈牙利）",
    "is-IS": "冰岛语（冰岛）",
    "id-ID": "印度尼西亚语（印度尼西亚）",
    "ga-IE": "爱尔兰语（爱尔兰）",
    "it-IT": "意大利语（意大利）",
    "ja-JP": "日语（日本）",
    "jv-ID": "爪哇语（印度尼西亚）",
    "kn-IN": "卡纳达语（印度）",
    "kk-KZ": "哈萨克语（哈萨克斯坦）",
    "km-KH": "高棉语（柬埔寨）",
    "ko-KR": "韩语（韩国）",
    "lo-LA": "老挝语（老挝）",
    "lv-LV": "拉脱维亚语（拉脱维亚）",
    "lt-LT": "立陶宛语（立陶宛）",
    "mk-MK": "马其顿语（北马其顿）",
    "ms-MY": "马来语（马来西亚）",
    "ml-IN": "马拉雅拉姆语（印度）",
    "mt-MT": "马耳他语（马耳他）",
    "mn-MN": "蒙古语（蒙古）",
    "ne-NP": "尼泊尔语（尼泊尔）",
    "nb-NO": "挪威语（挪威）",
    "ps-AF": "普什图语（阿富汗）",
    "fa-IR": "波斯语（伊朗）",
    "pl-PL": "波兰语（波兰）",
    "pt-BR": "葡萄牙语（巴西）",
    "pt-PT": "葡萄牙语（葡萄牙）",
    "ro-RO": "罗马尼亚语（罗马尼亚）",
    "ru-RU": "俄语（俄罗斯）",
    "sr-RS": "塞尔维亚语（塞尔维亚）",
    "si-LK": "僧伽罗语（斯里兰卡）",
    "sk-SK": "斯洛伐克语（斯洛伐克）",
    "sl-SI": "斯洛文尼亚语（斯洛文尼亚）",
    "so-SO": "索马里语（索马里）",
    "es-MX": "西班牙语（墨西哥）",
    "es-ES": "西班牙语（西班牙）",
    "su-ID": "巽他语（印度尼西亚）",
    "sw-KE": "斯瓦希里语（肯尼亚）",
    "sv-SE": "瑞典语（瑞典）",
    "ta-IN": "泰米尔语（印度）",
    "te-IN": "泰卢固语（印度）",
    "th-TH": "泰语（泰国）",
    "tr-TR": "土耳其语（土耳其）",
    "uk-UA": "乌克兰语（乌克兰）",
    "ur-PK": "乌尔都语（巴基斯坦）",
    "uz-UZ": "乌兹别克语（乌兹别克斯坦）",
    "vi-VN": "越南语（越南）",
    "cy-GB": "威尔士语（英国）",
    "zu-ZA": "祖鲁语（南非）"
}

def switch_language(lang):
    """
    根据 lang (可取 'cn' 或 'en') 切换所有控件的文本
    """
    items["NameTypeCombo"].Clear()
    items["minimaxEmotionCombo"].Clear()

    if "MyTabs" in items:
        for index, new_name in enumerate(translations[lang]["Tabs"]):
            items["MyTabs"].SetTabText(index, new_name)

    for item_id, text_value in translations[lang].items():
        # 确保 items[item_id] 存在，否则会报 KeyError
        if item_id == "Tabs":
            continue
        if item_id in items:
            items[item_id].Text = text_value
        elif item_id in azure_items:
            azure_items[item_id].Text = text_value
        elif item_id in minimax_items:    
            minimax_items[item_id].Text = text_value
        elif item_id in openai_items:    
            openai_items[item_id].Text = text_value
        elif item_id in minimax_clone_items:    
            minimax_clone_items[item_id].Text = text_value
        else:
            print(f"[Warning] items 中不存在 ID 为 {item_id} 的控件，无法设置文本！")

    # 缓存复选框状态
    checked = items["LangEnCheckBox"].Checked

    # 名称类型
    for cn, en in NameTypeMapping.items():
        items["NameTypeCombo"].AddItem(en if checked else cn)

    # 情感列表
    for cn, en in emotions:
        items["minimaxEmotionCombo"].AddItem(en if checked else cn)


def on_cn_checkbox_clicked(ev):
    items["LangEnCheckBox"].Checked = not items["LangCnCheckBox"].Checked
    if items["LangEnCheckBox"].Checked:
        switch_language("en")
        print("en")
    else:
        print("cn")
        switch_language("cn")
win.On.LangCnCheckBox.Clicked = on_cn_checkbox_clicked

def on_en_checkbox_clicked(ev):
    items["LangCnCheckBox"].Checked = not items["LangEnCheckBox"].Checked
    if items["LangEnCheckBox"].Checked:
        switch_language("en")
        print("en")
    else:
        print("cn")
        switch_language("cn")
win.On.LangEnCheckBox.Clicked = on_en_checkbox_clicked

def update_name_combo(items, lang, voice_dict):
    items["NameCombo"].Clear()
    selected_type = get_english_name_type(items["NameTypeCombo"].CurrentText)
    matching_voices = []
    for voice in voice_dict[lang]['voices']:
        voice_name = list(voice.keys())[0]
        voice_gender = voice[voice_name]["Gender"]
        if selected_type in voice_gender:
            display_name = voice[voice_name].get("Name", voice_name)
            matching_voices.append(display_name)
    for display_name in matching_voices:
        items["NameCombo"].AddItem(display_name)  

# 从保存的设置中设置 UnuseAPICheckBox 的状态
if saved_settings:
    azure_items["UnuseAPICheckBox"].Checked = saved_settings.get("UNUSE_API", default_settings["UNUSE_API"])
    items["LangCnCheckBox"].Checked = saved_settings.get("CN", default_settings["CN"])
    items["LangEnCheckBox"].Checked = saved_settings.get("EN", default_settings["EN"])

if items["LangEnCheckBox"].Checked :
    switch_language("en")
else:
    switch_language("cn")


def get_english_name_type(chinese_name_type):
    return NameTypeMapping.get(chinese_name_type, chinese_name_type)

audio_formats = {
    "8k, .wav": speechsdk.SpeechSynthesisOutputFormat.Riff8Khz16BitMonoPcm,
    "16k, .wav": speechsdk.SpeechSynthesisOutputFormat.Riff16Khz16BitMonoPcm,
    "24k, .wav": speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm,
    "48k, .wav": speechsdk.SpeechSynthesisOutputFormat.Riff48Khz16BitMonoPcm,
   # "16k, .mp3": speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3,
   # "24k, .mp3": speechsdk.SpeechSynthesisOutputFormat.Audio24Khz48KBitRateMonoMp3,
   # "48k, .mp3": speechsdk.SpeechSynthesisOutputFormat.Audio48Khz96KBitRateMonoMp3
}

for fmt in audio_formats.keys():
    items["OutputFormatCombo"].AddItem(fmt)

# 根据 UnuseAPICheckBox 的状态定义 voice_dict
voice_dict = {}

if azure_items["UnuseAPICheckBox"].Checked:
    voice_dict = edgeTTS_voices
else:
    voice_dict = azure_voices

Language = [voice_dict[locale]['language'] for locale in voice_dict.keys()]

for language in Language:
    items["LanguageCombo"].AddItem(language)

if saved_settings:
    azure_items["ApiKey"].Text = saved_settings.get("API_KEY", default_settings["API_KEY"])
    azure_items["Region"].Text = saved_settings.get("REGION", default_settings["REGION"])
    items["LanguageCombo"].CurrentIndex = saved_settings.get("LANGUAGE", default_settings["LANGUAGE"])
    items["NameTypeCombo"].CurrentIndex = saved_settings.get("TYPE", default_settings["TYPE"])
    items["NameCombo"].CurrentIndex = saved_settings.get("NAME", default_settings["NAME"])
    items["RateSpinBox"].Value = saved_settings.get("RATE", default_settings["RATE"])
    items["PitchSpinBox"].Value = saved_settings.get("PITCH", default_settings["PITCH"])
    items["VolumeSpinBox"].Value = saved_settings.get("VOLUME", default_settings["VOLUME"])
    items["StyleCombo"].CurrentIndex = saved_settings.get("STYLE", default_settings["STYLE"])
    items["StyleDegreeSpinBox"].Value = saved_settings.get("STYLEDEGREE", default_settings["STYLEDEGREE"])
    items["OutputFormatCombo"].CurrentIndex = saved_settings.get("OUTPUT_FORMATS", default_settings["OUTPUT_FORMATS"])

    minimax_items["minimaxApiKey"].Text = saved_settings.get("minimax_API_KEY", default_settings["minimax_API_KEY"])
    minimax_items["minimaxGroupID"].Text = saved_settings.get("minimax_GROUP_ID", default_settings["minimax_GROUP_ID"])
    minimax_items["intlCheckBox"].Checked = saved_settings.get("minimax_intlCheckBox", default_settings["minimax_intlCheckBox"])
    items["Path"].Text = saved_settings.get("Path", default_settings["Path"])
    items["minimaxModelCombo"].CurrentIndex = saved_settings.get("minimax_Model", default_settings["minimax_Model"])
    items["minimaxLanguageCombo"].CurrentIndex= saved_settings.get("minimax_Language", default_settings["minimax_Language"])
    items["minimaxVoiceCombo"].CurrentIndex= saved_settings.get("minimax_Voice", default_settings["minimax_Voice"])
    items["minimaxSubtitleCheckBox"].Checked = saved_settings.get("minimax_SubtitleCheckBox", default_settings["minimax_SubtitleCheckBox"])
    items["minimaxEmotionCombo"].CurrentIndex = saved_settings.get("minimax_Emotion", default_settings["minimax_Emotion"])
    items["minimaxRateSpinBox"].Value = saved_settings.get("minimax_Rate", default_settings["minimax_Rate"])
    items["minimaxVolumeSpinBox"].Value = saved_settings.get("minimax_Volume", default_settings["minimax_Volume"])
    items["minimaxPitchSpinBox"].Value = saved_settings.get("minimax_Pitch", default_settings["minimax_Pitch"])
    items["minimaxFormatCombo"].CurrentIndex = saved_settings.get("minimax_Format", default_settings["minimax_Format"])
    
    openai_items["OpenAIApiKey"].Text = saved_settings.get("OpenAI_API_KEY", default_settings["OpenAI_API_KEY"])
    openai_items["OpenAIBaseURL"].Text = saved_settings.get("OpenAI_BASE_URL", default_settings["OpenAI_BASE_URL"])    
    items["OpenAIModelCombo"].CurrentIndex = saved_settings.get("OpenAI_Model", default_settings["OpenAI_Model"])
    items["OpenAIVoiceCombo"].CurrentIndex= saved_settings.get("OpenAI_Voice", default_settings["OpenAI_Voice"])
    items["OpenAIPresetCombo"].CurrentIndex = saved_settings.get("OpenAI_Preset", default_settings["OpenAI_Preset"])
    items["OpenAIRateSpinBox"].Value = saved_settings.get("OpenAI_Rate", default_settings["OpenAI_Rate"])
    items["OpenAIFormatCombo"].CurrentIndex = saved_settings.get("OpenAI_Format", default_settings["OpenAI_Format"])
    items["OpenAIInstructionText"].Text = saved_settings.get("OpenAI_Instruction", default_settings["OpenAI_Instruction"])

def flagmark():
    global flag
    flag = True
def on_outputformat_combo_current_index_changed(ev):
    flagmark()
win.On.OutputFormatCombo.CurrentIndexChanged = on_outputformat_combo_current_index_changed

def on_multilingual_combo_current_index_changed(ev):
    flagmark()
win.On.MultilingualCombo.CurrentIndexChanged = on_multilingual_combo_current_index_changed

def on_style_combo_current_index_changed(ev):
    flagmark()
win.On.StyleCombo.CurrentIndexChanged = on_style_combo_current_index_changed


# 定义一个通用的更新函数
def handle_value_change(ev, last_update_time, update_interval, from_widget, to_widget, multiplier=1.0):
    current_time = time.time()
    if current_time - last_update_time < update_interval:
        return last_update_time
    flagmark()
    value = round(ev['Value'] * multiplier, 2)
    items[to_widget].Value = value
    return current_time

# 定义全局变量
last_updates = {
    "style_degree": 0,
    "rate": 0,
    "pitch": 0,
    "volume": 0
}
update_intervals = {
    "style_degree": 0.1,
    "rate": 0.1,
    "pitch": 0.1,
    "volume": 0.1
}
# 速率 Slider 和 SpinBox 事件处理
def on_minimax_rate_slider_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "minimaxRateSlider", "minimaxRateSpinBox", 1/100.0)
win.On.minimaxRateSlider.ValueChanged = on_minimax_rate_slider_value_changed

def on_minimax_rate_spinbox_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "minimaxRateSpinBox", "minimaxRateSlider", 100)
win.On.minimaxRateSpinBox.ValueChanged = on_minimax_rate_spinbox_value_changed

# 速率 Slider 和 SpinBox 事件处理
def on_openai_rate_slider_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "OpenAIRateSlider", "OpenAIRateSpinBox", 1/100.0)
win.On.OpenAIRateSlider.ValueChanged = on_openai_rate_slider_value_changed

def on_openai_rate_spinbox_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "OpenAIRateSpinBox", "OpenAIRateSlider", 100)
win.On.OpenAIRateSpinBox.ValueChanged = on_openai_rate_spinbox_value_changed

# 音调 Slider 和 SpinBox 事件处理
def on_minimax_pitch_slider_value_changed(ev):
    last_updates["pitch"] = handle_value_change(ev, last_updates["pitch"], update_intervals["pitch"], "minimaxPitchSlider", "minimaxPitchSpinBox", 1/100.0)
win.On.minimaxPitchSlider.ValueChanged = on_minimax_pitch_slider_value_changed

def on_minimax_pitch_spinbox_value_changed(ev):
    last_updates["pitch"] = handle_value_change(ev, last_updates["pitch"], update_intervals["pitch"], "minimaxPitchSpinBox", "minimaxPitchSlider", 100)
win.On.minimaxPitchSpinBox.ValueChanged = on_minimax_pitch_spinbox_value_changed

# 音量 Slider 和 SpinBox 事件处理
def on_minimax_volume_slider_value_changed(ev):
    last_updates["volume"] = handle_value_change(ev, last_updates["volume"], update_intervals["volume"], "minimaxVolumeSlider", "minimaxVolumeSpinBox", 1/100.0)
win.On.minimaxVolumeSlider.ValueChanged = on_minimax_volume_slider_value_changed

def on_minimax_volume_spinbox_value_changed(ev):
    last_updates["volume"] = handle_value_change(ev, last_updates["volume"], update_intervals["volume"], "minimaxVolumeSpinBox", "minimaxVolumeSlider", 100)
win.On.minimaxVolumeSpinBox.ValueChanged = on_minimax_volume_spinbox_value_changed

# 样式度 Slider 和 SpinBox 事件处理
def on_style_degree_slider_value_changed(ev):
    last_updates["style_degree"] = handle_value_change(ev, last_updates["style_degree"], update_intervals["style_degree"], "StyleDegreeSlider", "StyleDegreeSpinBox", 1/100.0)
win.On.StyleDegreeSlider.ValueChanged = on_style_degree_slider_value_changed

def on_style_degree_spinbox_value_changed(ev):
    last_updates["style_degree"] = handle_value_change(ev, last_updates["style_degree"], update_intervals["style_degree"], "StyleDegreeSpinBox", "StyleDegreeSlider", 100)
win.On.StyleDegreeSpinBox.ValueChanged = on_style_degree_spinbox_value_changed

# 速率 Slider 和 SpinBox 事件处理
def on_rate_slider_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "RateSlider", "RateSpinBox", 1/100.0)
win.On.RateSlider.ValueChanged = on_rate_slider_value_changed

def on_rate_spinbox_value_changed(ev):
    last_updates["rate"] = handle_value_change(ev, last_updates["rate"], update_intervals["rate"], "RateSpinBox", "RateSlider", 100)
win.On.RateSpinBox.ValueChanged = on_rate_spinbox_value_changed

# 音调 Slider 和 SpinBox 事件处理
def on_pitch_slider_value_changed(ev):
    last_updates["pitch"] = handle_value_change(ev, last_updates["pitch"], update_intervals["pitch"], "PitchSlider", "PitchSpinBox", 1/100.0)
win.On.PitchSlider.ValueChanged = on_pitch_slider_value_changed

def on_pitch_spinbox_value_changed(ev):
    last_updates["pitch"] = handle_value_change(ev, last_updates["pitch"], update_intervals["pitch"], "PitchSpinBox", "PitchSlider", 100)
win.On.PitchSpinBox.ValueChanged = on_pitch_spinbox_value_changed

# 音量 Slider 和 SpinBox 事件处理
def on_volume_slider_value_changed(ev):
    last_updates["volume"] = handle_value_change(ev, last_updates["volume"], update_intervals["volume"], "VolumeSlider", "VolumeSpinBox", 1/100.0)
win.On.VolumeSlider.ValueChanged = on_volume_slider_value_changed

def on_volume_spinbox_value_changed(ev):
    last_updates["volume"] = handle_value_change(ev, last_updates["volume"], update_intervals["volume"], "VolumeSpinBox", "VolumeSlider", 100)
win.On.VolumeSpinBox.ValueChanged = on_volume_spinbox_value_changed

def on_my_tabs_current_changed(ev):
    items["MyStack"].CurrentIndex = ev["Index"]
win.On.MyTabs.CurrentChanged = on_my_tabs_current_changed

def on_subtitle_text_changed(ev):
    flagmark()
    global stream
    stream = None
win.On.AzureTxt.TextChanged = on_subtitle_text_changed

def on_minimax_only_add_id_checkbox_clicked(ev):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()

    if not current_timeline:
        print("❌ 当前没有打开的时间线。")
        return

    checked = minimax_clone_items["minimaxOnlyAddID"].Checked
    en_checked = items["LangEnCheckBox"].Checked
    marker_frame = 0
    #print(marker_frame)
    marker_name = "Clone Marker" if en_checked else "克隆标记" 
    marker_note = "Drag the marker points to define the range for clone audio, which should be greater than 10 seconds and less than 5 minutes." if en_checked else"拖拽Mark点范围确定克隆音频的范围，大于10s，小于5分钟"
    marker_date = "clone"
    marker_color = "Red"
    marker_duration = 250
    if checked:
        success = current_timeline.DeleteMarkerByCustomData(marker_date)
        print("✅ 成功删除 Marker！" if success else "❌ 删除 Marker 失败，请手动删除")
    else:
        current_timeline.DeleteMarkerAtFrame(marker_frame)
        success = current_timeline.AddMarker(
            marker_frame,
            marker_color,
            marker_name,
            marker_note,
            marker_duration,
            marker_date
        )
        print("✅ 成功添加 Marker！" if success else "❌ 添加 Marker 失败，请检查frameId或其他参数是否正确。")

    # 批量处理控件启用状态
    for key in ["minimaxNeedNoiseReduction", "minimaxNeedVolumeNormalization", "minimaxClonePreviewText"]:
        minimax_clone_items[key].Enabled = not checked

    # 设置按钮文本
    minimax_clone_items["MiniMaxCloneConfirm"].Text = ("Add" if checked else "Clone") if items["LangEnCheckBox"].Checked else ("添加" if checked else "克隆")
minimax_clone_window.On.minimaxOnlyAddID.Clicked = on_minimax_only_add_id_checkbox_clicked

def on_unuseapi_checkbox_clicked(ev):
    global voice_dict,Language
    items["LanguageCombo"].Clear()
    if azure_items["UnuseAPICheckBox"].Checked:
        toggle_api_checkboxes(False)
        voice_dict = edgeTTS_voices
    else:
        toggle_api_checkboxes(True)
        voice_dict = azure_voices
    Language = [voice_dict[locale]['language'] for locale in voice_dict.keys()]
    for language in Language:
        items["LanguageCombo"].AddItem(language)
    update_name_combo(items, lang, voice_dict)
    
azure_config_window.On.UnuseAPICheckBox.Clicked = on_unuseapi_checkbox_clicked

def on_language_combo_current_index_changed(ev):
    flagmark()
    global lang
    lang_index = items["LanguageCombo"].CurrentIndex
    if lang_index == 0 and not azure_items["UnuseAPICheckBox"].Checked:
        items["AlphabetButton"].Enabled = True
    else:
        items["AlphabetButton"].Enabled = False
    selected_language = Language[lang_index]
    lang = next(locale for locale, data in voice_dict.items() if data['language'] == selected_language)
    update_name_combo(items, lang, voice_dict)
    
win.On.LanguageCombo.CurrentIndexChanged = on_language_combo_current_index_changed

def on_name_combo_current_index_changed(ev):
    flagmark()
    items["StyleCombo"].Clear()
    items["StyleCombo"].AddItem('Default')
    items["StyleCombo"].Enabled = False
    items["MultilingualCombo"].Clear()
    items["MultilingualCombo"].AddItem('Default')
    items["MultilingualCombo"].Enabled = False
    if azure_items["UnuseAPICheckBox"].Checked:
        return
    
    selected_voice = return_voice_name(items["NameCombo"].CurrentText)
    
    # 查找并更新风格选项
    found_voice = False
    valid_styles = False
    for voice_locale, locale_data in azure_voices.items():
        for voice_dict in locale_data["voices"]:
            if selected_voice in voice_dict:
                found_voice = True
                voice_info = voice_dict[selected_voice]
                styles = voice_info.get("Styles", [])  # 安全获取 Styles 列表，避免 KeyError
                # 过滤掉空字符串
                filtered_styles = [style for style in styles if style.strip()]
                if filtered_styles:
                    valid_styles = True
                    items["StyleCombo"].Enabled = True  # 有有效风格时启用下拉菜单
                    for style in filtered_styles:
                        if items["LangCnCheckBox"].Checked:
                            items["StyleCombo"].AddItem(StyleMapping.get(style, style))
                        else:
                            items["StyleCombo"].AddItem(style)    
                break  # 找到后终止循环
        if found_voice:
            break

    if not found_voice or not valid_styles:  # 如果没有找到声音或有效风格为空
        items["StyleCombo"].Enabled = False  # 禁用风格选择

    if "Multilingual" in selected_voice:
        items["MultilingualCombo"].Enabled = True
        for group_name, data in Multilinguals.items():
            cleaned_names = [n.split(' (')[0] for n in data["names"]]
            if selected_voice in cleaned_names:
                print(group_name)
                for language in data["languages"]:
                    if items["LangCnCheckBox"].Checked:
                        items["MultilingualCombo"].AddItem(lang_translation.get(language, language))
                    else:
                        items["MultilingualCombo"].AddItem(language)
                break 
win.On.NameCombo.CurrentIndexChanged = on_name_combo_current_index_changed

def on_name_type_combo_current_index_changed(ev):
    flagmark()
    update_name_combo(items, lang, voice_dict)
    
win.On.NameTypeCombo.CurrentIndexChanged = on_name_type_combo_current_index_changed


if azure_items["UnuseAPICheckBox"].Checked:
    azure_items["ApiKey"].Enabled = False
    azure_items["Region"].Enabled = False
    items["StyleCombo"].Enabled = False
    items["MultilingualCombo"].Enabled = False
    items["PlayButton"].Enabled = False
    items["BreakButton"].Enabled = False
    items["AlphabetButton"].Enabled = False
    items["StyleDegreeSpinBox"].Enabled = False
    items["StyleDegreeSlider"].Enabled = False
    items["OutputFormatCombo"].Enabled = False

##frame_rate = float(current_project.GetSetting("timelineFrameRate"))

def get_subtitles(timeline):
    subtitles = []
    track_count = timeline.GetTrackCount("subtitle")
    print(f"Subtitle track count: {track_count}")

    for track_index in range(1, track_count + 1):
        track_enabled = timeline.GetIsTrackEnabled("subtitle", track_index)
        if track_enabled:
            subtitleTrackItems = timeline.GetItemListInTrack("subtitle", track_index)
            for item in subtitleTrackItems:
                try:
                    start_frame = item.GetStart()
                    end_frame = item.GetEnd()
                    text = item.GetName()
                    subtitles.append({'start': start_frame, 'end': end_frame, 'text': text})
                except Exception as e:
                    print(f"Error processing item: {e}")

    return subtitles

def get_subtitle_texts(subtitles):
    return "\n".join([subtitle['text'] for subtitle in subtitles])

def frame_to_timecode(frame, framerate):
    total_seconds = frame / framerate
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def timecode_to_frames(timecode, frame_rate):
    """
    将时间码转换为帧数。
    参数：
    - timecode: 格式为 'hh:mm:ss;ff' 或 'hh:mm:ss:ff' 的时间码。
    - frame_rate: 时间线的帧率。
    返回值：
    - 对应时间码的帧数。
    """
    try:
        # 提取时间组件
        match = re.match(r"^(\d{2}):(\d{2}):(\d{2})([:;])(\d{2,3})$", timecode)
        if not match:
            raise ValueError(f"Invalid timecode format: {timecode}")
        
        hours, minutes, seconds, separator, frames = match.groups()
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        frames = int(frames)
        
        is_drop_frame = separator == ';'
        
        if is_drop_frame:
            # 计算名义帧率和丢帧数
            if frame_rate in [23.976, 29.97, 59.94, 119.88]:
                nominal_frame_rate = round(frame_rate * 1000 / 1001)
                drop_frames = int(round(nominal_frame_rate / 15))
            else:
                raise ValueError(f"Unsupported drop frame rate: {frame_rate}")

            # 总分钟数
            total_minutes = hours * 60 + minutes

            # 计算总的丢帧数
            total_dropped_frames = drop_frames * (total_minutes - total_minutes // 10)

            # 计算总帧数
            frame_count = ((hours * 3600) + (minutes * 60) + seconds) * nominal_frame_rate + frames
            frame_count -= total_dropped_frames

        else:
            # 非丢帧时间码
            if frame_rate in [23.976, 29.97, 47.952, 59.94, 95.904, 119.88]:
                nominal_frame_rate = round(frame_rate * 1000 / 1001)
            else:
                nominal_frame_rate = frame_rate

            frame_count = ((hours * 3600) + (minutes * 60) + seconds) * nominal_frame_rate + frames

        return frame_count

    except ValueError as e:
        print(f"Error converting timecode to frames: {e}")
        return None


def print_srt(subtitles, framerate):
    for index, subtitle in enumerate(subtitles):
        start_time = frame_to_timecode(subtitle['start'], framerate)
        end_time = frame_to_timecode(subtitle['end'], framerate)
        print(f"{index + 1}\n{start_time} --> {end_time}\n{subtitle['text']}\n")


def on_getsub_button_clicked(ev):
    frame_rate = float(current_project.GetSetting("timelineFrameRate"))
    subtitles = get_subtitles(current_timeline)
    subtitle_texts = get_subtitle_texts(subtitles)
    items["AzureTxt"].Text = subtitle_texts
    items["minimaxText"].Text = subtitle_texts
    items["OpenAIText"].Text = subtitle_texts
    print_srt(subtitles,frame_rate)
win.On.GetSubButton.Clicked = on_getsub_button_clicked
win.On.minimaxGetSubButton.Clicked = on_getsub_button_clicked
win.On.OpenAIGetSubButton.Clicked = on_getsub_button_clicked

def process_text_with_breaks(parent, text):
    parts = text.split('<break')
    for i, part in enumerate(parts):
        if i == 0:
            handle_phoneme_and_text(parent, part.strip(), is_initial=True)
        else:
            end_idx = part.find('>')
            if end_idx != -1:
                break_tag = '<break' + part[:end_idx + 1]
                remaining_text = part[end_idx + 1:].strip()
                
                break_elem = ET.fromstring(break_tag)
                parent.append(break_elem)
                
                handle_phoneme_and_text(parent, remaining_text)

def handle_phoneme_and_text(parent, text, is_initial=False):
    phoneme_parts = text.split('<phoneme')
    for j, phoneme_part in enumerate(phoneme_parts):
        if j == 0:
            if is_initial:
                if parent.text:
                    parent.text += phoneme_part.strip()
                else:
                    parent.text = phoneme_part.strip()
            else:
                if parent[-1].tail:
                    parent[-1].tail += phoneme_part.strip()
                else:
                    parent[-1].tail = phoneme_part.strip()
        else:
            end_phoneme_idx = phoneme_part.find('</phoneme>')
            if end_phoneme_idx != -1:
                phoneme_end_tag = '</phoneme>'
                phoneme_start_idx = phoneme_part.find('>') + 1
                phoneme_tag = '<phoneme' + phoneme_part[:phoneme_start_idx]
                remaining_text = phoneme_part[phoneme_start_idx:end_phoneme_idx]
                tail_text = phoneme_part[end_phoneme_idx + len(phoneme_end_tag):].strip()
                
                phoneme_elem = ET.fromstring(phoneme_tag + remaining_text + phoneme_end_tag)
                parent.append(phoneme_elem)
                
                if tail_text:
                    if phoneme_elem.tail:
                        phoneme_elem.tail += tail_text
                    else:
                        phoneme_elem.tail = tail_text
            else:
                if parent[-1].tail:
                    parent[-1].tail += phoneme_part.strip()
                else:
                    parent[-1].tail = phoneme_part.strip()

def create_ssml(lang, voice_name, text, rate=None, pitch=None, volume=None, style=None, styledegree=None, multilingual = None):
    speak = ET.Element('speak', xmlns="http://www.w3.org/2001/10/synthesis", attrib={
        "xmlns:mstts": "http://www.w3.org/2001/mstts",
        "xmlns:emo": "http://www.w3.org/2009/10/emotionml",
        "version": "1.0",
        "xml:lang": f"{lang}"
    })
    voice = ET.SubElement(speak, 'voice', name=voice_name)
    if multilingual != None:
        lang_tag = ET.SubElement(voice, 'lang', attrib={"xml:lang": multilingual})
        parent_tag = lang_tag
    else:
        parent_tag = voice
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            paragraph = ET.SubElement(parent_tag, 's')
            if style != "Default":
                express_as_attribs = {'style': style}
                if styledegree is not None and styledegree != 1.0:
                    express_as_attribs['styledegree'] = f"{styledegree:.2f}"
                express_as = ET.SubElement(paragraph, 'mstts:express-as', attrib=express_as_attribs)
                prosody_attrs = {}
                if rate is not None and rate != 1.0:
                    prosody_rate = f"+{(rate-1)*100:.2f}%" if rate > 1 else f"-{(1-rate)*100:.2f}%"
                    prosody_attrs['rate'] = prosody_rate
                if pitch is not None and pitch != 1.0:
                    prosody_pitch = f"+{(pitch-1)*100:.2f}%" if pitch > 1 else f"-{(1-pitch)*100:.2f}%"
                    prosody_attrs['pitch'] = prosody_pitch
                if volume is not None and volume != 1.0:
                    prosody_volume = f"+{(volume-1)*100:.2f}%" if volume > 1 else f"-{(1-volume)*100:.2f}%"
                    prosody_attrs['volume'] = prosody_volume
                if prosody_attrs:
                    prosody = ET.SubElement(express_as, 'prosody', attrib=prosody_attrs)
                    process_text_with_breaks(prosody, line.strip())
                else:
                    process_text_with_breaks(express_as, line.strip())
            else:
                prosody_attrs = {}
                if rate is not None and rate != 1.0:
                    prosody_rate = f"+{(rate-1)*100:.2f}%" if rate > 1 else f"-{(1-rate)*100:.2f}%"
                    prosody_attrs['rate'] = prosody_rate
                if pitch is not None and pitch != 1.0:
                    prosody_pitch = f"+{(pitch-1)*100:.2f}%" if pitch > 1 else f"-{(1-pitch)*100:.2f}%"
                    prosody_attrs['pitch'] = prosody_pitch
                if volume is not None and volume != 1.0:
                    prosody_volume = f"+{(volume-1)*100:.2f}%" if volume > 1 else f"-{(1-volume)*100:.2f}%"
                    prosody_attrs['volume'] = prosody_volume
                if prosody_attrs:
                    prosody = ET.SubElement(paragraph, 'prosody', attrib=prosody_attrs)
                    process_text_with_breaks(prosody, line.strip())
                else:
                    process_text_with_breaks(paragraph, line.strip())
        if multilingual:
            parent_tag.tail = "\n"
    return format_xml(ET.tostring(speak, encoding='unicode'))

def format_xml(xml_string):
    parsed = minidom.parseString(xml_string)
    pretty_xml_as_string = parsed.toprettyxml(indent="", newl="")
    pretty_xml_as_string = ''.join([line for line in pretty_xml_as_string.split('\n') if line.strip()])
    return pretty_xml_as_string


def update_status(status_tuple):
    """
    更新状态信息：
    如果 items["LangEnCheckBox"].Checked 为 True，则选择英文，
    否则选择中文。
    """
    use_english = items["LangEnCheckBox"].Checked
    # 元组索引 0 为英文，1 为中文
    message = status_tuple[0] if use_english else status_tuple[1]
    items["StatusLabel"].Text = message
    items["minimaxStatusLabel"].Text = message
    items["OpenAIStatusLabel"].Text = message
    minimax_clone_items["minimaxCloneStatus"].Text = message
    

def synthesize_speech(service_region, speech_key, lang, voice_name, subtitle, rate, volume, style, style_degree, multilingual,pitch,audio_format, audio_output_config):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.set_speech_synthesis_output_format(audio_format)
    ssml = create_ssml(lang=lang, voice_name=voice_name, text=subtitle, rate=rate, volume=volume, style=style, styledegree=style_degree,multilingual= multilingual,pitch=pitch)
    print(ssml)
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    result = speech_synthesizer.speak_ssml_async(ssml).get()
    
    return result

def get_current_subtitle(current_timeline):
    frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
    current_timecode = current_timeline.GetCurrentTimecode()  
    current_frame = timecode_to_frames(current_timecode, frame_rate)

    track_count = current_timeline.GetTrackCount("subtitle")

    selected_subtitles = []
    for track_index in range(1, track_count + 1):
        items = current_timeline.GetItemListInTrack("subtitle", track_index)
        for item in items:
            start_frame = item.GetStart()
            end_frame = item.GetEnd()
            if start_frame is not None and end_frame is not None and start_frame <= current_frame <= end_frame:
                selected_subtitles.append(item)
    
    for subtitle in selected_subtitles:
        print(f"Start: {frame_to_timecode(subtitle.GetStart(), frame_rate)}")
        print(f"Start: {subtitle.GetStart()}")
        print(f"End: {frame_to_timecode(subtitle.GetEnd(), frame_rate)}")
        print(f"Duration: {subtitle.GetDuration()}")
        print(f"Text: {subtitle.GetName()}")  # 假设字幕文本是通过 GetName() 获取的
        print(subtitle.GetStart())
    if selected_subtitles:
        return selected_subtitles[0].GetName(), selected_subtitles[0].GetStart(), selected_subtitles[0].GetEnd()
    else:
        return None, current_frame, current_frame

def generate_filename(base_path, subtitle, extension):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # 先把换行去掉
    clean_subtitle = subtitle.replace('\n', ' ').replace('\r', ' ')
    # 再用正则去除 Windows 不允许的字符
    clean_subtitle = re.sub(r'[<>:"/\\|?*]', '', clean_subtitle)
    # 也可以控制下长度，比如只取前 15 或 30 个字符等
    clean_subtitle = clean_subtitle[:15]

    count = 0
    while True:
        count += 1
        filename = f"{base_path}/{clean_subtitle}#{count}{extension}"
        if not os.path.exists(filename):
            return filename

def edgetts_speech_synthesis( subtitle, voice_name, rate, pitch, volume, filename, start_frame, end_frame):
    update_status(STATUS_MESSAGES.synthesizing)   
    prosody_rate = f"+{int((rate-1)*100)}%" if rate > 1 else f"-{int((1-rate)*100)}%"
    prosody_pitch = f"+{int((pitch-1)*100)}Hz" if pitch > 1 else f"-{int((1-pitch)*100)}Hz"
    prosody_volume = f"+{int((volume-1)*100)}%" if volume > 1 else f"-{int((1-volume)*100)}%"
    print(f"Voice Name: {voice_name}")
    print(f"Prosody Rate: {prosody_rate}")
    print(f"Prosody Pitch: {prosody_pitch}")
    print(f"Prosody Volume: {prosody_volume}")
    try:
        communicate = edge_tts.Communicate(subtitle, voice_name, rate=prosody_rate, volume=prosody_volume,pitch=prosody_pitch)
        communicate.save_sync(filename)
        time.sleep(1)
        add_to_media_pool_and_timeline(start_frame, end_frame, filename)
        update_status(STATUS_MESSAGES.loaded_to_timeline)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        update_status(STATUS_MESSAGES.synthesis_failed)
    except edge_tts.exceptions.HTTPError as he:
        print(f"HTTPError: {he}")
        update_status(STATUS_MESSAGES.synthesis_failed)
    except Exception as e:
        print(f"Unexpected error: {e}")
        update_status(STATUS_MESSAGES.synthesis_failed)

def on_fromsub_button_clicked(ev):
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    global subtitle,stream,flag
    subtitle,start_frame, end_frame = get_current_subtitle(current_timeline)
    items['AzureTxt'].PlainText = subtitle
    extension = ".mp3" if azure_items["UnuseAPICheckBox"].Checked else items["OutputFormatCombo"].CurrentText.split(", ")[1]
    filename = generate_filename(items["Path"].Text, subtitle, extension)
    #print(filename)
    voice_name = return_voice_name(items["NameCombo"].CurrentText)
    rate = items["RateSpinBox"].Value
    pitch = items["PitchSpinBox"].Value
    volume = items["VolumeSpinBox"].Value
    if azure_items["UnuseAPICheckBox"].Checked:
        edgetts_speech_synthesis( subtitle, voice_name, rate, pitch, volume, filename, start_frame, end_frame)
        return
    if azure_items["ApiKey"].Text == '' or azure_items["Region"].Text == '':
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        update_status(STATUS_MESSAGES.synthesis_failed)
        return
    update_status(STATUS_MESSAGES.synthesizing)
    service_region = azure_items["Region"].Text
    speech_key = azure_items["ApiKey"].Text
    style = get_original_style(items["StyleCombo"].CurrentText)
    style_degree = items["StyleDegreeSpinBox"].Value
    multilingual = items["MultilingualCombo"].CurrentText if items["MultilingualCombo"].CurrentText in lang_translation else next((k for k, v in lang_translation.items() if v == items["MultilingualCombo"].CurrentText), None)
    output_format = items["OutputFormatCombo"].CurrentText
    if output_format in audio_formats:
        audio_format = audio_formats[output_format]
    else:
        show_warning_message(STATUS_MESSAGES.unsupported_audio)
        return

    audio_output_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    
    result = synthesize_speech(service_region, speech_key, lang, voice_name, subtitle, rate,volume, style, style_degree, multilingual,pitch,audio_format, audio_output_config)
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        time.sleep(1)
        add_to_media_pool_and_timeline(start_frame, end_frame, filename)
        flag = False
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        update_status(STATUS_MESSAGES.synthesis_failed)
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

win.On.FromSubButton.Clicked = on_fromsub_button_clicked

def on_fromtxt_button_clicked(ev):
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    global subtitle,stream,flag
    subtitle = items["AzureTxt"].PlainText
    extension = ".mp3" if azure_items["UnuseAPICheckBox"].Checked else items["OutputFormatCombo"].CurrentText.split(", ")[1]
    filename = generate_filename(items["Path"].Text, subtitle, extension)
    #print(filename)
    voice_name = return_voice_name(items["NameCombo"].CurrentText)
    rate = items["RateSpinBox"].Value
    pitch = items["PitchSpinBox"].Value
    volume = items["VolumeSpinBox"].Value
    if azure_items["UnuseAPICheckBox"].Checked:
        frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
        current_timecode = current_timeline.GetCurrentTimecode()  
        current_frame = timecode_to_frames(current_timecode, frame_rate)
        edgetts_speech_synthesis( subtitle, voice_name, rate, pitch, volume, filename, current_frame, current_timeline.GetEndFrame())
        return
    if azure_items["ApiKey"].Text == '' or azure_items["Region"].Text == '':
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        update_status(STATUS_MESSAGES.synthesis_failed)
        return
    print(f"stream:{stream}")
    if stream and flag:
        stream.save_to_wav_file(filename)
        time.sleep(1)
        frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
        current_timecode = current_timeline.GetCurrentTimecode()  
        current_frame = timecode_to_frames(current_timecode, frame_rate)
        add_to_media_pool_and_timeline(current_frame, current_timeline.GetEndFrame(), filename)
        flag = False
        stream =None
    elif not stream and flag:
        update_status(STATUS_MESSAGES.synthesizing)
        service_region = azure_items["Region"].Text
        speech_key = azure_items["ApiKey"].Text
        style = get_original_style(items["StyleCombo"].CurrentText)
        style_degree = items["StyleDegreeSpinBox"].Value
        multilingual = items["MultilingualCombo"].CurrentText if items["MultilingualCombo"].CurrentText in lang_translation else next((k for k, v in lang_translation.items() if v == items["MultilingualCombo"].CurrentText), None)
        output_format = items["OutputFormatCombo"].CurrentText
        if output_format in audio_formats:
            audio_format = audio_formats[output_format]
        else:
            show_warning_message(STATUS_MESSAGES.unsupported_audio)
            return

        audio_output_config = speechsdk.audio.AudioOutputConfig(filename=filename)
        
        result = synthesize_speech(service_region, speech_key, lang, voice_name, subtitle, rate,volume, style, style_degree, multilingual,pitch,audio_format, audio_output_config)
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            time.sleep(1)
            frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
            current_timecode = current_timeline.GetCurrentTimecode()  
            current_frame = timecode_to_frames(current_timecode, frame_rate)
            add_to_media_pool_and_timeline(current_frame, current_timeline.GetEndFrame(), filename)
            flag = False
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            update_status(STATUS_MESSAGES.synthesis_failed)
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
    else:
        update_status(STATUS_MESSAGES.media_clip_exists)
    
win.On.FromTxtButton.Clicked = on_fromtxt_button_clicked

def on_play_button_clicked(ev):
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    if items["AzureTxt"].PlainText == '':
        show_warning_message(STATUS_MESSAGES.prev_txt)
        return
    if azure_items["ApiKey"].Text == '' or azure_items["Region"].Text == '':
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        return
    update_status(STATUS_MESSAGES.playing)
    items["PlayButton"].Enabled = False
    global subtitle, ssml, stream 
    service_region = azure_items["Region"].Text
    speech_key = azure_items["ApiKey"].Text
    style = get_original_style(items["StyleCombo"].CurrentText)
    style_degree = items["StyleDegreeSpinBox"].Value
    subtitle = items["AzureTxt"].PlainText
    rate = items["RateSpinBox"].Value
    pitch = items["PitchSpinBox"].Value
    volume = items["VolumeSpinBox"].Value
    multilingual = items["MultilingualCombo"].CurrentText if items["MultilingualCombo"].CurrentText in lang_translation else next((k for k, v in lang_translation.items() if v == items["MultilingualCombo"].CurrentText), None)
    voice_name = return_voice_name(items["NameCombo"].CurrentText)
    output_format = items["OutputFormatCombo"].CurrentText
    if output_format in audio_formats:
        audio_format = audio_formats[output_format]
    else:
        show_warning_message(STATUS_MESSAGES.unsupported_audio)
        return

    audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    result = synthesize_speech(service_region, speech_key, lang, voice_name, subtitle, rate, volume, style, style_degree, multilingual,pitch,audio_format, audio_output_config)
    stream = speechsdk.AudioDataStream(result)
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        flagmark()
        update_status(STATUS_MESSAGES.reset_status)
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        update_status(STATUS_MESSAGES.synthesis_failed)
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            
    items["PlayButton"].Enabled = True  

win.On.PlayButton.Clicked = on_play_button_clicked

def play_audio_segment(pcm_file, json_file, voice_name, sample_rate=32000, channels=2, sample_width=2):
    try:
        # 读取 JSON 文件
        with open(json_file, 'r', encoding='utf-8') as f:
            voice_data = json.load(f)
        
        # 检查声音名称是否存在
        if voice_name not in voice_data:
            raise ValueError(f"音色 '{voice_name}' 不存在于 JSON 文件中。")
        
        # 获取音频片段起止位置
        start, end = voice_data[voice_name]["start"], voice_data[voice_name]["end"]
        
        # 从 PCM 文件中读取对应片段
        with open(pcm_file, 'rb') as pcm_in:
            pcm_in.seek(start)
            data = pcm_in.read(end - start + 1)
        
        # 将 PCM 数据转化为 WAV 格式
        wav_file = f"{voice_name}_temp.wav"
        print(wav_file)
        with wave.open(wav_file, 'wb') as wav_out:
            wav_out.setnchannels(channels)
            wav_out.setsampwidth(sample_width)
            wav_out.setframerate(sample_rate)
            wav_out.writeframes(data)
        
        # 使用系统命令播放音频
        if os.name == 'nt':  # Windows 系统
            import winsound
            winsound.PlaySound(wav_file, winsound.SND_FILENAME)

        else:  # Linux/Unix 或 macOS
            subprocess.run(['afplay', wav_file], check=True)

        # 删除临时 WAV 文件
        time.sleep(1)  # 等待1秒钟
        os.remove(wav_file)
        print(f"播放完成: {voice_name}")
    
    except Exception as e:
        os.remove(wav_file)
        print(f"播放失败: {e}")

def on_minimax_preview_button_click(ev):
    if minimax_items["intlCheckBox"].Checked:
        webbrowser.open(MINIMAX_PREW_URL)
    else:
        webbrowser.open(MINIMAXI_PREW_URL)
"""
    try:
        # 请确保文件路径正确
        pcm_file = os.path.join(config_dir, "minimax_voice_data.pcm")  # 拼接完整路径
        json_file = os.path.join(config_dir, "minimax_voice_data.json")
        # 检查文件是否存在
        if not os.path.exists(pcm_file):
            show_warning_message(STATUS_MESSAGES.download_pcm)
            return
        if not os.path.exists(json_file):
            show_warning_message(STATUS_MESSAGES.download_json)
            return
        voice_name = items["minimaxVoiceCombo"].CurrentText  # 目标音色

        voice_id = next(
            (v["voice_name"] for v in minimax_voices 
            if voice_name == v["voice_name"] or voice_name == v["voice_id"]),
            ""
        )

        # 播放音频
        play_audio_segment(pcm_file, json_file, voice_id)

    except Exception as e:
        print(f"播放失败: {e}")
"""      
win.On.minimaxPreviewButton.Clicked = on_minimax_preview_button_click

def process_minimax_request(text_func, timeline_func):
    """
    通用处理函数，用于 Minimax 请求和音频处理
    :param text_func: 函数，返回文本内容
    :param timeline_func: 函数，返回 (start_frame, end_frame) 时间线帧信息
    """
    # 获取输入字段的值
    if minimax_items["minimaxGroupID"].Text == '' or minimax_items["minimaxApiKey"].Text == '':
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        update_status(STATUS_MESSAGES.synthesis_failed)
        return
    group_id = minimax_items["minimaxGroupID"].Text
    api_key = minimax_items["minimaxApiKey"].Text
    model = items["minimaxModelCombo"].CurrentText
    text = text_func()
    if minimax_items["intlCheckBox"].Checked:
        url = f"https://api.minimaxi.chat/v1/t2a_v2?GroupId={group_id}"
    else:
        url = f"https://api.minimax.chat/v1/t2a_v2?GroupId={group_id}"
    
    # 获取 voice_id 和 emotion
    voice_name = items["minimaxVoiceCombo"].CurrentText  # 目标音色

    voice_id = next(
        (v["voice_id"] for v in minimax_voices 
        if voice_name == v["voice_name"] or voice_name == v["voice_id"]),
        ""
    )
    if not voice_id:
        voice_id = next(
            (v["voice_id"] for v in minimax_clone_voices 
            if voice_name == v["voice_name"] or voice_name == v["voice_id"]),
            ""
        )

    lang_id = items["minimaxLanguageCombo"].CurrentText
    emotion_name = items["minimaxEmotionCombo"].CurrentText
    emotion_value = next((en for cn, en in emotions if emotion_name in (cn, en)), "")
    
    # 其他参数
    speed = items["minimaxRateSpinBox"].Value
    vol = items["minimaxVolumeSpinBox"].Value
    pitch = items["minimaxPitchSpinBox"].Value
    subtitle_enable = items["minimaxSubtitleCheckBox"].Checked
    sample_rate = 32000
    bitrate = 128000
    channel = 2
    file_format = items["minimaxFormatCombo"].CurrentText

    # 构建请求的Payload
    payload = {
        "model": model,
        "text": text,
        "stream": False,
        "subtitle_enable":subtitle_enable,
        #"language_boost":lang_id,
        "voice_setting": {
            "voice_id": voice_id,
            "speed": speed,
            "vol": vol,
            "pitch": pitch,
            "english_normalization":True,
            "latex_read":True,
        },
        "audio_setting": {
            "sample_rate": sample_rate,
            "bitrate": bitrate,
            "format": file_format,
            "channel": channel
        }
    }

    # 如果 emotion 不为空，添加到 voice_setting 中
    if emotion_value not in ["默认", "Default"]:
        payload["voice_setting"]["emotion"] = emotion_value

    # 转换为 JSON 格式
    payload_json = json.dumps(payload)

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    print(payload)
    update_status(STATUS_MESSAGES.synthesizing)

    try:
        resp = session.post(url, headers=headers, data=payload_json, timeout=(5, 60))

        resp.raise_for_status()
        resp_data = resp.json()
        base_resp = resp_data.get("base_resp", {})
        code = str(base_resp.get("status_code", ""))
        # 仅当 code 非 "0" 时才弹警告
        if code != "0":
            attr = f"error_{code}"
            status_tuple = getattr(
                STATUS_MESSAGES,
                attr,
                STATUS_MESSAGES.error_1000
            )
            show_warning_message(status_tuple)
            update_status(status_tuple)
            raise RuntimeError(f"合成失败，状态码 {code}")

        data = resp_data.get("data")
        if not data:
            update_status(STATUS_MESSAGES.synthesis_failed)
            print("响应中未包含 'data' 字段:", resp_data)
            return
  
        # 处理音频数据
        audio_data = bytes.fromhex(data.get("audio", ""))
        filename = generate_filename(items["Path"].Text, text, f".{file_format}")
        print(filename)
    
        with open(filename, 'wb') as f:
            f.write(audio_data)
        #print(f"音频已保存到 {filename}")
    
        if os.path.exists(filename):
            start_frame, end_frame = timeline_func()
            add_to_media_pool_and_timeline(start_frame, end_frame, filename)
            #print(f"成功将文件添加到媒体池: {filename}")
        else:
            update_status(STATUS_MESSAGES.audio_save_failed)
            print("音频文件保存失败")
            return
    
        # 下载字幕文件及转换为 SRT
        subtitle_url = data.get("subtitle_file")
        if subtitle_url:
            #print("字幕文件URL:", subtitle_url)
            try:
                subtitle_response = session.get(subtitle_url, timeout=(5, 60))
                subtitle_response.raise_for_status()  # 检查响应状态
            
                subtitle_filename = os.path.splitext(filename)[0] + ".json"
                with open(subtitle_filename, 'wb') as f:
                    f.write(subtitle_response.content)
                #print(f"字幕文件已保存到 {subtitle_filename}")

                # 读取 JSON 并转换为 SRT 格式
                with open(subtitle_filename, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                srt_filename = os.path.splitext(subtitle_filename)[0] + ".srt"
                json_to_srt(json_data, srt_filename)
                # 成功生成 SRT 后，删除 JSON 文件
                os.remove(subtitle_filename)
                import_srt_to_timeline(srt_filename)
            except (requests.exceptions.ChunkedEncodingError) as e:
                print(f"字幕处理出错: {e}")
        else:
            print("响应中未包含 'subtitle_file' 字段")
        
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        update_status(STATUS_MESSAGES.synthesis_failed)
    except requests.exceptions.ChunkedEncodingError as e:
        print(f"连接中断或数据读取不完整（ChunkedEncodingError）: {e}")
        update_status(STATUS_MESSAGES.synthesis_failed)
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
        update_status(STATUS_MESSAGES.synthesis_failed)
    except KeyError as e:
        print(f"响应中缺少关键字段: {e}")
        update_status(STATUS_MESSAGES.synthesis_failed)

def json_to_srt(json_data, srt_path):
    """
    将JSON格式的字幕信息转换为 .srt 文件并保存。
    """
    srt_output = []
    subtitle_id = 1
    frame_rate = float(current_timeline.GetSetting("timelineFrameRate"))
    for item in json_data:
        text = item["text"]
        # 移除可能出现的 BOM
        if text.startswith("\ufeff"):
            text = text[1:]
        start_time = frame_to_timecode(item["time_begin"] / 1000,1)
        end_time = frame_to_timecode(item["time_end"] / 1000,1)
        srt_output.append(f"{subtitle_id}")
        srt_output.append(f"{start_time} --> {end_time}")
        srt_output.append(text)
        srt_output.append("")
        subtitle_id += 1
    try:
        with open(srt_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(srt_output))
        print(f"SRT 文件已保存：{srt_path}")
    except Exception as e:
        print(f"保存 SRT 文件失败: {e}")

def process_openai_request(text_func, timeline_func):
    update_status(STATUS_MESSAGES.synthesizing)
    save_path = items["Path"].Text
    if not save_path:
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return False

    base_url = openai_items["OpenAIBaseURL"].Text.strip().rstrip('/') or "https://api.openai.com/v1"
    api_key  = openai_items["OpenAIApiKey"].Text
    
    if not api_key:
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        update_status(STATUS_MESSAGES.synthesis_failed)
        return False

    model       = items["OpenAIModelCombo"].CurrentText
    text        = text_func()
    voice_name  = items["OpenAIVoiceCombo"].CurrentText
    speed       = items["OpenAIRateSpinBox"].Value
    file_format = items["OpenAIFormatCombo"].CurrentText
    filename    = generate_filename(save_path, text, f".{file_format}")

    url = f"{base_url}/audio/speech"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "input": text,
        "voice": voice_name,
        "response_format": file_format,
        "speed": speed
    }
    
    if model not in ["tts-1", "tts-1-hd"]:
        instructions = items["OpenAIInstructionText"].PlainText.strip()
        if instructions:
            payload["instructions"] = instructions
    print(payload)
    try:
        resp = requests.post(url, headers=headers, json=payload)
    except Exception as e:
        print(f"请求 OpenAI 失败：{e}")
        update_status(STATUS_MESSAGES.synthesis_failed)
        return False

    if resp.status_code == 200:
        try:
            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            if os.path.exists(filename):
                start_frame, end_frame = timeline_func()
                add_to_media_pool_and_timeline(start_frame, end_frame, filename)
                update_status(STATUS_MESSAGES.loaded_to_timeline)
                return True
            else:
                update_status(STATUS_MESSAGES.audio_save_failed)
                print("音频文件保存失败")
        except Exception as e:
            print(f"写入文件失败：{e}")
            update_status(STATUS_MESSAGES.synthesis_failed)
    else:
        try:
            error_detail = resp.json().get("error", resp.text)
        except Exception:
            error_detail = resp.text
        print(f"OpenAI 返回错误 (HTTP {resp.status_code})：{error_detail}")
        update_status(STATUS_MESSAGES.synthesis_failed)

    return False

# 针对字幕的处理函数
def on_openai_fromsub_button_clicked(ev):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return False

    process_openai_request(
        text_func=lambda: get_current_subtitle(current_timeline)[0],
        timeline_func=lambda: get_current_subtitle(current_timeline)[1:]
        )

win.On.OpenAIFromSubButton.Clicked = on_openai_fromsub_button_clicked

def on_openai_fromtxt_button_clicked(ev):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return False

    process_openai_request(
        text_func=lambda: items["OpenAIText"].PlainText,
        timeline_func=lambda: (
            # 动态获取当前帧和时间线结束帧
            timecode_to_frames(
                current_timeline.GetCurrentTimecode(),
                float(current_timeline.GetSetting("timelineFrameRate"))
            ),
            current_timeline.GetEndFrame()
        )
    )
 
win.On.OpenAIFromTxtButton.Clicked = on_openai_fromtxt_button_clicked

# 针对字幕的处理函数
def on_minimax_fromsub_button_clicked(ev):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    items["minimaxSubtitleCheckBox"].Checked = False
    process_minimax_request(
        text_func=lambda: get_current_subtitle(current_timeline)[0],
        timeline_func=lambda: get_current_subtitle(current_timeline)[1:]
    )
win.On.minimaxFromSubButton.Clicked = on_minimax_fromsub_button_clicked

# 针对文本框输入的处理函数
def on_minimax_fromtxt_button_clicked(ev):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()
    if not current_timeline:
        show_warning_message(STATUS_MESSAGES.create_timeline)
        return
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    process_minimax_request(
        text_func=lambda: items["minimaxText"].PlainText,
        timeline_func=lambda: (
            # 动态获取当前帧和时间线结束帧
            timecode_to_frames(
                current_timeline.GetCurrentTimecode(),
                float(current_timeline.GetSetting("timelineFrameRate"))
            ),
            current_timeline.GetEndFrame()
        )
    )
win.On.minimaxFromTxtButton.Clicked = on_minimax_fromtxt_button_clicked

def on_break_button_clicked(ev):
    breaktime =  items["BreakSpinBox"].Value
    # 插入<break>标志
    items["AzureTxt"].InsertPlainText(f'<break time="{breaktime}ms" />')

win.On.BreakButton.Clicked = on_break_button_clicked

def on_minimax_break_button_clicked(ev):
    breaktime =  items["minimaxBreakSpinBox"].Value/1000
    # 插入<break>标志
    items["minimaxText"].InsertPlainText(f'<#{breaktime}#>')

win.On.minimaxBreakButton.Clicked = on_minimax_break_button_clicked


def on_alphabet_button_clicked(ev):
    items["AzureTxt"].Copy()
    from pypinyin import pinyin, Style

    def convert_to_pinyin_with_tone(text):
        pinyin_list = pinyin(text, style=Style.TONE3, heteronym=False)
        pinyin_with_tone = []

        for word in pinyin_list:
            if word[0][-1].isdigit():  # 如果最后一个字符是数字（声调）
                pinyin_with_tone.append(f"{word[0][:-1]} {word[0][-1]}")
            else:  # 否则，表示是轻声
                pinyin_with_tone.append(f"{word[0]} 5")
        
        return ' '.join(pinyin_with_tone)

    alphabet = dispatcher.AddWindow(
        {
            "ID": 'Alphabet',
            "WindowTitle": '多音字',
            "Geometry": [750, 400, 500, 150],
            "Spacing": 10,
        },
        [   
            ui.VGroup(
                [
                    ui.HGroup(
                        {"Weight": 1},
                        [
                            ui.LineEdit({"ID": 'AlphaTxt', "Text": ""}),
                        ]
                    ),
                    ui.HGroup(
                        {"Weight": 0},
                        [
                            ui.Label({"ID": 'msgLabel', "Text": """例如，'li 4 zi 5' 表示 '例子'。数字代表拼音声调。'5' 代表轻声。\n若要控制儿化音，请在拼音的声调前插入 "r"。例如，"hou r 2 shan 1" 代表“猴儿山”。"""}),
                        ]
                    ),
                    ui.HGroup(
                        {
                            "Weight": 0,
                        },
                        [
                            ui.Button({"ID": 'OkButton', "Text": 'OK'}),
                        ]
                    ),
                ]
            ),
        ]
    )

    ahb = alphabet.GetItems()
    ahb["AlphaTxt"].Text =  ahb["AlphaTxt"].Paste()
    original_text = ahb["AlphaTxt"].Text
    convert_test= convert_to_pinyin_with_tone(re.sub(r'[^\u4e00-\u9fa5]', '', original_text))
    ahb["AlphaTxt"].Text = convert_test

    def on_ok_button_clicked(ev):
        replace_text = ahb["AlphaTxt"].Text
        replace_text = '' if replace_text == '' else (original_text if replace_text == convert_test else f"<phoneme alphabet=\"sapi\" ph=\"{ahb['AlphaTxt'].Text}\">{original_text}</phoneme>")
        items["AzureTxt"].InsertPlainText(replace_text)
        dispatcher.ExitLoop()
        
    alphabet.On.OkButton.Clicked = on_ok_button_clicked
    def on_close(ev):
        dispatcher.ExitLoop()
    alphabet.On.Alphabet.Close = on_close
    alphabet.Show()
    dispatcher.RunLoop()
    alphabet.Hide()

win.On.AlphabetButton.Clicked = on_alphabet_button_clicked

def on_reset_button_clicked(ev):

    items["LanguageCombo"].CurrentIndex = default_settings["LANGUAGE"]
    items["NameTypeCombo"].CurrentIndex = default_settings["TYPE"]
    items["NameCombo"].CurrentIndex = default_settings["NAME"]
    items["RateSpinBox"].Value = default_settings["RATE"]
    items["BreakSpinBox"].Value = default_settings["BREAKTIME"]
    items["PitchSpinBox"].Value = default_settings["PITCH"]
    items["VolumeSpinBox"].Value = default_settings["VOLUME"]
    items["StyleCombo"].CurrentIndex = default_settings["STYLE"]
    items["StyleDegreeSpinBox"].Value = default_settings["STYLEDEGREE"]
    items["OutputFormatCombo"].CurrentIndex = default_settings["OUTPUT_FORMATS"]

win.On.ResetButton.Clicked = on_reset_button_clicked

def on_minimax_reset_button_clicked(ev):
    """
    重置所有输入控件为默认设置。
    """
    items["minimaxModelCombo"].CurrentIndex = default_settings["minimax_Model"]
    items["minimaxVoiceCombo"].CurrentIndex = default_settings["minimax_Voice"]
    items["minimaxLanguageCombo"].CurrentIndex = default_settings["minimax_Language"]
    items["minimaxEmotionCombo"].CurrentIndex = default_settings["minimax_Emotion"]
    items["minimaxRateSpinBox"].Value = default_settings["minimax_Rate"]
    items["minimaxVolumeSpinBox"].Value = default_settings["minimax_Volume"]
    items["minimaxPitchSpinBox"].Value = default_settings["minimax_Pitch"]
    items["minimaxFormatCombo"].CurrentIndex=default_settings["minimax_Format"]
    items["minimaxBreakSpinBox"].Value = default_settings["minimax_Break"]
    items["minimaxSubtitleCheckBox"].Checked = default_settings["minimax_SubtitleCheckBox"]

# 绑定重置按钮事件
win.On.minimaxResetButton.Clicked = on_minimax_reset_button_clicked

def on_openai_reset_button_clicked(ev):
    """
    重置所有输入控件为默认设置。
    """
    items["OpenAIModelCombo"].CurrentIndex = default_settings["OpenAI_Model"]
    items["OpenAIVoiceCombo"].CurrentIndex = default_settings["OpenAI_Voice"]
    items["OpenAIRateSpinBox"].Value = default_settings["minimax_Rate"]
    items["OpenAIFormatCombo"].CurrentIndex = default_settings["OpenAI_Format"]
    items["OpenAIInstructionText"].Text = default_settings["OpenAI_Instruction"]
    items["OpenAIPresetCombo"].CurrentIndex = default_settings["OpenAI_Preset"]
    
# 绑定重置按钮事件
win.On.OpenAIResetButton.Clicked = on_openai_reset_button_clicked

def on_browse_button_clicked(ev):
    current_path = items["Path"].Text
    selected_path = fusion.RequestDir(current_path)
    if selected_path:
        # 创建以项目名称命名的子目录
        project_subdir = os.path.join(selected_path, f"{current_project.GetName()}_TTS")
        try:
            os.makedirs(project_subdir, exist_ok=True)
            items["Path"].Text = str(project_subdir)
            print(f"Directory created: {project_subdir}")
        except Exception as e:
            print(f"Failed to create directory: {e}")
    else:
        print("No directory selected or the request failed.")

win.On.Browse.Clicked = on_browse_button_clicked

def close_and_save(settings_file):
    settings = {
        "API_KEY": azure_items["ApiKey"].Text,
        "REGION": azure_items["Region"].Text,
        "LANGUAGE": items["LanguageCombo"].CurrentIndex,
        "TYPE": items["NameTypeCombo"].CurrentIndex,
        "NAME": items["NameCombo"].CurrentIndex,
        "RATE": items["RateSpinBox"].Value,
        "PITCH": items["PitchSpinBox"].Value,
        "VOLUME": items["VolumeSpinBox"].Value,
        "STYLEDEGREE": items["StyleDegreeSpinBox"].Value,
        "OUTPUT_FORMATS": items["OutputFormatCombo"].CurrentIndex,
        "UNUSE_API":azure_items["UnuseAPICheckBox"].Checked,

        "minimax_API_KEY": minimax_items["minimaxApiKey"].Text,
        "minimax_GROUP_ID": minimax_items["minimaxGroupID"].Text,
        "minimax_intlCheckBox":minimax_items["intlCheckBox"].Checked,
        "Path": items["Path"].Text,
        "minimax_Model": items["minimaxModelCombo"].CurrentIndex,
        #"Text": items["minimaxText"].PlainText,
        "minimax_Voice": items["minimaxVoiceCombo"].CurrentIndex,
        "minimax_Language": items["minimaxLanguageCombo"].CurrentIndex,
        "minimax_SubtitleCheckBox":items["minimaxSubtitleCheckBox"].Checked,
        "minimax_Emotion": items["minimaxEmotionCombo"].CurrentIndex,
        "minimax_Rate": items["minimaxRateSpinBox"].Value,
        "minimax_Volume": items["minimaxVolumeSpinBox"].Value,
        "minimax_Pitch": items["minimaxPitchSpinBox"].Value,
        "minimax_Format": items["minimaxFormatCombo"].CurrentIndex,
        "minimax_Break":items["minimaxBreakSpinBox"].Value,

        "OpenAI_API_KEY": openai_items["OpenAIApiKey"].Text,
        "OpenAI_BASE_URL": openai_items["OpenAIBaseURL"].Text,
        "OpenAI_Model": items["OpenAIModelCombo"].CurrentIndex,
        "OpenAI_Voice": items["OpenAIVoiceCombo"].CurrentIndex,
        "OpenAI_Rate": items["OpenAIRateSpinBox"].Value,
        "OpenAI_Format": items["OpenAIFormatCombo"].CurrentIndex,
        "OpenAI_Instruction":items["OpenAIInstructionText"].PlainText,
        "OpenAI_Preset":items["OpenAIPresetCombo"].CurrentIndex,

        "CN":items["LangCnCheckBox"].Checked,
        "EN":items["LangEnCheckBox"].Checked,
        
    }

    save_settings(settings, settings_file)


def on_open_link_button_clicked(ev):
    if items["LangEnCheckBox"].Checked :
        webbrowser.open(SCRIPT_KOFI_URL)
    else :
        webbrowser.open(SCRIPT_WX_URL)
win.On.CopyrightButton.Clicked = on_open_link_button_clicked

def on_openai_preview_button_clicked(ev):
    webbrowser.open(OPENAI_FM)
win.On.OpenAIPreviewButton.Clicked = on_openai_preview_button_clicked


def on_minimax_register_link_button_clicked(ev):
    if minimax_items["intlCheckBox"].Checked:
        url= "https://intl.minimaxi.com/login"
    else:
        url = "https://platform.minimaxi.com/registration"
        
    webbrowser.open(url)
minimax_config_window.On.minimaxRegisterButton.Clicked = on_minimax_register_link_button_clicked

def on_azure_register_link_button_clicked(ev):
    url = "https://speech.microsoft.com/portal/voicegallery"
    webbrowser.open(url)
azure_config_window.On.AzureRegisterButton.Clicked = on_azure_register_link_button_clicked

def on_open_guide_button_clicked(ev):
    html_path  = os.path.join(script_path, 'Installation-Usage-Guide.html') 
    if os.path.exists(html_path):
        webbrowser.open(f'file://{html_path}')
    else:
        print("找不到教程文件:", html_path)
win.On.openGuideButton.Clicked = on_open_guide_button_clicked

def on_show_azure(ev):
    azure_config_window.Show()
win.On.ShowAzure.Clicked = on_show_azure

def on_show_minimax(ev):
    minimax_config_window.Show()
win.On.ShowMiniMax.Clicked = on_show_minimax

def on_show_minimax_clone(ev):
    minimax_clone_items["minimaxNeedNoiseReduction"].Enabled = not minimax_clone_items["minimaxOnlyAddID"].Checked
    minimax_clone_items["minimaxNeedVolumeNormalization"].Enabled = not minimax_clone_items["minimaxOnlyAddID"].Checked
    minimax_clone_items["minimaxClonePreviewText"].Enabled = not minimax_clone_items["minimaxOnlyAddID"].Checked
    minimax_clone_window.Show()
win.On.ShowMiniMaxClone.Clicked = on_show_minimax_clone

def on_show_openai(ev):
    openai_config_window.Show()
win.On.ShowOpenAI.Clicked = on_show_openai

# Azure配置窗口按钮事件
def on_azure_close(ev):
    print("Azure API 配置完成")
    azure_config_window.Hide()
azure_config_window.On.AzureConfirm.Clicked = on_azure_close
azure_config_window.On.AzureConfigWin.Close = on_azure_close

# MiniMax配置窗口按钮事件
def on_minimax_close(ev):
    print("MiniMax API 配置完成")
    minimax_config_window.Hide()
minimax_config_window.On.MiniMaxConfirm.Clicked = on_minimax_close
minimax_config_window.On.MiniMaxConfigWin.Close = on_minimax_close

class MinimaxVoiceCloner:
    BASE_URL = "https://api.minimax.chat"
    BASE_URL_INTL = "https://api.minimaxi.chat"
    UPLOAD_PATH = "/v1/files/upload"
    CLONE_PATH = "/v1/voice_clone"
    def __init__(self,
                 api_key: str,
                 group_id: str,
                 voice_file: str,
                 items: Dict[str, Any],
                 intl: bool = False):
        self.api_key = api_key
        self.group_id = group_id
        self.base_url = self.BASE_URL_INTL if intl else self.BASE_URL
        self.voice_file = voice_file
        self.items = items
        self.file_id = None
    def _make_url(self, path: str) -> str:
        return f"{self.base_url}{path}?GroupId={self.group_id}"

    def upload_file(self, file_path: str) -> str:
        """
        上传音频文件，成功时返回 file_id，不弹窗；失败时根据状态码弹出警告并抛异常。
        """
        print("Upload File ...")
        update_status(STATUS_MESSAGES.file_upload)
        url = self._make_url(self.UPLOAD_PATH)
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'purpose': 'voice_clone'}

        # 1. 发起请求并捕获网络或文件打开异常
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                resp = requests.post(url, headers=headers,
                                        data=data, files=files, timeout=300)
                resp.raise_for_status()
                resp_data = resp.json()
        except Exception as e:
            print(f"文件上传请求失败：{e}")
            # 通用错误提示
            show_warning_message(STATUS_MESSAGES.error_1000)
            raise

        # 2. 解析业务状态码
        base_resp = resp_data.get("base_resp", {})
        code = str(base_resp.get("status_code", ""))

        # 3. 只有业务失败时才弹窗并抛异常
        if code != "0" or "file" not in resp_data:
            attr = f"error_{code}"
            status_tuple = getattr(
                STATUS_MESSAGES,
                attr,
                STATUS_MESSAGES.error_1000
            )
            show_warning_message(status_tuple)
            update_status(status_tuple)
            raise RuntimeError(f"文件上传失败: {resp_data}")

        # 4. 成功时直接返回 file_id，不弹窗
        self.file_id = resp_data["file"]["file_id"]
        print(f"上传成功，file_id={self.file_id}")
        return self.file_id


    def submit_clone(self,
                 voice_id: str,
                 need_noise_reduction: bool,
                 need_volume_normalization: bool,
                 text: str) -> dict:
        update_status(STATUS_MESSAGES.file_clone)
        print("Clone File ...")
        url = self._make_url(self.CLONE_PATH)
        payload = {
            "file_id": self.file_id,
            "voice_id": voice_id,
            "need_noise_reduction": need_noise_reduction,
            "need_volume_normalization": need_volume_normalization
        }
        if text.strip():
            payload["text"] = text
            payload["model"] = "speech-02-hd"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        resp_data = resp.json()
        base_resp = resp_data.get("base_resp", {})
        code = str(base_resp.get("status_code", ""))
        # 仅当 code 非 "0" 时才弹警告
        if code != "0":
            attr = f"error_{code}"
            status_tuple = getattr(
                STATUS_MESSAGES,
                attr,
                STATUS_MESSAGES.error_1000
            )
            show_warning_message(status_tuple)
            update_status(status_tuple)
            raise RuntimeError(f"合成失败，状态码 {resp_data}")

        # 成功时不弹窗，直接返回
        return resp_data


    def download_demo(self,
                      data: dict,
                      save_dir: str,
                      voice_id: str) -> Optional[str]:
        print("Download Preview Audio ...")
        update_status(STATUS_MESSAGES.download_preclone)
        demo_url = data.get("demo_audio")
        if not demo_url:
            return None
        os.makedirs(save_dir, exist_ok=True)
        local_path = os.path.join(save_dir, f"preview_{voice_id}.mp3")
        resp = requests.get(demo_url, stream=True, timeout=30)
        resp.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in resp.iter_content(8192):
                f.write(chunk)
        return local_path

    
def load_clone_data(voice_file: str) -> Dict[str, Any]:
    """
    读取 JSON 文件，返回包含 key 'minimax_clone_voices' 的字典
    若文件不存在或解析失败，则返回空 dict 并初始化该 key
    """
    try:
        with open(voice_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (IOError, json.JSONDecodeError):
        data = {}
    data.setdefault("minimax_clone_voices", [])
    return data

def save_clone_data(voice_file: str, data: Dict[str, Any]) -> None:
    """
    将 data 写回 voice_file，格式化输出
    """
    try:
        with open(voice_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError:
        raise Exception(f"Cannot write to file: {voice_file}")

def refresh_voice_combo(
    items: Dict[str, Any],
    clone_list: List[Dict[str, Any]],
    system_list: List[Dict[str, Any]],
) -> None:
    """
    刷新下拉框：只添加 language 与当前语言一致的条目
    """
    combo = items["minimaxVoiceCombo"]
    combo.Clear()  # 清空所有选项 _README_WORKFLOW_20.txt](file-service://file-27aT4jFAer9mu7jVoLKdot)

    current_lang = items["minimaxLanguageCombo"].CurrentText.strip()
    # 先添加符合当前语言的克隆列表
    for v in clone_list:
        if v.get("language", "").strip() == current_lang:
            combo.AddItem(v["voice_name"])
    # 再添加符合当前语言的系统列表
    for v in system_list:
        if v.get("language", "").strip() == current_lang:
            combo.AddItem(v["voice_name"])

def add_clone_voice(
    voice_file: str,
    voice_name: str,
    voice_id: str,
    items: Dict[str, Any],
    minimax_clone_voices: List[Dict[str, str]],
    minimax_voices: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    # 1. 加载现有数据
    data = load_clone_data(voice_file)

    # 2. 重复检查
    for v in data["minimax_clone_voices"]:
        if v.get("voice_name") == voice_name or v.get("voice_id") == voice_id:
            show_warning_message(STATUS_MESSAGES.error_2039)
            return minimax_clone_voices

    # 3. 插入新条目到列表开头
    new_voice = {
        "voice_id": voice_id,
        "voice_name": voice_name,
        "description": [],
        "created_time": "1970-01-01",
        "language": items["minimaxLanguageCombo"].CurrentText
    }
    data["minimax_clone_voices"].insert(0, new_voice)

    # 4. 保存并刷新 UI
    save_clone_data(voice_file, data)
    refresh_voice_combo(items, data["minimax_clone_voices"], minimax_voices)

    show_warning_message(STATUS_MESSAGES.add_clone_succeed)
    return data["minimax_clone_voices"]

def delete_clone_voice(
    voice_file: str,
    voice_name: str,
    items: Dict[str, Any],
    minimax_clone_voices: List[Dict[str, str]],
    minimax_voices: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    # 1. 加载现有数据
    data = load_clone_data(voice_file)
    original = data["minimax_clone_voices"]

    # 2. 过滤出所有不匹配的条目（strip + lower 匹配）
    key = voice_name.strip().lower()
    filtered = [
        v for v in original
        if v.get("voice_name", "").strip().lower() != key
    ]

    # 3. 如果没有任何条目被删除，提示并返回旧列表
    if len(filtered) == len(original):
        show_warning_message(STATUS_MESSAGES.delete_clone_error)
        return minimax_clone_voices

    # 4. 保存并刷新 UI
    data["minimax_clone_voices"] = filtered
    save_clone_data(voice_file, data)
    refresh_voice_combo(items, filtered, minimax_voices)

    show_warning_message(STATUS_MESSAGES.delete_clone_succeed)
    return filtered

def on_delete_minimax_clone_voice(ev):
    global minimax_clone_voices  # 声明我们要更新的全局变量
    voice_name = items["minimaxVoiceCombo"].CurrentText.strip()
    minimax_clone_voices = delete_clone_voice(
            voice_file=voice_file,
            voice_name=voice_name,
            items=items,
            minimax_clone_voices=minimax_clone_voices,
            minimax_voices=minimax_voices,
            
        )
win.On.minimaxDeleteVoice.Clicked = on_delete_minimax_clone_voice

def on_minimax_clone_confirm(ev):
    # 1. 参数检查
    if not (minimax_items["minimaxGroupID"].Text and minimax_items["minimaxApiKey"].Text):
        show_warning_message(STATUS_MESSAGES.enter_api_key)
        return
    if items["Path"].Text == '':
        show_warning_message(STATUS_MESSAGES.select_save_path)
        return
    global minimax_clone_voices  # 声明我们要更新的全局变量
    # 2. 读取通用参数
    group_id = minimax_items["minimaxGroupID"].Text
    api_key  = minimax_items["minimaxApiKey"].Text
    intl     = minimax_items["intlCheckBox"].Checked
    voice_name = minimax_clone_items["minimaxCloneVoiceName"].Text.strip()
    voice_id   = minimax_clone_items["minimaxCloneVoiceID"].Text.strip()
    need_nr    = minimax_clone_items["minimaxNeedNoiseReduction"].Checked
    need_vn    = minimax_clone_items["minimaxNeedVolumeNormalization"].Checked
    preview_text = minimax_clone_items["minimaxClonePreviewText"].PlainText.strip()
    
    if not voice_name or not voice_id:
        show_warning_message(STATUS_MESSAGES.clone_id_error)
        return
    # 3. 初始化或复用封装好的类
    cloner = MinimaxVoiceCloner(api_key, group_id,
                                voice_file,
                                items, intl)

    # 4. 只添加 ID
    if minimax_clone_items["minimaxOnlyAddID"].Checked:
        minimax_clone_voices = add_clone_voice(
            voice_file=voice_file,
            voice_name=voice_name,
            voice_id=voice_id,
            items=items,
            minimax_clone_voices=minimax_clone_voices,
            minimax_voices=minimax_voices,
            
        )
        return

    # 5. 先 ensure file_id
    if minimax_clone_items["minimaxCloneFileID"].Text == "":
        file_path = render_audio_by_marker(items["Path"].Text)
        if file_path is None:
            return
        print(f"file_path:{file_path}")
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            if file_size > 20 * 1024 * 1024:
                show_warning_message(STATUS_MESSAGES.file_size)
                return
        
        cloner.upload_file(file_path)
        print(f"file_id:{cloner.file_id}")
        minimax_clone_items["minimaxCloneFileID"].Text = str(cloner.file_id)
    else:
        cloner.file_id = int(minimax_clone_items["minimaxCloneFileID"].Text)

    # 6. 提交克隆并下载 demo
   
    resp = cloner.submit_clone(voice_id, need_nr, need_vn, preview_text)
    print(f"response:{resp}")

    # 7. 如果成功，再把声音写入列表
    if resp.get("base_resp", {}).get("status_code") == 0:
        save_dir = items["Path"].Text
        demo_path = cloner.download_demo(resp, save_dir, voice_id)
        add_to_media_pool_and_timeline(
            current_timeline.GetStartFrame(),
            current_timeline.GetEndFrame(),
            demo_path
        )   
        minimax_clone_voices = add_clone_voice(
            voice_file=voice_file,
            voice_name=voice_name,
            voice_id=voice_id,
            items=items,
            minimax_clone_voices=minimax_clone_voices,
            minimax_voices=minimax_voices,
            
        )
        show_warning_message(STATUS_MESSAGES.clone_success)
    else:
        msg = resp.get("base_resp", {}).get("status_msg")
        minimax_clone_items["minimaxCloneStatus"].Text = f"ERROR:{msg}"


minimax_clone_window.On.MiniMaxCloneConfirm.Clicked = on_minimax_clone_confirm

def on_minimax_clone_close(ev):
    minimax_clone_items["minimaxCloneFileID"].Text = ""
    minimax_clone_window.Hide()
minimax_clone_window.On.MiniMaxCloneWin.Close = on_minimax_clone_close
minimax_clone_window.On.MiniMaxCloneCancel.Clicked = on_minimax_clone_close

# OpenAI配置窗口按钮事件
def on_openai_close(ev):
    print("OpenAI API 配置完成")
    openai_config_window.Hide()
openai_config_window.On.OpenAIConfirm.Clicked = on_openai_close
openai_config_window.On.OpenAIConfigWin.Close = on_openai_close

def on_aitranslator_button(ev):
    if items["LangEnCheckBox"].Checked :
        webbrowser.open(AIRANSLATOR_KOFI_URL)
    else :
        webbrowser.open(AIRANSLATOR_TAOBAO_URL)
win.On.TTSButton.Clicked = on_aitranslator_button

def on_close(ev):
    close_and_save(settings_file)
    dispatcher.ExitLoop()
win.On.MainWin.Close = on_close



win.Show()
dispatcher.RunLoop()
azure_config_window.Hide()
minimax_config_window.Hide()
openai_config_window.Hide()
win.Hide()
