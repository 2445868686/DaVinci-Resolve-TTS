SCRIPT_NAME = "DaVinci TTS Free"
SCRIPT_VERSION = " 3.3"
SCRIPT_AUTHOR = "HEIBA"
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
X_CENTER = (SCREEN_WIDTH - WINDOW_WIDTH) // 2
Y_CENTER = (SCREEN_HEIGHT - WINDOW_HEIGHT) // 2
SCRIPT_INFO_CN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #ffffff;
            padding: 20px;
        }
        h3 {
            font-weight: bold;
            font-size: 1.5em;
            margin-top: 15px;
            margin-bottom: 0px; /* 调整此处以减少间隔 */
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* 黄色 */
        }
        p {
            font-size: 1.2em;
            margin-top: 5px;
            margin-bottom: 20px; /* 调整此处以减少间隔 */
            color: #a3a3a3; /* 白色 */
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
<h3>更新[3.2] 2025-04-30</h3>
    <li>-MiniMax语音</li>
    <ul>
            <li>新增270+系统音色！</li> 
        </ul>   
    <h3>更新[3.1] 2025-04-20</h3>
    <li>-MiniMax语音</li>
    <ul>
            <li>新增从达芬奇获取音频克隆音色！</li> 
        </ul>   
    <h3>更新[3.0] 2025-04-05</h3>
        <li>-MiniMax语音</li>
        <ul>
            <li>新增speech-02-hd，全新的HD模型，拥有更出色的韵律和稳定性，复刻相似度和音质表现突出！</li> 
            <li>新增speech-02-turbo，全新的Turbo模型，拥有更出色的韵律和稳定性，小语种能力加强，性能表现出色！</li> 
            <li>可添加自定义克隆音色（前往<a href="https://www.minimaxi.com/">MINIMAX</a>获取你的克隆ID）！</li> 
        </ul>   
    <h3>更新[2.9] 2025-03-23</h3>
        <li>-新增OpenAI TTS语音模型</li>

    <h3>更新[2.8] 2025-03-16</h3>
    
        <li>-微软语音</li>
        <ul>
            <li>新增13种HD高清语音</li> 
        </ul>
        <li>-MiniMax语音</li>
        <ul>
            <li>新增语种选项，增强对指定的小语种和方言的识别能力！</li> 
            <li>新增字幕功能，生成音频文件对应的时间戳字幕！</li> 
        </ul>
        
    <h3>更新[2.7] 2025-01-18</h3>
    
        <li>-新增MiniMax 语音模型！</li>
        <ul>
            <li>支持100+系统音色自主选择；</li> 
            <li>支持音量、语调、语速、输出格式调整；</li>    
            <li>支持固定间隔时间控制；</li>   
            <li>支持预览音色；</li>  
        </ul>
        
    <h3>更新[2.6] 2025-01-16</h3>
    
        <li>-修复Window系统保存文件出错问题！</li>

    <h3>更新[2.5] 2024-10-21</h3>
    
        <li>-新增最新的HD高清语音模型！</li>
        <li>-修复使用丢帧时间码无法加载音频问题！</li>
    <h3>更新[2.4] 2024-09-21</h3>
        <li>-修复键盘上下键调整参数卡死问题！</li>
        
    <h3>新增功能 2024-08-13</h3>
    
        <li>-无需API KEY，免费使用超过300+种语音和100+种语言！</li>
        <li>-修复语音名称显示问题</li>
        <li>-新增功能：</li>
        <ul>
            <li>加载音频到时间线：合成音频后自动加载到时间线。</li> 
            <li>朗读当前字幕：合成并加载播放头位置的字幕块。</li>    

        </ul>

    <h3>新增功能 2024-07-10</h3>
    
        <li>-全新UI设计，更大的字幕输入框以及字体</li>
        <li>-新增自定义功能：</li>
        <ul>
            <li>发音：更改文字的发音！</li>
            <li>文稿矫正：使用输入框的文本对生成的字幕一键修正！</li>       
        </ul>

    <h3>新增功能 2024-07-01</h3>
    
        <li>-启用API：需要填入Azure API，能够体验到软件的完整功能！</li>
        <li>-停用API：不需要填入Azure API，但某些功能将被暂停使用！</li>
        <li>-新增更多自定义功能：</li>
        <ul>
            <li>停顿：插入朗读停顿。</li>
            <li>语速：调整说话语速。</li>
            <li>音高：调整声音的高低。</li>
            <li>音量：调整音量的大小。</li>  
            <li>语言技能：使用Multilingual人物时，可切换为其他语言。</li>             
        </ul>


    <h3>介绍</h3>
    <p>此脚本使用Azure的TTS功能将文字转换为语音。</p>

    <h3>保存路径</h3>
    <p>指定生成文件的保存路径。</p>

    <h3>区域、API密钥</h3>
    <p>从<a href="https://speech.microsoft.com/">Microsoft Speech Studio</a>获取您的API密钥。</p>
</body>
</html>

"""
SCRIPT_INFO_EN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #ffffff;
            padding: 20px;
        }
        h3 {
            font-weight: bold;
            font-size: 1.5em;
            margin-top: 15px;
            margin-bottom: 0px; /* Adjust spacing */
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* Yellow */
        }
        p {
            font-size: 1.2em;
            margin-top: 5px;
            margin-bottom: 20px; /* Adjust spacing */
            color: #a3a3a3; /* White */
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
<h3>Update [3.2] 2025-04-30</h3> 
<li>-Minimax TTS</li> 
    <ul> 
       <li>Added 270+ system voices!</li>
    </ul>
<h3>Update [3.1] 2025-04-20</h3> 
<li>-Minimax TTS</li> 
    <ul> 
       <li>Add a feature to pull audio from DaVinci so we can clone the voice’s timbre!</li>
    </ul>
<h3>Update [3.0] 2025-04-05</h3> 
<li>-Minimax TTS</li> 
    <ul> 
        <li>New speech-02-hd: The brand new HD model boasts superior rhythm and stability, with outstanding performance in replication similarity and sound quality!</li> 
        <li>New speech-02-turbo: The brand new Turbo model boasts superior rhythm and stability, with enhanced multilingual capabilities and excellent performance!</li>
        <li>You can add a custom cloned voice (go to <a href="https://www.minimaxi.com/">MINIMAX</a> to get your clone ID)!</li>
    </ul>
<h3>Update [2.9] 2025-03-23</h3>
     <li>-Added OpenAI TTS voice model</li>
    <h3>Update [2.8] 2025-03-16</h3>
        <li>-Microsoft TTS</li>
        <ul>
            <li>Added 13 new HD voices.</li>
        </ul>
        <li>-Minimax TTS</li>
        <ul>
            <li>Introduced new language options, improving recognition of specific lesser-known languages and dialects.</li>
            <li>Added a subtitle generation feature, allowing the creation of subtitles with timestamps for audio files.</li>
        </ul>
    <h3>Update [2.7 beta] 2025-01-18</h3>
    
        <li>- Added MiniMax voice model!</li>
        <ul>
            <li>Supports 100+ system voice options;</li> 
            <li>Supports volume, pitch, speech rate, and output format adjustments;</li>    
            <li>Supports fixed interval time control;</li>   
            <li>Supports voice preview;</li>  
        </ul>
        
    <h3>Update [2.6] 2025-01-16</h3>
    
        <li>- Fixed file saving issue on Windows systems!</li>

    <h3>Update [2.5] 2024-10-21</h3>
    
        <li>- Added the latest HD high-definition voice model!</li>
        <li>- Fixed an issue where audio could not be loaded when using dropped frame timecodes!</li>
    
    <h3>Update [2.4] 2024-09-21</h3>
        <li>- Fixed an issue where adjusting parameters with the keyboard up and down keys would freeze!</li>
        
    <h3>New Features 2024-08-13</h3>
    
        <li>- No API KEY required, free access to over 300+ voices and 100+ languages!</li>
        <li>- Fixed an issue with voice name display.</li>
        <li>- New Features:</li>
        <ul>
            <li>Load audio to the timeline: Automatically load synthesized audio into the timeline.</li> 
            <li>Read current subtitle: Synthesize and load the subtitle block at the playhead position.</li>    
        </ul>

    <h3>New Features 2024-07-10</h3>
    
        <li>- Brand new UI design with a larger subtitle input box and font size.</li>
        <li>- Added customization features:</li>
        <ul>
            <li>Pronunciation: Modify the pronunciation of text!</li>
            <li>Transcript correction: Use text from the input box to correct generated subtitles with one click!</li>       
        </ul>

    <h3>New Features 2024-07-01</h3>
    
        <li>- Enable API: Requires Azure API key to experience the full functionality of the software.</li>
        <li>- Disable API: No need for an Azure API key, but some features will be temporarily unavailable.</li>
        <li>- Added more customization features:</li>
        <ul>
            <li>Pause: Insert reading pauses.</li>
            <li>Speech rate: Adjust the speaking speed.</li>
            <li>Pitch: Adjust the pitch of the voice.</li>
            <li>Volume: Adjust the volume level.</li>  
            <li>Language Skills: When using Multilingual voices, switch to other languages.</li>             
        </ul>

    <h3>Introduction</h3>
    <p>This script uses Azure's TTS feature to convert text to speech.</p>

    <h3>Save Path</h3>
    <p>Specifies the save path for the generated files.</p>

    <h3>Region, API Key</h3>
    <p>Obtain your API key from <a href="https://speech.microsoft.com/">Microsoft Speech Studio</a>.</p>
</body>
</html>
"""
SCRIPT_CLONE_INFO_CN = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #ffffff;
            padding: 20px;
        }
        h3 {
            font-weight: bold;
            font-size: 1.5em;
            margin-top: 15px;
            margin-bottom: 0px; /* Adjust spacing */
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* Yellow */
        }
        h4 {
            font-weight: bold;
            font-size: 1em;
            margin-top: 15px;
            margin-bottom: 0px; /* Adjust spacing */
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* Yellow */
        }
        p {
            font-size: 1.2em;
            margin-top: 5px;
            margin-bottom: 20px; /* Adjust spacing */
            color: #a3a3a3; /* White */
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
  <!-- 标题居中 -->
  <h3 style="text-align: center;">MiniMax 克隆说明</h3>

  <h4>☑ 已有克隆音色</h4>
  <ul>
    <li>
        如果已经从MiniMax官方克隆了音色，直接填入
        <strong>音色ID</strong> 和 <strong>音色名称</strong>，点击<strong>添加</strong>后，
        音色列表中即可看到您的克隆音色！
    </li>
</ul>
  <h4>☐ 已有克隆音色<br>（从达芬奇导出音频进行克隆）</h4>
  <li>
  <ul>
    <li><strong>步骤一：</strong>确保时间线上已有要克隆的音频。</li>
    <li>
      <strong>步骤二：</strong>按 <strong>M 键</strong> 添加标记点，
      按住 <strong>Alt 键</strong> 拖拽选取音频区间（<strong>10 秒–5 分钟</strong>）。
    </li>
    <li>
      <strong>步骤三：</strong>在交付界面取消勾选<strong>导出视频</strong>，
      将音频格式设置为 <strong>MP3</strong> 或 <strong>WAV</strong>。
    </li>
    <li>
      <strong>步骤四：</strong>填写 <strong>音色名称</strong> 和 <strong>音色ID</strong>，
      根据需要勾选 <strong>降噪</strong> 和 <strong>音频统一</strong> 选项。
    </li>
    <li>
      <strong>步骤五：</strong>输入 <strong>试听文本</strong>，
      克隆完成后试听音频会自动加载到时间线进行预览。
    </li>
    <li>
      <strong>步骤六：</strong>点击<strong>克隆</strong>，克隆完成后
      <strong>克隆ID</strong> 将出现在音色列表中。
    </li>
  </li>
</ul>
  <h4>费用说明</h4>
  <li>
    <ul>
    <li>确保 minimax 账户余额充足，<strong>9.9 元/音色</strong>。</li>
    <li>克隆音色时不会立即扣费，费用将在<strong>首次使用该音色合成语音</strong>时收取。</li>
  </ul>
  </li>
</body>
</html>

"""
SCRIPT_CLONE_INFO_EN="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #ffffff;
            padding: 20px;
        }
        h3 {
            font-weight: bold;
            font-size: 1.5em;
            margin-top: 15px;
            margin-bottom: 0px;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* Yellow */
        }
        h4 {
            font-weight: bold;
            font-size: 1em;
            margin-top: 15px;
            margin-bottom: 0px;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 5px;
            color: #c7a364; /* Yellow */
        }
        p {
            font-size: 1.2em;
            margin-top: 5px;
            margin-bottom: 20px;
            color: #a3a3a3; /* White */
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        ul {
            margin-top: 5px;
            margin-bottom: 20px;
            padding-left: 20px;
            color: #a3a3a3;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <!-- 标题居中 -->
    <h3 style="text-align: center;">MiniMax Clone Instructions</h3>

    <h4>☑ Existing Cloned Voice</h4>
    <ul>
        <li>
            If you have already cloned a voice from the official MiniMax, simply enter the <strong>Voice ID</strong> and <strong>Voice Name</strong>, then click <strong>Add</strong>. You will see your cloned voice in the voice list!
        </li>
    </ul>

    <h4>☐ Clone from DaVinci Exported Audio</h4>
    <ul>
        <li><strong>Step 1:</strong> Ensure the timeline contains the audio you want to clone.</li>
        <li>
            <strong>Step 2:</strong> Press <strong>M</strong> to add a marker, then hold <strong>Alt</strong> and drag to select the audio segment 
            (<strong>10 seconds–5 minutes</strong>).
        </li>
        <li>
            <strong>Step 3:</strong> In the delivery panel, uncheck <strong>Export Video</strong>, and set the audio format to 
            <strong>MP3</strong> or <strong>WAV</strong>.
        </li>
        <li>
            <strong>Step 4:</strong> Enter the <strong>Voice Name</strong> and <strong>Voice ID</strong>, and select the 
            <strong>Noise Reduction</strong> and <strong>Audio Normalization</strong> options as needed.
        </li>
        <li>
            <strong>Step 5:</strong> Enter the <strong>Preview Text</strong>. Once cloning is complete, the preview audio will automatically load into the timeline for playback.
        </li>
        <li>
            <strong>Step 6:</strong> Click <strong>Clone</strong>. After completion, the <strong>Clone ID</strong> will appear in the voice list.
        </li>
    </ul>

    <h4>Cost Explanation</h4>
    <ul>
        <li>Ensure your MiniMax account has sufficient balance; <strong>$3 per voice</strong>.</li>
        <li>
            Cloning a voice will not charge immediately; the fee is applied upon the <strong>first use</strong> of the voice for synthesis.
        </li>
    </ul>
</body>
</html>

"""

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

class STATUS_MESSAGES:
    synthesis_failed    = ("Synthesis failed!", "合成失败！")
    loaded_to_timeline  = ("Successfully loaded to timeline!", "成功加载到时间线！")
    synthesizing        = ("Synthesizing...", "合成中...")
    media_clip_exists   = ("The media pool already contains this clip.", "媒体池已存在该片段")
    playing             = ("Playing...", "播放中...")
    audio_save_failed   = ("Failed to save audio file.", "音频文件保存失败")
    # 新增状态信息
    enter_api_key       = ("Enter API key in the configuration panel.", "前往配置栏填写API密钥.")
    download_json       = ("Move minimax_voice_data.json to the plugin directory.", "请下载minimax_voice_data.json文件到插件目录")
    download_pcm        = ("Move minimax_voice_data.pcm to the plugin directory.", "请下载minimax_voice_data.pcm文件到插件目录")
    select_save_path    = ("Select a save path in the configuration panel.", "前往配置栏选择保存路径.")
    unsupported_audio   = ("Unsupported audio format selected.", "不支持的音频格式.")
    create_timeline     = ("Please create a timeline first!", "请先创建时间线！")
    reset_status        = ("", "")
    become_a_sponsor    = ("Unlock all features by becoming a sponsor!", "购买完整版解锁全部功能！")

def check_or_create_file(file_path):
    if os.path.exists(file_path):
        pass
    else:
        try:
            with open(file_path, 'w') as file:
                json.dump({}, file)  
        except IOError:
            raise Exception(f"Cannot create file: {file_path}")

def get_script_path():
    if len(sys.argv) > 0:
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    else:
        return os.getcwd()

config_dir = os.path.join(script_path, 'config')
settings_file = os.path.join(config_dir, 'TTS_settings.json')

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
    
    "CN":True,
    "EN":False,


}

