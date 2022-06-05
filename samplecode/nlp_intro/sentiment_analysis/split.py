import argparse
import re
import subprocess
from collections.abc import Generator


def split(line: str) -> Generator[str, None, None]:
    splitter_output = call_splitter(line)
    for sentence in splitter_output.split("\n"):
        if not sentence:
            continue
        prefix_subtracted = re.sub(r"^Sentence\s\d+:\s", "", sentence)
        yield prefix_subtracted


def call_splitter(line: str) -> str:
    p1 = subprocess.Popen(["echo", f"{line}"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(
        ["node_modules/.bin/sentence-splitter"],
        stdin=p1.stdout,
        stdout=subprocess.PIPE,
    )
    p1.stdout.close()
    output = p2.communicate()[0]
    return output.decode()


def sentence_split(input_file: str, output_file: str) -> None:
    with open(input_file) as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.rstrip()
            if not line:
                continue
            for sentence in split(line):
                fout.write(f"{sentence}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    sentence_split(args.input, args.output)
