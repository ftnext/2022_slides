"""青空文庫の『吾輩は猫である』を取得する

ref: 『Pythonによるあたらしいデータ分析の教科書』5章 5.2.5
"""

import urllib.request

urllib.request.urlretrieve(
    "https://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip",
    "789_ruby_5639.zip",
)
