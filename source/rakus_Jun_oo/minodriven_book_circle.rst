:ogp_title: 1人で、みんなで、ミノ駆動本で学ぶオブジェクト指向
:ogp_event_name: rakus_Jun_oo
:ogp_slide_name: minodriven_book_circle
:ogp_description: 2022/06 オブジェクト指向LT会 vol.4 LT スライド

============================================================
1人で、みんなで、ミノ駆動本で学ぶオブジェクト指向
============================================================

:Event: オブジェクト指向LT会 vol.4
:Presented: 2022/06/29 nikkie

お前、誰よ（自己紹介）
============================================================

* Python（とアニメ）大好き **にっきー** ／ Twitter `@ftnext <https://twitter.com/ftnext>`__ ／ GitHub `@ftnext <https://github.com/ftnext>`__
* 株式会社ユーザベースのデータサイエンティスト（自称えぬえるぴーや😎）
* `『アイの歌声を聴かせて』冒頭17分公開 <https://youtu.be/B79JyC1xflI>`_ ！ 面白いからみんな観て🙏

ラクスさんのLT会、お世話になっております
--------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2022_slides/rakus_Jun_agile/user_stories.html"
        title="ユーザーストーリーについて"></iframe>

.. カット Python マルチパラダイムと伝える

オブジェクト指向界隈の **今**
============================================================

ここから本題

**#ミノ駆動本**
--------------------------------------------------

N=1（個人の意見です）

ミノ駆動本って、何よ
--------------------------------------------------

* 『`良いコード／悪いコードで学ぶ設計入門 <https://gihyo.jp/book/2022/978-4-297-12783-1>`_』
* 副題： **保守しやすい** 成長し続けるコードの書き方
* 技術書だが、**和書全体** のランキング入り（大快挙だ！🎉）

.. revealjs-break::

* IMO： **オブジェクト指向のクラスの入門書** でもある
* 拙ブログ `#ミノ駆動本 2章を読んで、クラスの使い所がようやく分かった気がします <https://nikkie-ftnext.hatenablog.com/entry/minodriven-book-chapter2-class>`_
* プログラミング言語のクラス（という文法）に入門した後に、ミノ駆動本2章オススメ

.. https://twitter.com/ftnext/status/1532200432957014016

ミノ駆動本、学びたくさん
============================================================

例：ストラテジパターン
--------------------------------------------------

* **インターフェース** による条件分岐の実装（6章）
* IMO：ミノ駆動本で一番の学び（現時点）
* （本日既出ですね😃）

**Pythonでやるなら** こうかな
--------------------------------------------------

ミノ駆動本、読みながら考える

アウトプットしたい！
--------------------------------------------------

* Pythonでの実装をアウトプットする場
* **フィードバック** がほしい

そうだ、読書会開こう📖
============================================================

.. revealjs-break::
    :notitle:

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">「なければ主催すればいいんだし」ってことで読書会のグループ作りました<a href="https://t.co/oY7eAybj7s">https://t.co/oY7eAybj7s</a><br>直近では <a href="https://twitter.com/hashtag/%E3%83%9F%E3%83%8E%E9%A7%86%E5%8B%95%E6%9C%AC?src=hash&amp;ref_src=twsrc%5Etfw">#ミノ駆動本</a> をPythonでどう適用するかを考える読書会を予定しています。近日公開！<br><br>やりたいと発信したら、「私も」と手を挙げていただいた方がいて2人teamになり、とてもありがたいです😃 <a href="https://t.co/spRs6TSYjo">https://t.co/spRs6TSYjo</a></p>&mdash; nikkie にっきー シオンv0.0.1開発中⚒ (@ftnext) <a href="https://twitter.com/ftnext/status/1527687434946744320?ref_src=twsrc%5Etfw">May 20, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ミノ駆動本_読書py
--------------------------------------------------

* 主催：nikkie、Yumihikiさん
* 6月に2回開催
* 次回は `7/1(金) ストラテジパターンのところ <https://pythonista-books.connpass.com/event/251790/>`_ （ウェルカムカモーン）

.. _アートオブアジャイルデベロップメント読書会: https://agiledevs.connpass.com/event/240227/

Based on `アートオブアジャイルデベロップメント読書会`_
------------------------------------------------------------

* **アウトプットメイン** な別の読書会のやり方を参考に
* 事前に読んでくる（直前もくもく会あり）
* 読書会では「ここがわからん」「ここはわかった」をボイスチャット&テキストチャット

ミノ駆動本_読書pyでの学びの共有
============================================================

**2つ** 共有

1.「データクラス」は #増田本 にもありますよ
============================================================

読書会で出会った言葉

「データクラス」in #ミノ駆動本
--------------------------------------------------

* 1.3 さまざまな悪魔を招きやすいデータクラス

  * 「悪魔」＝ **設計や実装上の問題** （はじめに）😈

* 3章 クラス設計では、データクラスの悪魔を退治していく（成熟したクラスへ）

教えていただいた #増田本
--------------------------------------------------

