================================================================================
Norm@lizer（文字列の正規化処理について）
================================================================================

:Event: ボーネンLT会 はんなりプログラミングの会
:Presented: 2022/12/16 nikkie

お前、誰よ
============================================================

* **Python** 大好き、にっきー（`アスタリスク好き <https://2022.pycon.jp/timetable?id=LPYF7C>`_）
* :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `はてなブログ <https://nikkie-ftnext.hatenablog.com/>`_
* 株式会社ユーザベースでデータサイエンティスト（自然言語処理、XP）
* 近江彼方さん、おめでとう🎂🐑

本編：自然言語処理の話です
================================================================================

* 日本語は文の中の単語が区切られていない
* **形態素解析** して

  * 単語分割＝分かち書き
  * 品詞付与

「オープンソース 形態素解析エンジン」MeCab
--------------------------------------------------

    言語, 辞書,コーパスに依存しない汎用的な設計

* https://taku910.github.io/mecab/

形態素解析に使う辞書
--------------------------------------------------

* MeCabの辞書の1つ mecab-ipadic-NEologd
* :fab:`github` https://github.com/neologd/mecab-ipadic-neologd

mecab-ipadic-NEologd を作る上で
--------------------------------------------------

* *解析前に行うことが望ましい文字列の正規化処理*
* https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja
* これを **理解し、真似る** のが今回のLTです

.. include:: neologd_normalization.rst.txt

.. >>> p = re.compile("([{}]) ([{}])".format(basic_latin, blocks))
.. >>> s = "ＰＲＭＬ　　副　読　本"  # 全角・半角と全角スペースの扱いがいる
.. >>> while p.search(s):
.. ...     s = p.sub(r"\1\2", s)
.. >>> s  # 全角・半角は他の処理と合わせて
.. 'ＰＲＭＬ副読本'

.. include:: implementation_proposal.rst.txt

まとめ🌯： ``Norm@lizer``
================================================================================

* mecab-ipadic-NEologdの文字列の正規化処理を理解し、真似た
* 正規表現や :code:`str.translate` を駆使して正規化している
* 🤗/tokenizersを参考にし、処理を部品化した実装を提案

ご清聴ありがとうございました！
--------------------------------------------------

さよなら2022年！！！🐯

mecab-ipadic-NEologd、学びをありがとう！

Appendix 関連アウトプット
============================================================

* :fab:`github` `提案実装 <https://github.com/ftnext/2022_slides/blob/main/samplecode/normalizers/assembled.py>`__
* Part2と関連： `huggingface/tokenizersのNormalizer観察記 〜処理の部品化と統一されたインターフェース〜 <https://nikkie-ftnext.hatenablog.com/entry/observe-huggingface-tokenizers-normalizers>`__

EOF
==============================
