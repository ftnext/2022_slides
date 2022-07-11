import tempfile

import numpy as np
import soundfile as sf
import speech_recognition as sr
from espnet2.bin.asr_inference import Speech2Text
from scipy.io import wavfile

speech2text = Speech2Text.from_pretrained(
    "kan-bayashi/csj_asr_train_asr_transformer_raw_char_sp_valid.acc.ave"
)


def input_from_microphone(recognizer: "sr.Recognizer") -> "sr.AudioData":
    with sr.Microphone(sample_rate=16_000) as source:
        print("なにか話してください")
        audio = recognizer.listen(source)
        print("音声を取得しました")
        return audio


def convert_to_array(audio: "sr.AudioData") -> "np.array":
    frame_bytes = audio.get_raw_data()
    speech_array = np.frombuffer(frame_bytes, dtype=np.int16)
    with tempfile.NamedTemporaryFile() as tempf:
        wavfile.write(tempf.name, audio.sample_rate, speech_array)
        audio_array, sampling_rate = sf.read(tempf.name)
        return audio_array


def recognize_speech(audio_array: "np.array") -> str:
    nbests = speech2text(audio_array)
    text, tokens, *_ = nbests[0]
    return text


if __name__ == "__main__":
    r = sr.Recognizer()

    while True:
        audio = input_from_microphone(r)
        array = convert_to_array(audio)
        text = recognize_speech(array)
        print(text)

        character = input("ここで終了する場合はq、続ける場合はEnterを押してください: ")
        if character.strip().lower() == "q":
            break
