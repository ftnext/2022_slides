import argparse

import speech_recognition as sr


def input_from_microphone(recognizer: "sr.Recognizer") -> "sr.AudioData":
    with sr.Microphone(sample_rate=16_000) as source:
        print("なにか話してください")
        audio = recognizer.listen(source)
        print("音声を取得しました")
        return audio


def recognize_speech(
    recognizer: "sr.Recognizer", audio: "sr.AudioData", credentials: str
) -> str:
    recognized_text = recognizer.recognize_google_cloud(
        audio, credentials, language="ja-JP"
    )
    return recognized_text.strip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("credentials_path")
    args = parser.parse_args()

    with open(args.credentials_path) as f:
        credentials = f.read()

    r = sr.Recognizer()

    while True:
        audio = input_from_microphone(r)
        text = recognize_speech(r, audio, credentials)
        print(text)

        character = input("ここで終了する場合はq、続ける場合はEnterを押してください: ")
        if character.strip().lower() == "q":
            break
