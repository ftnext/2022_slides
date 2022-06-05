"""Web上のリソースを取得する

ref: 『Pythonによるあたらしいデータ分析の教科書』5章 5.2.5

以下の取得に使用
- 青空文庫 『吾輩は猫である』
- 日本語極性評価辞書
"""

import argparse
import urllib.request
from urllib.parse import urlparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    parsed = urlparse(args.url)
    output_file = parsed.path.split("/")[-1]
    urllib.request.urlretrieve(args.url, output_file)
