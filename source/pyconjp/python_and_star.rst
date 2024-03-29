:ogp_title: Pythonとアスタリスク 🐍🌟💫🐍🌟💫
:ogp_event_name: pyconjp
:ogp_slide_name: python_and_star
:ogp_description: 2022/10 PyCon JP 2022 トーク スライド

.. _Python実践入門: https://gihyo.jp/book/2020/978-4-297-11111-3
.. _Effective Python 第2版: https://www.oreilly.co.jp/books/9784873119175/

.. role:: strike

================================================================================
Pythonとアスタリスク 🐍🌟💫🐍🌟💫
================================================================================

`#pyconjp <https://twitter.com/search?q=%23pyconjp>`_ `#pyconjp_4 <https://twitter.com/search?q=%23pyconjp_4>`_

:Event: PyCon JP 2022
:Presented: 2022/10/14 nikkie

ういっす✌️
============================================================

㊗️有明開催🌈（スタッフの方々、ありがとうございます！！👏❤️）

聞きに来てくださり、誠にありがとうございます
--------------------------------------------------

*ヒトツダケナンテエラベナイヨー* なラインナップですよね！（全45本）

お前、誰よ
============================================================

* **Python** 大好き、にっきー
* Twitter `@ftnext <https://twitter.com/ftnext>`__ ／ GitHub `@ftnext <https://github.com/ftnext>`__ ／ `はてなブログ <https://nikkie-ftnext.hatenablog.com/>`_
* **アニメ** も好きで、積極的に *アニメネタを仕込む* アウトプットスタイル

XPするデータサイエンティスト
--------------------------------------------------

* `株式会社ユーザベース <https://www.uzabase.com/jp/>`_
* *えぬえるぴーや* （自然言語処理、Python）にして *えくすぴーや* （テスト駆動開発、ペアプログラミング）
* We're hiring!! (Engineers, Data scientists, Researchers)

.. image:: https://drive.google.com/uc?id=19PMMnkqDiFMCJBPwoA1B51ltQBG0y4kL

.. include:: talk_introduction.rst.txt

お品書き：Pythonとアスタリスク 🐍🌟💫🐍🌟💫
============================================================

1. 二項算術演算子としての ``*``, ``**``
2. アンパック代入と ``*``
3. アンパック演算子としての ``*``, ``**``
4. 関数と ``*`` その1： *専用* 引数
5. 関数と ``*`` その2： *可変長* 引数

**LT⚡️が5本** ある感じです！
--------------------------------------------------

* オススメの聞き方： **興味** のあるトピックに **集中**
* 早くて分からなくなってしまったら **次のトピックから合流** で大丈夫です🙆‍♂️

この色のスライドは **休憩タイム** （本題ではありません）
------------------------------------------------------------

.. revealjs-section::
    :data-background-color: #002b36

* LTの間には閑話🍵コンテンツ
* さらに知りたい方向けコンテンツ（さら知り）は本編では駆け抜けます🏃‍♂️（スライド、作りすぎちった）

.. include:: as_binary_arithmetic_operator.rst.txt

お品書き：Pythonとアスタリスク 🐍🌟💫🐍🌟💫
============================================================

1. 二項算術演算子としての ``*``, ``**`` ✅
2. アンパック代入と ``*``
3. アンパック演算子としての ``*``, ``**``
4. 関数と ``*`` その1： *専用* 引数
5. 関数と ``*`` その2： *可変長* 引数

.. include:: tips/do_not_import_star.rst.txt

📺提供：にっきー（お前、誰よ 2/N）
--------------------------------------------------

.. revealjs-section::
    :data-background-color: #002b36

* PyCon JP 2019からスタッフ、2021は **座長** 🇨🇭

  * 小声：実は2021もオンサイト開催でした（ハイブリッドなので）

* そして、燃え尽きました！！

  * 現在の関心：コーディングでOSSにコントリビュート

📺提供：にっきー（お前、誰よ 2/N）
--------------------------------------------------

.. revealjs-section::
    :data-background-color: #002b36

