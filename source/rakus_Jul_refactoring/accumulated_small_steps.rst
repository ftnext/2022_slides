:ogp_title: 達人の驚くほど小さいリファクタリング
:ogp_event_name: rakus_Jul_refactoring
:ogp_slide_name: accumulated_small_steps
:ogp_description: 2022/07 リファクタリングLT スライド（発表後IMO明示版）

============================================================
達人の驚くほど小さいリファクタリング
============================================================

:Event: リファクタリングLT
:Presented: 2022/07/28 nikkie

お前、誰よ（自己紹介）
============================================================

* Python（とアニメ）大好き **にっきー** ／ Twitter `@ftnext <https://twitter.com/ftnext>`__ ／ GitHub `@ftnext <https://github.com/ftnext>`__
* 株式会社ユーザベースでアジャイル開発するデータサイエンティスト（自称えぬえるぴーや😎）
* イチオシアニメ『アイの歌声を聴かせて』 ㊗️ `配信開始 <https://ainouta.jp/ondemand.html>`_ ！

面白いからみんな観て🙏（配信も！）
--------------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/oS36ehQVPYU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

ラクスさんのLT会、お世話になっております
--------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2022_slides/rakus_Jun_oo/minodriven_book_circle.html"
        title="1人で、みんなで、ミノ駆動本で学ぶオブジェクト指向"></iframe>

ミノ駆動本_読書py 共催しています
--------------------------------------------------

* ミノ駆動さんの『`良いコード／悪いコードで学ぶ設計入門 <https://gihyo.jp/book/2022/978-4-297-12783-1>`_』をPython使いの視点で読む読書会
* 主催：nikkie、Yumihikiさん
* 次回 `7/29(金) 10章 名前設計の前半 <https://pythonista-books.connpass.com/event/254917/>`_！（〜10.3）

達人の驚くほど小さいリファクタリングについて話します
============================================================

ここから本題

このLTで伝えたいこと
--------------------------------------------------

* 「リファクタリングのステップ、 **小さっ！**」という衝撃を共有
* 1個1個は小さいリファクタリング、それを **何回も何回も行う** ことでコードが良くなっていく！（と理解）

.. _リファクタリング: https://www.ohmsha.co.jp/book/9784274224546/

参考書籍
--------------------------------------------------

* 元ネタは『The Art of Agile Development Second edition』（James Shore）の `リファクタリングの章 <https://www.jamesshore.com/v2/books/aoad2/refactoring>`_

  * 書籍で紹介されたリファクタリングをPythonに書き換えています（リファクタリング方針についてのフィードバックはJamesさん・Pythonのコードについてはnikkieへ）

* Martin Fowler『`リファクタリング`_』第1章にも「小さい！」という感想を抱きました

今回のサンプルコード
============================================================

アルファベットを13文字入れ替える

.. code-block:: python

    >>> transform("a")  # 13文字先のnに変える（小文字のまま）
    'n'
    >>> transform("N")  # 13文字前のAに変える（大文字のまま）
    'A'

変換表
--------------------------------------------------

.. list-table::

    * - a
      - b
      - c
      - d
      - e
      - f
      - g
      - h
      - i
      - j
      - k
      - l
      - m
    * - n
      - o
      - p
      - q
      - r
      - s
      - t
      - u
      - v
      - w
      - x
      - y
      - z

.. code-block:: python

    >>> transform("NIKKIE")
    'AVXXVR'
    >>> transform("satomi")
    'fngbzv'

アルファベットでないなら変換しません
--------------------------------------------------

.. code-block:: python

    >>> transform("satomi1231")  # 数字は変換されない
    'fngbzv1231'
    >>> transform("🤗")  # emojiも変換されない
    '🤗'

リファクタリング前の実装
============================================================

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :linenos:

Pythonに書き直しました（Python 3.10）

変換戦略
--------------------------------------------------

* 関数 ``transform`` は、受け取った文字列の1文字ごとに *文字コードに変換して* ``transform_letter`` 関数を呼び出す

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :pyobject: transform
    :emphasize-lines: 6-8

``transform_letter`` 関数
--------------------------------------------------

* 文字コードを受け取り、文字列を返す
* ``A-Ma-m`` の場合と ``N-Zn-z`` の場合で分岐（判定に ``is_between`` 関数を使用）

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :pyobject: transform_letter

``is_between`` 関数
--------------------------------------------------

* 文字コードと範囲の開始・終了の文字を受け取る
* ``code_for`` 関数で文字コードに変換して、範囲に含まれるか返す

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :pyobject: is_between

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :pyobject: code_for

今回のリファクタリングのアイデア
============================================================

文字コードにせずに **文字のまま** でも比較できる！

.. code-block:: python

    >>> ord("a") <= ord("c") <= ord("m")
    True
    >>> "a" <= "c" <= "m"
    True

リファクタリング後の実装
--------------------------------------------------

.. literalinclude:: ../../samplecode/refactoring/after.py
    :language: python
    :linenos:

すごーくスッキリ！✨

``transform`` の単体テストコードはあります
--------------------------------------------------

.. code-block::

    $ python -m unittest
    ........
    ----------------------------------------------------------------------
    Ran 8 tests in 0.001s

    OK

