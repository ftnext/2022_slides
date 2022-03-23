============================================================
[ドラフト版] 内部状態を保持するオブジェクトで読みやすく
============================================================

:Event: リーダブルコード LT会 - vol.3
:Presented: 2022/03/24 nikkie

お前、誰よ（自己紹介）
========================================

* nikkie（にっきー）
* 好きなもの：Python🐍

  * データサイエンティスト at 株式会社ユーザベース
  * PyCon JP 2021座長でした

.. _技術で(も)支えたPyCon JP 2021: https://nikkie-ftnext.hatenablog.com/entry/pyconjp2021-portfolio

拙ブログ：「`技術で(も)支えたPyCon JP 2021`_」
--------------------------------------------------

    個人的にはスッキリした実装にできたと思っています。（ウェブサイトのタイムテーブル用に、sessionize APIの返り値をパース）

読みやすく（＝リーダブルに）書けた経験を共有します

.. _アイの歌声を聴かせて: https://ainouta.jp/

再度 お前、誰よ
--------------------------------------------------

* 好きなもの：アニメ

  * 『`アイの歌声を聴かせて`_』にドハマリ
  * 📣 面白いから全人類観て！（上映も配信もあります）

先日、登壇より優先しちゃいました😉
--------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">我が名はにっきー、<a href="https://twitter.com/hashtag/%E3%82%A2%E3%82%A4%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%E8%81%B4%E3%81%8B%E3%81%9B%E3%81%A6?src=hash&amp;ref_src=twsrc%5Etfw">#アイの歌声を聴かせて</a> 大好きなデータサイエンティスト！<br>アイうたに出会い、開発ネタが次々浮かんで毎日幸せ！(RT)<br>本日 <a href="https://twitter.com/hashtag/studyhacklt?src=hash&amp;ref_src=twsrc%5Etfw">#studyhacklt</a> にて上記共有予定も、なんと最終上映+監督トークとブッキング！<br>トークだけは見過ごせません！登壇辞退です<br><br>空いた枠を埋めた方に大感謝です🙇‍♂️ <a href="https://t.co/Ikw8hq41VY">https://t.co/Ikw8hq41VY</a></p>&mdash; nikkie にっきー シオンv0.0.1開発中⚒ (@ftnext) <a href="https://twitter.com/ftnext/status/1499300361370099716?ref_src=twsrc%5Etfw">March 3, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

このLTでは
--------------------------------------------------

* APIの返り値（JSON形式）をパースする実装で、スッキリ書けた例を共有します
* コード例はPython🐍です

本題：こんなシーンありませんか？
========================================

* データの加工
* JSONオブジェクトが入った配列から **辞書** を作りたい
* Pythonの「辞書」は、他の言語では「マッピング」や「連想配列」です

単純化すると、2つのプロパティを持つJSON
--------------------------------------------------

.. code-block:: json

    {
      "main_data": [...],
      "items": [...]
    }

``main_data`` プロパティ
--------------------------------------------------

* 配列の要素1つ1つが処理の対象
* ``items`` に関して、 ``item_id`` だけを含む

  * itemのデータを見たいときは ``item_id`` を使って ``items`` プロパティから探す必要がある

``items`` プロパティ
--------------------------------------------------

* itemの **一覧**
* ``main_data`` プロパティから ``item_id`` で参照される

  * ``item_id`` に対応したitemを返せるように実装したい

``items`` プロパティの例：学生を表すデータ
--------------------------------------------------

.. literalinclude:: students.json
    :language: python

単純化のために、プロパティの数を絞っています

💡 ``items`` プロパティの配列から **辞書** を作ろう！
------------------------------------------------------------

* ``main_data`` プロパティのデータを処理する際に、この辞書を使う
* キーに ``item_id`` （ ``main_data`` プロパティで持つ）
* 値は ``item_id`` に対応するitem（ ``items`` プロパティの要素のうち、該当するもの）

.. doctestを通すためのコード
    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class Student:
    ...     name: str
    ...     favorite: str

今回の辞書の値はデータクラスで
--------------------------------------------------

.. code-block:: python

    from dataclasses import dataclass
    @dataclass
    class Student:
        """
        >>> Student("nikkie", "アイの歌声を聴かせて")
        Student(name='nikkie', favorite='アイの歌声を聴かせて')

        """
        name: str
        favorite: str

オブジェクトを操作してほしいデータを入手する想定です

.. doctestを通すためのコード
    >>> import json
    >>> with open("students.json", encoding="utf8") as f:
    ...     data = json.load(f)

``id`` をキー、 ``Student`` インスタンスを値とする辞書を作る
------------------------------------------------------------

.. code-block:: python

    >>> students = {}  # 空の辞書で初期化
    >>> for obj in data:  # dataは先ほどの「学生を表すデータ」
    ...     students[obj["id"]] = Student(obj["name"], obj["favorite"])
    >>> students["1231"]
    Student(name='satomi', favorite='抹茶アイス')