* 毎月オンライン開催 `みんなのPython勉強会（Start Python Club） <https://startpython.connpass.com/>`_ スタッフしてます

  * `初学者向けコンテンツ <https://2022.pycon.jp/contents/communities/stapy>`_ に掲載、ありがとうございます！
  * 11月は11/10(木)開催です（Django Congress JP関連コンテンツ）

.. include:: in_unpack_assignment.rst.txt

お品書き：Pythonとアスタリスク 🐍🌟💫🐍🌟💫
============================================================

1. 二項算術演算子としての ``*``, ``**`` ✅
2. アンパック代入と ``*`` ✅
3. アンパック演算子としての ``*``, ``**``
4. 関数と ``*`` その1： *専用* 引数
5. 関数と ``*`` その2： *可変長* 引数

.. include:: tips/pack_unpack.rst.txt

.. include:: as_unpack_operator.rst.txt

お品書き：Pythonとアスタリスク 🐍🌟💫🐍🌟💫
============================================================

1. 二項算術演算子としての ``*``, ``**`` ✅
2. アンパック代入と ``*`` ✅
3. アンパック演算子としての ``*``, ``**`` ✅
4. 関数と ``*`` その1： *専用* 引数
5. 関数と ``*`` その2： *可変長* 引数

.. include:: tips/merge_dicts.rst.txt

さかなー🐟
============================================================

折り返してます！ **ストレッチ** しましょう🙌

.. include:: in_keyword_only_parameters.rst.txt

お品書き：Pythonとアスタリスク 🐍🌟💫🐍🌟💫
============================================================

1. 二項算術演算子としての ``*``, ``**`` ✅
2. アンパック代入と ``*`` ✅
3. アンパック演算子としての ``*``, ``**`` ✅
4. 関数と ``*`` その1： *専用* 引数 ✅
5. 関数と ``*`` その2： *可変長* 引数

.. include:: tips/stars_in_stdlib.rst.txt

📺提供：にっきー（お前、誰よ 3/3）
--------------------------------------------------

.. revealjs-section::
    :data-background-color: #002b36

* ソフトウェアを作ることに関心があります

  * ソフト＝ **変更容易**
  * 私の書いてきたコード、変更難度高すぎるハードウェアなんですよ😢

📺提供：にっきー（お前、誰よ 3/3）
--------------------------------------------------

.. revealjs-section::
    :data-background-color: #002b36

* 『`良いコード/悪いコードで学ぶ設計入門 <https://gihyo.jp/book/2022/978-4-297-12783-1>`_』（ミノ駆動本）の **読書会** 、オンラインで共催してます📖

  * `ミノ駆動本_読書py <https://pythonista-books.connpass.com/>`_ 次回は `10/21(金)夜 <https://pythonista-books.connpass.com/event/262554/>`_ 隔週開催です！

* 📣他の方の意見を聞きながら読みたい本がある方、ノウハウお伝えできます！

.. include:: as_var_positional_var_keyword.rst.txt

Pythonとアスタリスク 🐍🌟💫🐍🌟💫 駆け抜けましたね⚡️
============================================================

1. 二項算術演算子としての ``*``, ``**`` ✅
2. アンパック代入と ``*`` ✅
3. アンパック演算子としての ``*``, ``**`` ✅
4. 関数と ``*`` その1： *専用* 引数 ✅
5. 関数と ``*`` その2： *可変長* 引数 ✅

閑話コンテンツたち🍵
--------------------------------------------------

* ``from module_or_package import *`` オススメしません
* タプルのパック↔️シーケンスのアンパック
* 辞書のマージはPython 3.9からは ``|`` で
* 標準ライブラリの ``*``, ``**``

学んだもの（ぜひ血肉にしてください）
--------------------------------------------------

* シーケンス、イテラブル、特殊メソッド
* catch-allアンパック
* 関数の仮引数の ``*``, ``/``, ``*args``, ``**kwargs``
* アンパック演算子を使って、新しいシーケンスを作る & 関数の可変長引数に渡す

ご清聴ありがとうございました！
--------------------------------------------------

| May the Stars🌟 be with you
| *星🌟は君の頭上に輝くよ*

Appendix
============================================================

* References
* Overrun contents（さらなる ``*``）

.. include:: appendix/references.rst.txt

.. include:: appendix/overrun.rst.txt

EOF
==============================
