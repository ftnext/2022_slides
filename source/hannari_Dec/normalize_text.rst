導入

* 自然言語処理
* 形態素解析
* MeCab
* 辞書
* 辞書の1つ neologd (mecab-ipadic-neologd)

解析前に行うことが望ましい文字列の正規化処理

https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja

かいつまんで紹介することになりそう

.. include:: neologd_normalization.rst.txt

.. >>> p = re.compile("([{}]) ([{}])".format(basic_latin, blocks))
.. >>> s = "ＰＲＭＬ　　副　読　本"  # 全角・半角と全角スペースの扱いがいる
.. >>> while p.search(s):
.. ...     s = p.sub(r"\1\2", s)
.. >>> s  # 全角・半角は他の処理と合わせて
.. 'ＰＲＭＬ副読本'

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
