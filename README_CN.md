<div align="center">
    
# <span style="color: #2ecc71;">DaVinci Resolve TTS 插件 🎤✨</span>

**[English](README.md) | [简体中文](README_CN.md)**
</div>

## 项目介绍 🚀

本项目基于 DaVinci Resolve 的脚本接口和 Fusion UI 构建了一个图形界面插件，实现了在DaVinci Resolve软件中文本转语音（TTS）功能。插件支持微软 [Azure's TTS](https://speech.microsoft.com/) 与 [MiniMax TTS](https://intl.minimaxi.com/) 两种语音合成服务，并提供多种参数配置（如语速、音调、音量、风格、停顿等）以及从时间线/文本框获取字幕后直接生成语音并加载到时间线的完整流程。

![TTS](https://github.com/user-attachments/assets/0626ed7e-40c9-4b8f-92ee-736ca6756619)

## 项目特点🎉

- **多服务支持**
    - 集成微软 [Azure's TTS](https://speech.microsoft.com/) 与 [MiniMax TTS](https://intl.minimaxi.com/) 服务，可根据需求自由切换。
    - 可选择无需 API 模式，插件调用 [Edge TTS](https://github.com/rany2/edge-tts) 进行语音合成。
- **友好的用户界面**
    - 通过 Fusion UI 构建了直观的多标签页界面。
    - 提供 Azure 与 MiniMax API 的单独配置窗口，便于管理密钥和区域等信息。
- **丰富的自定义设置**
    - 支持调整语速、音调、音量以及风格等参数。
    - 提供“停顿”按钮，便于在文本中插入停顿标签；同时支持“发音”功能，利用拼音转换处理多音字。
- **与 DaVinci Resolve 无缝集成**
    - 可直接从时间线提取字幕，并将合成后的音频自动添加至媒体池和当前时间线。

## 安装步骤 🔧

1. **下载代码**  
    克隆本仓库到本地：
    ```bash
    git clone https://github.com/2445868686/DaVinci-Resolve-TTS.git
    ```
2. **安装依赖**
	```
	pip install requests azure-cognitiveservices-speech edge_tts pypinyin
	```
	
3. **将`DaVinci Resolve TTS`文件夹移动到以下位置：**  
	Mac： 
	```sh
	/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit 
	```
	Win： 
	```sh
	C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Edit
	```

## 使用教程 💡

<img width="800" alt="截屏2025-02-08 09 04 10" src="https://github.com/user-attachments/assets/b943cde6-6885-4c5e-9395-d7d536e6871c" />

1. **启动插件**  
    - 在 DaVinci Resolve 工作区-脚本中运行后，会弹出主窗口。窗口中包含多个标签页，分别用于 Azure TTS、MiniMax TTS 以及配置信息与使用帮助。
2. **设置输出路径**  
    - 在配置栏界面，点击“浏览”按钮选择生成音频文件的保存路径。
3. **配置 API 信息**
    - 在配置栏界面，点击“配置”按钮打开 Azure API 配置窗口，填写区域和 API 密钥。
    - 若使用 MiniMax TTS，请点击对应的“配置”按钮填写 GroupID 和 API 密钥，并根据实际情况选择海外或国内版本。
4. **获取字幕与调整参数**
    - 点击“从时间线获取字幕”按钮，插件会自动提取当前时间线中的字幕，并填充到文本编辑框内，也可以复制文本到文本编辑框内。
    - 调整语速、音调、音量、风格及风格强度等参数。
    - 如需要插入停顿，可点击“停顿”按钮。
5. **合成语音**  
    根据需求选择“**朗读当前字幕**”或“**朗读文本框**”按钮。
	- **朗读当前字幕**：此按钮的功能是朗读当前播放头所处位置的字幕内容。
	- **朗读文本框**：此按钮的功能是朗读文本输入框中的所有文字。
    - 合成成功后插件将自动将生成的音频添加至媒体池，并加载到当前时间线中指定的位置。
6. **其他功能**
    - “发音”按钮：复制文本后利用 pypinyin 库生成带声调的拼音，有助于控制多音字的发音。
    - “播放预览”按钮：试听语音效果。

## 注意事项⚠️

- 请确保 API 密钥、区域等信息填写正确，否则语音合成将无法正常进行。
- 在使用过程中，如遇到问题请查看控制台输出日志，日志中包含详细的错误信息。
- 文件保存路径需要具有写入权限，否则可能导致音频文件保存失败。

## 贡献🤝

欢迎任何形式的贡献！如有问题、建议或 bug，请通过 GitHub issue 与我联系，或直接提交 pull request。

## **支持 ❤️**  

🚀 **热爱开源与 AI 创新？** 这个项目致力于让 AI 工具更加**实用**和**易用**，所有软件都是**完全免费**且**开源**的，旨在回馈社区，让更多人受益！  

如果你觉得这个项目对你有所帮助，欢迎支持我的工作！你的支持将帮助我持续开发，并带来更多令人兴奋的新功能！💡✨  

<img width="200" alt="A031269C-141F-4338-95F1-6018D40E0A3F" src="https://github.com/2445868686/Davinci-Resolve-SD-Text-to-Image/assets/50979290/a17d3ade-7486-4b3f-9b19-1d2d0c4b6945">



## 许可 📄

本项目采用 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。