current_manager = resolve.GetProjectManager()
current_project = current_manager.GetCurrentProject()
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

ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)
screen_width = 1920
screen_height = 1080
window_width = 850
window_height = 400
x_center = (screen_width - window_width) // 2
y_center = (screen_height - window_height) // 2
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
                        ui.HGroup({"Weight": 0.1}, [
                            ui.CheckBox({"ID": "LangEnCheckBox", "Text": "EN", "Checked": True, "Alignment": {"AlignRight": True}, "Weight": 0}),
                            ui.CheckBox({"ID": "LangCnCheckBox", "Text": "简体中文", "Checked": False, "Alignment": {"AlignRight": True}, "Weight": 1}),
                            ui.Button({"ID": "openGuideButton", "Text": "教程","Weight": 0.1}),
                        ]),
                        ui.Button({
                            "ID": "OpenLinkButton", 
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
                            ui.TextEdit({"ID": "minimaxcloneinfoTxt", "Text": SCRIPT_CLONE_INFO_CN, "ReadOnly": True, "Font": ui.Font({"PixelSize": 14})})
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
        "OpenLinkButton":f"关注公众号：游艺所\n\n>>>点击查看更多信息<<<\n\n© 2025, Copyright by {SCRIPT_AUTHOR}.",
        "infoTxt":SCRIPT_INFO_CN,
        "AzureLabel":"填写Azure API信息",
        "RegionLabel":"区域",
        "ApiKeyLabel":"密钥",
        "UnuseAPICheckBox":"停用 API",
        "minimaxSubtitleCheckBox":"生成srt字幕",
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
        "minimaxcloneinfoTxt":SCRIPT_CLONE_INFO_CN,
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
        "OpenLinkButton":f"😊Buy Me A Coffe😊\n\n© 2025, Copyright by {SCRIPT_AUTHOR}.",
        "infoTxt":SCRIPT_INFO_EN,
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
        #"minimaxCloneGuide":"$3 per voice. \n\nYou won’t be charged for cloning a voice right away \n\n the cloning fee will only be charged the first time you use that cloned voice for speech synthesis.",
        "minimaxCloneVoiceIDLabel":"Voice ID",
        "minimaxCloneFileIDLabel":"File ID",
        "minimaxOnlyAddID":"I already have a clone voice.(just fill in below).",
        "minimaxNeedNoiseReduction":"Noise Reduction",
        "minimaxNeedVolumeNormalization":"Volume Normalization",
        "minimaxClonePreviewLabel":"Input text for cloned voice preview:\n(Limited to 2000 characters. )",
        "minimaxApiKeyLabel":"Key",
        "minimaxcloneinfoTxt":SCRIPT_CLONE_INFO_EN,
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

# 加载Voice
voice_file = os.path.join(config_dir, 'voices_list.json')
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

minimax_voice_index_initialized = False
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

win.On["minimaxModelCombo"].CurrentIndexChanged = on_minimax_model_combo_changed

def on_openai_model_combo_changed(event):
    selected_model = items["OpenAIModelCombo"].CurrentText
    if selected_model not in ["tts-1", "tts-1-hd"]:
        items["OpenAIInstructionText"].PlaceholderText = ""
        items["OpenAIInstructionText"].Enabled = True  
    else:
        items["OpenAIInstructionText"].PlaceholderText = "Does not work with tts-1 or tts-1-hd."
        items["OpenAIInstructionText"].Enabled = False  

win.On["OpenAIModelCombo"].CurrentIndexChanged = on_openai_model_combo_changed
# 在启动时检查模型状态
on_minimax_model_combo_changed({"Index": items["minimaxModelCombo"].CurrentIndex})
on_openai_model_combo_changed({"Index": items["OpenAIModelCombo"].CurrentIndex})


# 汉化映射字典
StyleMapping = {
    
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
           ],
        "languages": {
            }
    },
    "Multilingual2": {
        "names": [
           ],
        "languages": {
            }
    },
    "Multilingual3": {
        "names": [],
        "languages": {
           }
    }
}

