import readline  # noqa: F401

import sounddevice as sd
from ttslearn.dnntts import DNNTTS

dnntts_engine = DNNTTS()


def say(sentence: str):
    audio_array, sampling_rate = dnntts_engine.tts(sentence)
    sd.play(audio_array, sampling_rate)
    sd.wait()


if __name__ == "__main__":
    while True:
        sentence = input("読み上げたい文を入力してください (qで終了): ")
        stripped = sentence.strip()
        if not stripped:
            continue
        if stripped.lower() == "q":
            break

        say(stripped)
