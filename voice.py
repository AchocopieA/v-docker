# import streamlit as st
# import requests

# # メイン関数
# def main():
#     st.title("Text to Speech with Faster Whisper")

#     # ユーザーが入力するテキストボックス
#     user_text = st.text_area("Enter the text you want to convert to speech:")

#     if st.button("Generate Speech"):
#         if user_text:
#             # Faster Whisper APIにリクエストを送信
#             response = requests.post(
#                 "http://192.168.2.128:5000/api/v1/synthesize",
#                 json={"text": user_text}
#             )

#             if response.status_code == 200:
#                 # 音声ファイルのバイナリデータを取得
#                 audio_data = response.content

#                 # 音声ファイルの保存
#                 with open("output.wav", "wb") as f:
#                     f.write(audio_data)

#                 # 音声ファイルのダウンロードリンク
#                 st.audio(audio_data, format="audio/wav")
#                 st.download_button("Download Speech", data=audio_data, file_name="output.wav", mime="audio/wav")
#             else:
#                 st.error("Failed to generate speech. Please try again.")
#         else:
#             st.warning("Please enter some text to convert.")
















import streamlit as st
import pyttsx3
# from text_to_speech import text_to_speech  # text_to_speech関数をインポート
import os

def text_to_speech(text, file_path):
    engine = pyttsx3.init()

    # 音声のスピード調整
    rate = engine.getProperty('rate')
    print('デフォルトの音声スピード: {}'.format(rate))
    engine.setProperty('rate', 180)

    # 音量調整
    engine.setProperty('volume', 2.0) # デフォルトは1.0
    volume = engine.getProperty('volume')
    print('現在のボリューム: {}'.format(volume))

    # 音声を「滑らかな女性」の方に設定
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    for i, voice in enumerate(voices):
        print(f"Voice {i} has ID {voice.id}")

    engine.save_to_file(text, file_path)
    engine.runAndWait()

# メイン関数
def main():


    st.title("Text to Speech Converter")
    
    # ユーザーがテキストを入力
    text = st.text_area("Enter text here:", "")
    
    if st.button("Convert to Speech"):
        if text:
            output_file = "output.mp3"
            text_to_speech(text, output_file)
            st.success("Conversion successful! Click below to download.")
            
            # 音声ファイルをダウンロードリンクとして表示
            with open(output_file, "rb") as file:
                btn = st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=output_file,
                    mime="audio/mpeg"
                )
            # 一時ファイルの削除
            os.remove(output_file)
        else:
            st.error("Please enter some text to convert.")



if __name__ == "__main__":
    main()













# import streamlit as st
# import requests


# def main():
#     st.title("Text to Speech Converter")
    
#     text = st.text_area("Enter text here:", "")
    
#     if st.button("Convert to Speech"):
#         if text:
#             response = requests.post(
#                 "http://192.168.2.128:5000/convert",
#                 data={'text': text}
#             )
            
#             if response.status_code == 200:
#                 st.success("Conversion successful! Click below to download.")
#                 st.download_button(
#                     label="Download MP3",
#                     data=response.content,
#                     file_name="output.mp3",
#                     mime="audio/mpeg"
#                 )
#             else:
#                 st.error("Error in conversion. Please try again.")
#         else:
#             st.error("Please enter some text to convert.")



# if __name__ == "__main__":
#     main()

