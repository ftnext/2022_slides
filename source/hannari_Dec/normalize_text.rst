導入

* 自然言語処理
* 形態素解析
* MeCab
* 辞書
* 辞書の1つ neologd (mecab-ipadic-neologd)

解析前に行うことが望ましい文字列の正規化処理

https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja

かいつまんで紹介することになりそう

先頭と末尾の半角スペースは削除

.. code-block:: python

    >>> "      テキストの前".strip()
    'テキストの前'
    >>> "テキストの後      ".strip()
    'テキストの後'

https://docs.python.org/ja/3/library/stdtypes.html#str.strip

文字を置換して揃える

* ハイフンマイナスっぽい文字
* 長音記号っぽい文字
* 1回以上連続する長音記号

.. code-block:: python

    >>> import re
    >>> re.sub("[˗֊‐‑‒–⁃⁻₋−]+", "-", "o₋o")
    'o-o'
    >>> re.sub("[﹣－ｰ—―─━ー]+", "ー", "majika━")
    'majikaー'
    >>> re.sub("[﹣－ｰ—―─━ー]+", "ー", "スーパーーーー")
    'スーパー'

* チルダっぽい文字は削除

.. code-block:: python

    >>> re.sub("[~∼∾〜〰～]", "", "わ〰い")
    'わい'

全角・半角

* 全角英数字は半角に置換
* 半角カタカナは全角に置換

.. code-block:: python

    >>> import re
    >>> import unicodedata
    >>> pt = re.compile("([０-９Ａ-Ｚａ-ｚ｡-ﾟ]+)")  # 半角カタカナ含む
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "０１２３４５６７８９")
    ... )
    '0123456789'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ")
    ... )
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
    ... )
    'abcdefghijklmnopqrstuvwxyz'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "ﾊﾝｶﾞｸ")
    ... )
    'ハンガク'

* 全角であれば半角に置換する記号
* 半角であれば全角に置換する記号

.. code-block:: python

    >>> mapping = str.maketrans(  # 一度全角に揃える
    ...     '!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣',
    ...     "！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」"
    ... )
    >>> pt = re.compile("([！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝〜]+)")
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "!#".translate(mapping))
    ... )
    '!#'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "!\"#$%&'()*+,-./:;<>?@[¥]^_`{|}".translate(mapping))
    ... )
    '!”#$%&’()*+,-./:;<>?@[¥]^_`{|}'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "!”#$%&’()*+,-./:;<>?@[¥]^_`{|}".translate(mapping))
    ... )  # クォートを半角ではないものにした例
    '!”#$%&’()*+,-./:;<>?@[¥]^_`{|}'
    >>> "".join(
    ...     unicodedata.normalize("NFKC", x) if pt.match(x) else x
    ...     for x in re.split(pt, "！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝".translate(mapping))
    ... )
    '!”#$%&’()*+,-./:;<>?@[¥]^_`{|}'
    >>> # クォートについてはunicode.normalizeの修正が必要

半角スペースの削除

* 全角スペースは半角スペースに置換
* 1つ以上の半角スペースは、1つの半角スペースに置換
* （1つにした後 ``remove_extra_spaces`` されていそう）

.. s = re.sub('[ 　]+', ' ', s)

* 「ひらがな・全角カタカナ・半角カタカナ・漢字・全角記号」間に含まれる場合
* 「ひらがな・全角カタカナ・半角カタカナ・漢字・全角記号」と「半角英数字」の間に含まれる場合

.. code-block:: python

    >>> blocks = "".join(
    ...     (
    ...         "\u4E00-\u9FFF",  # CJK UNIFIED IDEOGRAPHS
    ...         "\u3040-\u309F",  # HIRAGANA
    ...         "\u30A0-\u30FF",  # KATAKANA
    ...         "\u3000-\u303F",  # CJK SYMBOLS AND PUNCTUATION
    ...         "\uFF00-\uFFEF",  # HALFWIDTH AND FULLWIDTH FORMS
    ...     )
    ... )
    >>> basic_latin = "\u0000-\u007F"
    >>> p = re.compile("([{}]) ([{}])".format(blocks, blocks))
    >>> s = "検索 エンジン 自作 入門 を 買い ました!!!"
    >>> while p.search(s):
    ...     s = p.sub(r"\1\2", s)
    >>> s
    '検索エンジン自作入門を買いました!!!'
    >>> p = re.compile("([{}]) ([{}])".format(blocks, basic_latin))
    >>> s = "アルゴリズム C"
    >>> while p.search(s):
    ...     s = p.sub(r"\1\2", s)
    >>> s
    'アルゴリズムC'

グループを確認するとよいかも

.. >>> p = re.compile("([{}]) ([{}])".format(basic_latin, blocks))
.. >>> s = "ＰＲＭＬ　　副　読　本"  # 全角・半角と全角スペースの扱いがいる
.. >>> while p.search(s):
.. ...     s = p.sub(r"\1\2", s)
.. >>> s  # 全角・半角は他の処理と合わせて
.. 'ＰＲＭＬ副読本'

日本語の分かち書きを戻せる

写経パート

* ここまでで動きは分かった
* huggingface/tokenizers みたいなインターフェースにしたい
* インターフェースの統一
* 処理の部品化

プロトコル

* 型ヒントでダックタイピングを表せる
* 抽象クラスとは別のアプローチを試したい

Sequenceが肝

* まとめられる・かつインターフェースが揃う
* Sequenceもまとめられる
