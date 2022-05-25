:ogp_title: \* と **
:ogp_event_name: rakus_May_pythontips
:ogp_slide_name: superstar
:ogp_description: 2022/05 Python Tips LT会 - vol.3 LT スライド

============================================================
``*`` と ``**``
============================================================

🌟💫🌟💫🌟💫🌟💫🌟💫🌟💫

:Event: Python Tips LT会 - vol.3
:Presented: 2022/05/25 nikkie

質問です！ どうなるでしょうか？
============================================================

.. code-block:: python

    >>> *(1, 2)

* Python **3.10** で動作確認
* 現在サポートされている Python 3.7 以降で再現します（はず）

お前、誰よ
============================================================

* 「お前、誰よ」は自己紹介のエイリアス（Python界隈の慣習）
* Python大好き **にっきー**

  * Twitter `@ftnext <https://twitter.com/ftnext>`_ ／ GitHub `@ftnext <https://github.com/ftnext>`_

* 株式会社ユーザベースのデータサイエンティスト（NLPer）

Python Tips LT、お世話になっております
--------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/rakus_Feb_pythontips/about_yield.html"
        title="yieldについて"></iframe>

.. revealjs-break::

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/rakus_Aug_pythontips/about_decorators.html"
        title="デコレータについて"></iframe>

最近のPythonニュース
--------------------------------------------------

NHKのドラマ『17才の帝国』に㊗️ **出演**

.. revealjs-break::
    :notitle:

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/17%E6%89%8D%E3%81%AE%E5%B8%9D%E5%9B%BD?src=hash&amp;ref_src=twsrc%5Etfw">#17才の帝国</a> 第2話を視聴。<br><br>え、待って！<br>プログラミング言語のPythonが出演してる！！<br>PythonがNHKに！！！<br><br>あと真木くんのエディタがAtom！<br>VSCodeじゃなくてAtom！！<br>AtomもNHKに！！！（再現画像）<br><br>コードはめっちゃ突っ込みどころが😂<br><br>真木くんのコードはこちらから<a href="https://t.co/z7xE4nKEYg">https://t.co/z7xE4nKEYg</a> <a href="https://t.co/sOPTpfR9pf">pic.twitter.com/sOPTpfR9pf</a></p>&mdash; nikkie にっきー シオンv0.0.1開発中⚒ (@ftnext) <a href="https://twitter.com/ftnext/status/1527865711942504449?ref_src=twsrc%5Etfw">May 21, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

もう1つ：読書会やるんで、`みんな来て <https://pythonista-books.connpass.com/event/248895/>`_！
----------------------------------------------------------------------------------------------------

* #ミノ駆動本 『`良いコード／悪いコードで学ぶ設計入門 <https://gihyo.jp/book/2022/978-4-297-12783-1>`_』
* Javaのコード例で示された設計を **Pythonにどう適用するか** 考えたい！

再掲：どうなるでしょうか？
============================================================

.. code-block:: python

    >>> *(1, 2)

考えながらお聞きください

Pythonにおける ``*`` と ``**``
============================================================

* 二項演算子（ ``*`` は乗算、 ``**`` はべき乗）
* 可変長引数（ ``*args, **kwargs`` ）
* *アンパック演算子*

他にも浮かんだらぜひ教えてください🙏

Pythonにおける ``*``
--------------------------------------------------

* catch-all アンパック代入
* *キーワード専用引数*

他にも浮かんだらぜひ教えてください🙏🙏

このLTでは、2つの切り口 🌟💫🌟💫
============================================================

1. アンパック
2. 関数の引数

紹介できないものはAppendixへ

お品書き ``*`` と ``**`` 🌟💫🌟💫
--------------------------------------------------

1. アンパック演算子
2. 関数と ``*`` や ``**``

    a. キーワード専用引数
    b. 可変長引数

.. include:: unpack_operators.rst.txt

閑話休題：PyCon JP 2022はプロポーザルを募集中！
============================================================

* `Python Conference Japan 2022 <https://2022.pycon.jp/>`_ は10/14(金)-16(日) 有明で開催
* https://pretalx.com/pyconjp2022/cfp
* JST **6/13(月)** 20:59まで

.. include:: function_with_stars.rst.txt

まとめ🌯 ``*`` と ``**`` 🌟💫🌟💫
============================================================

* {イテラブル,辞書}アンパック演算子
* 可変長{位置,キーワード}引数 + アンパック演算子との組合せ
* これらは頻出ではないですが、 **知っていたからこそ簡単に書けた瞬間** が訪れると思います

ご清聴ありがとうございました
------------------------------------------------

Enjoy development with stars! 🌟💫

TODO：appendix（追加をお楽しみに！）

EOF
==============================