Pythonでは、内包表記で書ける🐍
--------------------------------------------------

.. code-block:: python

    >>> students = {  # for文で作ったのと同様に辞書ができます
    ...     obj["id"]: Student(obj["name"], obj["favorite"])
    ...     for obj in data
    ... }
    >>> students["1231"]
    Student(name='satomi', favorite='抹茶アイス')

for文より内包表記の方が性能がよいと言われます

スクリプトに書く
--------------------------------------------------

.. code-block:: python

    # ... 省略 ...

    students = {
        obj["id"]: Student(obj["name"], obj["favorite"])
        for obj in data
    }
    # students を使った処理が続く

    # ... 省略 ...

読みやすく：辞書を作る処理を関数に切り出す
--------------------------------------------------

.. code-block:: python

    def create_mapping(data):
        return {
            obj["id"]: Student(obj["name"], obj["favorite"])
            for obj in data
        }

    # ... 省略 ...

    students = create_mapping(data)
    # students を使った処理が続く

    # ... 省略 ...

PyCon JP 2021スタッフ活動と辞書
========================================

* タイムテーブルに載せるトークの情報
* sessionizeというサービスのAPIの返り値をパースする
* 例：トークの部屋の情報は、部屋IDから取得する

sessionize APIの返り値
--------------------------------------------------

* https://sessionize.com/api/v2/{endpoint_id}/view/All
* フィールド ``sessions`` , ``speakers``, ``rooms`` などを持つ
* 各フィールドの値は、（先ほど見た）JSONオブジェクトが入った配列

スクリプト
--------------------------------------------------

.. code-block:: python

    def create_speakers(speaker_data):
        return {
            d["id"]: Speaker(d["fullName"], d["bio"])
            for d in speaker_data
        }
    
    data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    speakers = create_speakers(data["speakers"])

    # data["sessions"]からトークの情報を構築
    # speakerのidに対応するnameを取得: speakers[session["speakers"][0]].name

実装してみての気持ち
--------------------------------------------------

* ``speakers`` のようにいくつもの辞書を書いた
* ``id`` に対応する値を取り出すための辞書を、スクリプトのメインの処理で取り扱う必要はないのでは
* 辞書を隠せればコードがスッキリしそう

辞書を多用していたスクリプト
--------------------------------------------------

.. code-block:: python

    data = fetch_from_sessionize()
    rooms = create_rooms(data["rooms"])
    speakers = create_speakers(data["speakers"])

    # data["sessions"]からトークの情報を構築
    # roomsやspeakersを使い、それぞれのIDから値を取り出す

辞書をオブジェクトに隠した実装
========================================

.. code-block:: python

    data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    # Before: speakers = create_speakers(data["speakers"])
    speaker_factory = SpeakerFactory.from_(data["speakers"])

    # data["sessions"]からトークの情報を構築するコードの一部抜粋
    # Before: [speakers[speaker_id] for speaker_id in session["speakers"]]
    [speaker_factory.create(speaker_id) for speaker_id in session["speakers"]]

``SpeakerFactory``
--------------------------------------------------

.. code-block:: python

    class SpeakerFactory:
        def __init__(self, speakers_raw_map: Mapping):
            # インスタンス変数として、辞書を持つ（ラップしている）
            self._speakers = speakers_raw_map

``SpeakerFactory``
--------------------------------------------------

.. .. revealjs-break::

.. code-block:: python

    class SpeakerFactory:
        # __init__ （前スライド）

        @classmethod
        def from_(cls, speakers_raw_data: Sequence) -> SpeakerFactory:
            """APIの返り値からSpeakerFactoryを作るメソッド（辞書を作ってから初期化する）"""
            speakers_raw_map = {data["id"]: data for data in speakers_raw_data}
            return cls(speakers_raw_map)

``SpeakerFactory``
--------------------------------------------------

.. .. revealjs-break::

.. code-block:: python

    class SpeakerFactory:
        # __init__
        # from_

        def create(self, speaker_id: str) -> Speaker:
            """speaker_idに対応するSpeakerオブジェクトを返す"""
            speaker_data = self._speakers[speaker_id]
            return Speaker(speaker_data["fullName"], speaker_data["bio"])

``SpeakerFactory`` に込めた想い
--------------------------------------------------

* 「Speakerの作り方を知っているモノ」（スピーカーのファクトリ）
* スクリプトのメイン処理で持っていた辞書が、 **ファクトリの属性に移った**
* スクリプトが知りすぎていなくてスッキリ！✨（変更する場合も箇所が絞られた）

まとめ🌯：内部状態を保持するオブジェクトで読みやすく
============================================================

* 最初の実装は、スクリプトのメイン処理で辞書を作り、IDに応じたインスタンスを使うというもの
* リファクタリングとして、 **辞書を属性に持つオブジェクト** を定義
* スクリプトのメイン処理で辞書を扱う必要がなくなり、スッキリしたコードになった

ご清聴ありがとうございました
------------------------------------------------