lang_translation = {
    
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
    items["minimaxVoiceCombo"].CurrentIndex= saved_settings.get("minimax_Voice", default_settings["minimax_Voice"])
    items["minimaxLanguageCombo"].CurrentIndex= saved_settings.get("minimax_Language", default_settings["minimax_Language"])
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
    
win.On.FromTxtButton.Clicked = on_fromtxt_button_clicked

def on_play_button_clicked(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.PlayButton.Clicked = on_play_button_clicked

def on_minimax_preview_button_click(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.minimaxPreviewButton.Clicked = on_minimax_preview_button_click

# 针对字幕的处理函数
def on_openai_fromsub_button_clicked(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
   
win.On.OpenAIFromSubButton.Clicked = on_openai_fromsub_button_clicked

def on_openai_fromtxt_button_clicked(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
 
win.On.OpenAIFromTxtButton.Clicked = on_openai_fromtxt_button_clicked

# 针对字幕的处理函数
def on_minimax_fromsub_button_clicked(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.minimaxFromSubButton.Clicked = on_minimax_fromsub_button_clicked

# 针对文本框输入的处理函数
def on_minimax_fromtxt_button_clicked(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
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

def sponsor(status_tuple):
    use_english = items["LangEnCheckBox"].Checked
    # 元组索引 0 为英文，1 为中文
    message = status_tuple[0] if use_english else status_tuple[1]
    if use_english :
        test =  "Become a Sponsor"
        url =  "https://ko-fi.com/s/9e769243b5"
    else:
        test =  "购买完整版"
        url =  "https://item.taobao.com/item.htm?abbucket=19&id=808582811947&ns=1&priceTId=2100c88917427376539382786e0bb3&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22f314a2f9d6cc2c50562b8cedfa27584d%22%7D&xxc=taobaoSearch"

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
                            ui.Button({"ID": 'OkButton', "Text": test}),
                        ]
                    ),
                ]
            ),
        ]
    )

    def on_ok_button_clicked(ev):
        webbrowser.open(url)
        dispatcher.ExitLoop()
    msgbox.On.OkButton.Clicked = on_ok_button_clicked
    def on_close(ev):
        dispatcher.ExitLoop()
    msgbox.On.msg.Close = on_close

    msgbox.Show()
    dispatcher.RunLoop()
    msgbox.Hide()

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

        "CN":items["LangCnCheckBox"].Checked,
        "EN":items["LangEnCheckBox"].Checked,
        
    }

    save_settings(settings, settings_file)