* 『`現場で役立つシステム設計の原則 <https://gihyo.jp/book/2017/978-4-7741-9087-7>`_』(2017)
* 副題：変更を楽で安全にするオブジェクト指向の実践技法

#増田本 3章
--------------------------------------------------

    データとロジックを別のクラスに分けることがわかりにくさを生む

3章の中のタイトル

アンチパターン「データクラス」の解像度が上がった
--------------------------------------------------

* データだけを持ち、ロジックを持たないクラス
* プログラミング言語の文法的には誤っていない
* **オブジェクト指向のクラスの使い方として誤り**

読書会で #増田本 とのつながりに気づけたから書けました 🏃‍♂️(= `@skip`)
----------------------------------------------------------------------

* Pythonの標準ライブラリには `dataclasses` があるんです
* 拙ブログ `dataclassデコレータを使ったクラスが #ミノ駆動本 でいう「データクラス」になるかは、プログラマ次第 <https://nikkie-ftnext.hatenablog.com/entry/dataclass-decorator-is-anti-pattern-or-not>`_

明日です！ ミノ駆動さん × 増田さん 🏃‍♂️
--------------------------------------------------

* 6/30 `BPStudy#178〜成長し続け、変更を楽に安全にできるソフトウェア設計とは <https://bpstudy.connpass.com/event/250694/>`_
* 相性のいい2冊の本、著者が共演！！

2.不変がないPythonで値オブジェクトどうすればいいんだ？
============================================================

読書会で深まった理解

値オブジェクト
--------------------------------------------------

* 「値を **クラス（型）として表現** する設計パターン」（#ミノ駆動本 3章 p.77）
* 「値を扱うための専用クラスを作るやり方」（#増田本 1章 Kindle の位置No.687）

  * 「値オブジェクトを **不変** にする」（#増田本 1章 Kindle の位置No.727）

Pythonで実装例：金額を表すクラス
--------------------------------------------------

.. code:: python

    @dataclass(frozen=True)
    class Money:
        amount: int
        currency: str

        def __post_init__(self):
            if self.amount < 0:
                raise ValueError("金額が0以上でありません。")

        def __add__(self, other: Money) -> Money:
            if not isinstance(other, Money):
                return NotImplemented
            if self.currency != other.currency:
                raise ValueError("通貨単位が違います。")
            added = self.amount + other.amount
            return self.__class__(added, self.currency)

#ミノ駆動本 3章を参考にしました（`ソースコード <https://github.com/ftnext/exile-of-the-wicked-py/blob/92a81a564ec01bba7d0e67da447848a86c83d2d5/chapter3/dataclass_version.py>`_）

.. doctestを通すためのコード
    >>> from dataclasses import dataclass
    >>> @dataclass(frozen=True)
    ... class Money:
    ...     amount: int
    ...     currency: str
    ...     def __post_init__(self):
    ...         if self.amount < 0:
    ...             raise ValueError("金額が0以上でありません。")
    ...     def __add__(self, other):
    ...         if not isinstance(other, Money):
    ...             return NotImplemented
    ...         if self.currency != other.currency:
    ...             raise ValueError("通貨単位が違います。")
    ...         added = self.amount + other.amount
    ...         return self.__class__(added, self.currency)

不変です💰
--------------------------------------------------

.. code-block:: python

    >>> yukichi = Money(10_000, "¥")
    >>> yukichi.amount = 1_000_000
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 4, in __setattr__
    dataclasses.FrozenInstanceError: cannot assign to field 'amount'

属性に再代入できません

あれ、不変じゃない😱
--------------------------------------------------

.. code-block:: python

    >>> object.__setattr__(yukichi, "amount", -1_000_000)
    >>> yukichi
    Money(amount=-1000000, currency='¥')

マイナス百万円爆誕！！💥

IMO：実装 and **コミュニケーション**
--------------------------------------------------

* Pythonには不変はない（みたい） 例： `object.__setattr__`
* 「不変が前提の値オブジェクトを変更したい」と考えるということは、 **何かがうまくいっていない** のでは？
* 大元の問題を特定し解決するために、コミュニケーションを取ろう

.. ref: https://twitter.com/ftnext/status/1537780337559818240

まとめ🌯 1人で、みんなで、ミノ駆動本で学ぶオブジェクト指向
============================================================

* ミノ駆動本の読書会（Python使い視点）を開いてます（次回は `7/1(金) 条件分岐 <https://pythonista-books.connpass.com/event/251790/>`_）
* 読もう、ミノ駆動本 & 開いてみよう、読書会

読書会で得た学びを共有
--------------------------------------------------

* アウトプットして学ぶ & 他の方のアウトプットがインプットとなって学ぶ
* #ミノ駆動本 × #増田本 、 **合わせ読み** で理解深まる
* Pythonに不変はないが、値オブジェクトはできる 👉 思うに鍵はコードの外の **コミュニケーション**

ご清聴ありがとうございました
--------------------------------------------------

これまでの読書py参加者の皆さまに感謝申し上げます

今後ともよろしくお願いします（ウェルカムカモーン）

EOF
============================================================
