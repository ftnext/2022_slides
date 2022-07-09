import readline  # noqa: F401
import subprocess


def say(sentence: str):
    subprocess.run(["say", "-v", "Kyoko", sentence])


if __name__ == "__main__":
    while True:
        sentence = input("読み上げたい文を入力してください (qで終了): ")
        stripped = sentence.strip()
        if not stripped:
            continue
        if stripped.lower() == "q":
            break

        say(stripped)
