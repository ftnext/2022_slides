import warnings
from io import BytesIO

import numpy as np
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from espnet2.bin.asr_inference import Speech2Text
from ttslearn.dnntts import DNNTTS

warnings.filterwarnings("ignore")

speech2text = Speech2Text.from_pretrained(
    "kan-bayashi/csj_asr_train_asr_transformer_raw_char_sp_valid.acc.ave"
)

SAMPLING_RATE_HZ = 16_000


def input_from_microphone(recognizer: "sr.Recognizer") -> "sr.AudioData":
    with sr.Microphone(sample_rate=SAMPLING_RATE_HZ) as source:
        print("なにか話してください")
        audio = recognizer.listen(source)
        print("音声を取得しました")
        return audio


def convert_to_array(audio: "sr.AudioData") -> "np.array":
    wav_bytes = audio.get_wav_data()
    wav_stream = BytesIO(wav_bytes)
    audio_array, sampling_rate = sf.read(wav_stream)
    assert sampling_rate == SAMPLING_RATE_HZ
    return audio_array


def recognize_speech(audio_array: "np.array") -> str:
    nbests = speech2text(audio_array)
    text, tokens, *_ = nbests[0]
    return text


def recognize_mircophone_input(recognizer: "sr.Recognizer") -> str:
    audio = input_from_microphone(recognizer)
    array = convert_to_array(audio)
    return recognize_speech(array)


def process_text(sentence: str) -> str:
    return sentence


dnntts_engine = DNNTTS()


def say(sentence: str):
    audio_array, sampling_rate = dnntts_engine.tts(sentence)
    sd.play(audio_array, sampling_rate)
    sd.wait()


if __name__ == "__main__":
    r = sr.Recognizer()

    while True:
        text = recognize_mircophone_input(r)
        response = process_text(text)
        say(response)

        character = input("ここで終了する場合はq、続ける場合はEnterを押してください: ")
        if character.strip().lower() == "q":
            break
