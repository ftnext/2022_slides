"""青空文庫の『吾輩は猫である』から本文テキストを取り出す

ref: 『Pythonによるあたらしいデータ分析の教科書』5章 5.2.5
"""

import re
import zipfile

with zipfile.ZipFile("789_ruby_5639.zip", "r") as zipf:
    data = zipf.read("wagahaiwa_nekodearu.txt")
text = data.decode("shift_jis")

text = re.split(r"\-{5,}", text)[2]  # TODO: テキストファイル確認
text = text.split("底本：")[0]  # 「底本：」より前が本文
text = re.sub(r"《.+?》", "", text)  # ルビ？を除いている？
text = re.sub(r"［＃.+?］", "", text)  # 入力者による注を除く
text = text.strip()
text = text.replace("\u3000", "")  # 空白文字を除く
# text = text.replace("\r", "").replace("\n", "")  # 改行コードを除く

with open("clean_wagahaiwa_nekodearu.txt", "w") as f:
    f.write(text)