https://github.com/ftnext/aoad2e-py/blob/start-refactoring/refactoring/test_rot13.py

質問：皆さんはどこからリファクタリングしますか❓
--------------------------------------------------

💡文字コードでなく文字で比較する

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :linenos:

文字コードでなく文字で比較しよう（nikkieの場合）
--------------------------------------------------

* ``transform_letter`` 関数をいじっていく
* 引数 ``char_code`` 消して、 ``letter`` 導入

.. literalinclude:: ../../samplecode/refactoring/before.py
    :language: python
    :pyobject: transform_letter
    :linenos:

.. revealjs-break::

* 導入したletter引数を渡す ``is_between`` 関数も変えて
* あ、``char_code`` どうするんだ？
* **格闘の末**、テスト全部通った！できた🙌

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,2,4

    def transform_letter(letter: str) -> str:
        if is_between(letter, "a", "m") or is_between(letter, "A", "M"):
            char_code += 13
        elif is_between(letter, "n", "z") or is_between(letter, "N", "Z"):
            char_code -= 13
        return chr(char_code)

文字コードでなく文字で比較しよう（達人の場合）
--------------------------------------------------

* **まずは** ``transform_letter`` 関数に **引数を追加するだけ**
* テストを全部通ることを確認（間違えていない😎）

.. code-block:: diff

    -        result += transform_letter(char_code)
    +        result += transform_letter(character, char_code)

    -def transform_letter(char_code: int) -> str:
    +def transform_letter(letter: str, char_code: int) -> str:

衝撃の「引数追加するだけ」
--------------------------------------------------

* 2手目3手目を続ける前提で初手は引数追加だけ
* **動きをいきなり変えない** のか！！
* 達人がどのようにリファクタリングするか一緒に見ていきましょう（10分に収まらない量なので、時間の許す限り）

.. include:: yoda_refactoring.rst.txt

書籍を通じて達人とリファクタリングしてみて
============================================================

まとめ🌯に代えて、気付きを最後に共有します（気付きについてのフィードバックはnikkieまで）

IMO: クソデカリファクタリングしかやってこなくて、すみませんでした！（懺悔）
--------------------------------------------------------------------------------

* リファクタリング＝ **小さいステップを積み上げる** と認識が変わった
* ステップが小さいので、テストが落ちているREDの時間が最小にできる
* チームでどうやるかは実践して学びを得たい

IMO: 小さいステップでリファクタリングするには
--------------------------------------------------

* 『`リファクタリング`_』にあるような知識（例：関数のインライン化）が必要
* **テクニックを知っているからこそ** 小さいステップに分解できる
* テクニックを知る＝IDE操作を知るにもなりそう

IMO: 小さいステップのリファクタリングの効果
--------------------------------------------------

* 小さいステップに分けているからこそ **今はここまで** ができる

  * 出した例では正規表現を導入せずに止めてもいい
  * 今は時間がないけど、ここは設計変えていきたいから「 **一手目として変数追加だけ** やろう」もできるはず（👉 *発表後記*）

.. _レガシーコード改善ガイド: https://www.shoeisha.co.jp/book/detail/9784798116839

IMO: 『`レガシーコード改善ガイド`_』を思い出す
--------------------------------------------------

* 小さなステップに分けて、 **いまできる手数だけ** リファクタリング
* betterな設計に向けてチームが動き出すための足がかりを作るということ🌱
* 6章 スプラウトクラスやラップクラスに通じるかも

.. _エクストリームプログラミング: https://www.ohmsha.co.jp/book/9784274217623/

結びに：ケント・ベック言ってた！（『エクストリームプログラミング』 はじめに）
--------------------------------------------------------------------------------

    | どんな状況でも必ず改善できる。
    | どんなときでもあなたから改善を始められる。
    | どんなときでも今日から改善を始められる。

達人のリファクタリングを知り、 **小さく改善** していけるイメージ！

小さなリファクタリングを積み上げていきましょう！
============================================================

ご清聴ありがとうございました

関連アウトプット
============================================================

* Python写経コード https://github.com/ftnext/aoad2e-py/tree/main/refactoring
* 事前アウトプット ブログ版 `え、待って！リファクタリングって1つ1つのステップそんなに小さく実施するの！？ （『The Art of Agile Development』読書録） <https://nikkie-ftnext.hatenablog.com/entry/art-of-agile-development-2nd-really-small-refactoring-steps>`_

IMO 発表後記：一手目として変数追加だけ
============================================================

* チャットではネガティブな反応が多数だった（と思っている）こちらについて発表後版で補足します
* なんにでもメリット・デメリットはあると思っていて、「一手目として変数追加だけ」も実践して学びを得ようと思っています

.. revealjs-break::

* 開発者のコミュニケーションのきっかけとして期待（コードを読んで「私ここやっておきますね」ができるのでは）
* *数手重ねた小まとまり* まで進めたほうが現実的なのかも

.. revealjs-break::

* ラップクラスでも「そんなことしたら前よりも悪くなる」という反応はあったと聞いています
* 「その時点では、そのとおりです」と続きます（『`レガシーコード改善ガイド`_』 p.85）
* 小さなリファクタリングを **重ねる前提** で **足がかりを作る** ためにやるのかなと理解しています

EOF
============================================================
