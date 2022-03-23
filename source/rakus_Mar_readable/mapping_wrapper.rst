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

.. code-block:: json

    [
      {"id": "0606", "name": "shion", "favorite": null},
      {"id": "1231", "name": "satomi", "favorite": "抹茶アイス"},
      {"id": "0410", "name": "toma", "favorite": "干物"},
      {"id": "1120", "name": "gocchan", "favorite": "ポテチ"},
      {"id": "0708", "name": "aya", "favorite": "ナタデココ"},
      {"id": "0309", "name": "thunder", "favorite": "きな粉餅"},
    ]

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

IDを使って別の値を照合
--------------------------------------------------

* 別のデータには ``id`` だけが含まれる
* ``id`` に対応する ``name`` を知りたい
* 💡 ``id`` をキー、 ``name`` を値とする **辞書** を作ろう

``id`` をキー、 ``name`` を値とする辞書を作る
--------------------------------------------------

.. code-block:: python

    >>> id_to_name = {}  # 空の辞書で初期化
    >>> for obj in data:  # dataは先ほどの「加工したいデータ」
    ...     id_to_name[obj["id"]] = obj["name"]
    >>> id_to_name["1231"]
    'satomi'

スクリプトに書く
--------------------------------------------------

.. code-block:: python

    # ... 省略 ...

    id_to_name = {}
    for obj in data:
        id_to_name[obj["id"]] = obj["name"]
    # id_to_name を使った処理が続く

    # ... 省略 ...

読みやすく：辞書を作る処理を関数に切り出す
--------------------------------------------------

.. code-block:: python

    def create_mapping(data):
        id_to_name = {}
        for obj in data:
            id_to_name[obj["id"]] = obj["name"]
        return id_to_name

    # ... 省略 ...

    id_to_name = create_mapping(data)
    # id_to_name を使った処理が続く

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

    def create_room_id_name_map(room_data):
        return {d["id"]: d["name"] for d in room_data}
    
    data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    room_id_name_map = create_room_id_name_map(data["rooms"])

    # data["sessions"]からトークの情報を構築
    # roomIdに対応するroom nameを取得: room_id_name_map[session["roomId"]]

実装してみての気持ち
--------------------------------------------------

* ``room_id_name_map`` のようにいくつもの辞書を書いた
* ``id`` に対応する値を取り出すための辞書を、スクリプトのメインの処理で取り扱う必要はないのでは
* 辞書を隠せればコードがスッキリしそう

辞書を多用していたスクリプト
--------------------------------------------------

.. code-block:: python

    data = fetch_from_sessionize()
    room_id_name_map = create_room_id_name_map(data["rooms"])
    speaker_id_map = create_speaker_id_map(data["speakers"])

    # data["sessions"]からトークの情報を構築
    # room_id_name_mapやspeaker_id_mapを使い、それぞれのIDから値を取り出す

辞書をオブジェクトに隠した実装
========================================

.. code-block:: python

    data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    # Before: speaker_id_map = create_speaker_id_map(data["speakers"])
    speaker_factory = SpeakerFactory.from_(data["speakers"])

    # data["sessions"]からトークの情報を構築するコードの一部抜粋
    # Before: [speaker_id_map[speaker_id] for speaker_id in session["speakers"]]
    [speaker_factory.create(speaker_id) for speaker_id in session["speakers"]]

``SpeakerFactory``
--------------------------------------------------

.. code-block:: python

    class SpeakerFactory:
        def __init__(self, id_to_raw_data_map):
            # インスタンス変数として、辞書を持つ（ラップしている）
            self._id_to_raw_data_map = id_to_raw_data_map

``SpeakerFactory``
--------------------------------------------------

.. .. revealjs-break::

.. code-block:: python

    class SpeakerFactory:
        # __init__ （前スライド）

        @classmethod
        def from_(cls, speakers_raw_data) -> SpeakerFactory:
            """APIの返り値からSpeakerFactoryを作るメソッド（辞書を作ってから初期化する）"""
            id_to_raw_data_map = {data["id"]: data for data in speakers_raw_data}
            return cls(id_to_raw_data_map)

``SpeakerFactory``
--------------------------------------------------

.. .. revealjs-break::

.. code-block:: python

    class SpeakerFactory:
        # __init__
        # from_

        def create(self, speaker_id: str) -> Speaker:
            """speaker_idに対応するSpeakerオブジェクトを返す"""
            speaker_data = self._id_to_raw_data_map[speaker_id]
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