def on_open_link_button_clicked(ev):
    if items["LangEnCheckBox"].Checked :
        webbrowser.open("https://ko-fi.com/heiba")
    else :
        webbrowser.open("https://mp.weixin.qq.com/s?__biz=MzUzMTk2MDU5Nw==&mid=2247484626&idx=1&sn=e5eef7e48fbfbf37f208ed9a26c5475a&chksm=fabbc2a8cdcc4bbefcb7f6c72a3754335c25ec9c3e408553ec81c009531732e82cbab923276c#rd")
win.On.OpenLinkButton.Clicked = on_open_link_button_clicked

def on_azure_register_link_button_clicked(ev):
    url = "https://speech.microsoft.com/portal/voicegallery"
    webbrowser.open(url)
azure_config_window.On.AzureRegisterButton.Clicked = on_azure_register_link_button_clicked

def on_show_azure(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.ShowAzure.Clicked = on_show_azure

def on_show_minimax(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.ShowMiniMax.Clicked = on_show_minimax

def on_show_minimax_clone(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.ShowMiniMaxClone.Clicked = on_show_minimax_clone

def on_delete_minimax_clone_voice(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.minimaxDeleteVoice.Clicked = on_delete_minimax_clone_voice

def on_openai_preview_button_clicked(ev):
    webbrowser.open("https://openai.fm")
win.On.OpenAIPreviewButton.Clicked = on_openai_preview_button_clicked

def on_open_guide_button_clicked(ev):

    html_path  = os.path.join(script_path, 'Installation-Usage-Guide.html') 
    if os.path.exists(html_path):
        webbrowser.open(f'file://{html_path}')
    else:
        print("找不到教程文件:", html_path)
win.On.openGuideButton.Clicked = on_open_guide_button_clicked

def on_show_openai(ev):
    sponsor(STATUS_MESSAGES.become_a_sponsor)
win.On.ShowOpenAI.Clicked = on_show_openai


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
