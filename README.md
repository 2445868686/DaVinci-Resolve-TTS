<div align="center">
    
# <span style="color: #2ecc71;">DavVinci-Resolve-TTS 🎤✨</span>

**[English](README.md) | [简体中文](README_CN.md)**
</div>

## Introduction 🚀

This project builds a graphical interface plugin based on DaVinci Resolve's scripting API and Fusion UI, enabling Text-to-Speech (TTS) functionality within DaVinci Resolve. The plugin supports two voice synthesis services: Microsoft [Azure's TTS](https://speech.microsoft.com/) and [MiniMax TTS](https://intl.minimaxi.com/), offering various parameter configurations (such as speech rate, pitch, volume, style, pauses, etc.) and a complete workflow for generating speech directly from timeline/text captions, previewing, and loading into the media pool.

![TTS](https://github.com/user-attachments/assets/0626ed7e-40c9-4b8f-92ee-736ca6756619)

## Project Features 🎉
- **Multi-Service Support**
    - Integrates Microsoft [Azure's TTS](https://speech.microsoft.com/) and [MiniMax TTS](https://intl.minimaxi.com/) services, allowing flexible switching based on requirements.
    - Option to disable API mode and directly use [Edge TTS](https://github.com/rany2/edge-tts) for voice synthesis.
- **User-Friendly Interface**
    - Builds an intuitive multi-tabbed interface using Fusion UI.
    - Provides separate configuration windows for Azure and MiniMax APIs, making it easy to manage keys and region information.
- **Rich Customization Options**
    - Supports adjusting speech rate, pitch, volume, style, and style intensity.
    - Offers a "Pause" button to insert pause tags in the text; also supports a "Pronunciation" feature using pinyin conversion to handle polyphonic characters.
- **Seamless Integration with DaVinci Resolve**
    - Automatically extracts captions from the timeline and adds the synthesized audio to the media pool and the current timeline.
  
## Installation 🔧

> 🚀 **You can download the plugin** [👉 **HERE** 👈](https://ko-fi.com/s/9e769243b5) **instead of through GitHub!**

1. **Download the Code**  
    Clone the repository to your local machine:
    ```bash
    git clone https://github.com/2445868686/DaVinci-Resolve-TTS.git
    ```
2. **Install Dependencies**
    ```bash
    pip install requests azure-cognitiveservices-speech edge_tts pypinyin
    ```
3. **Move the `DaVinci Resolve TTS` Folder to the Following Location:**  
    - **Mac:**
    ```sh
    /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit
    ```
    - **Windows:**
    ```sh
    C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Edit
    ```

## Usage 💡

<img width="800" alt="截屏2025-02-08 09 04 10" src="https://github.com/user-attachments/assets/b943cde6-6885-4c5e-9395-d7d536e6871c" />

1. **Launch the Plugin**  
    - After running the script in DaVinci Resolve's workspace, a main window will pop up. The window contains multiple tabs for Azure TTS, MiniMax TTS, configuration settings, and usage help.
2. **Set Output Path**  
    - In the configuration interface, click the "Browse" button to select the save path for the generated audio files.
3. **Configure API Information**
    - In the configuration interface, click the "Configure" button to open the Azure API configuration window, where you can fill in the region and API key.
    - If using MiniMax TTS, click the corresponding "Configure" button to fill in the GroupID and API key, and choose between the overseas or domestic version based on your needs.
4. **Get Captions and Adjust Parameters**
    - Click the "Get Captions from Timeline" button to automatically extract captions from the current timeline and populate them into the text editor. Alternatively, you can copy text directly into the text editor.
    - Adjust parameters such as speech rate, pitch, volume, style, and style intensity.
    - If you need to insert pauses, click the "Pause" button.
5. **Synthesize Speech**  
    Choose the "**Read Subs**" or "**Read TextBox**" button based on your needs.
    - **Read Subs**: This button reads the caption content at the current playhead position.
    - **Read TextBox**: This button reads all text in the text input box.
    - The plugin will automatically add the generated audio to the media pool and load it into the specified position on the current timeline upon successful synthesis.
6. **Other Features**
    - "Pronunciation" button: After copying text, the plugin generates pinyin with tones using the pypinyin library, helping to control the pronunciation of polyphonic characters.
    - "Preview" button: Listen to the synthesized speech.

## Notes ⚠️

- Ensure that the API key, region, and other information are correctly filled in; otherwise, voice synthesis may not work properly.
- If you encounter issues during use, check the console output logs, which contain detailed error information.
- The file save path must have write permissions; otherwise, audio file saving may fail.

## Contribution 🤝

Contributions of any kind are welcome! If you have any issues, suggestions, or bugs, please contact me via GitHub issues or submit a pull request.

## Support ❤️
🚀 **Passionate about open-source and AI innovation?** This project is dedicated to making AI-powered tools more **practical** and **accessible**. All software is **completely free** and **open-source**, created to give back to the community!  

If you find this project helpful, consider supporting my work! Your support helps me continue development and bring even more exciting features to life! 💡✨  

 [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G31A6SQU)  

## License 📄

This project is licensed under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.
