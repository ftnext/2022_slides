============================================================
辞書を保持するオブジェクトで読みやすく
============================================================

:Event: リーダブルコード LT会 - vol.3
:Presented: 2022/03/24 nikkie

お前、誰よ（自己紹介）
========================================

* Python🐍大好き **にっきー**

  * Twitter `@ftnext <https://twitter.com/ftnext>`_ ／ GitHub `@ftnext <https://github.com/ftnext>`_

* データサイエンティスト🐍 at 株式会社ユーザベース
* ラクスさんの勉強会でたまにLT・実況ツイート

.. _技術で(も)支えたPyCon JP 2021: https://nikkie-ftnext.hatenablog.com/entry/pyconjp2021-portfolio

nikkie as PyCon JP 2021 座長
--------------------------------------------------

* Python Conference JP
* 座長＝開催に責任を持つ人
* 拙ブログ：「`技術で(も)支えたPyCon JP 2021`_」（今日の話題もここから）

.. _アイの歌声を聴かせて: https://ainouta.jp/

nikkie loves アニメ！
--------------------------------------------------

* 『`アイの歌声を聴かせて`_』にドハマリ
* 📣 **面白いから全人類観て！** （ `上映 <https://eigakan.org/theaterpage/schedule.php?t=ainouta>`_ も `配信 <https://ainouta.jp/ondemand.html>`_ もあります）

すみません！登壇より優先しちゃいました😉
--------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">我が名はにっきー、<a href="https://twitter.com/hashtag/%E3%82%A2%E3%82%A4%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%E8%81%B4%E3%81%8B%E3%81%9B%E3%81%A6?src=hash&amp;ref_src=twsrc%5Etfw">#アイの歌声を聴かせて</a> 大好きなデータサイエンティスト！<br>アイうたに出会い、開発ネタが次々浮かんで毎日幸せ！(RT)<br>本日 <a href="https://twitter.com/hashtag/studyhacklt?src=hash&amp;ref_src=twsrc%5Etfw">#studyhacklt</a> にて上記共有予定も、なんと最終上映+監督トークとブッキング！<br>トークだけは見過ごせません！登壇辞退です<br><br>空いた枠を埋めた方に大感謝です🙇‍♂️ <a href="https://t.co/Ikw8hq41VY">https://t.co/Ikw8hq41VY</a></p>&mdash; nikkie にっきー シオンv0.0.1開発中⚒ (@ftnext) <a href="https://twitter.com/ftnext/status/1499300361370099716?ref_src=twsrc%5Etfw">March 3, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

それでは本題：このLTでは
========================================

* APIの返り値（JSON形式）をパースする実装で、 **スッキリ書けた** 例を共有します
* コードはPython🐍です（https://github.com/pyconjp/talks.domain.2021 もどうぞ）
* 1つの実装例の共有です。ちょっとしたことでも **コメント大歓迎** です

加工したいデータ（単純化）
--------------------------------------------------

2つのプロパティを持つJSON

.. code-block:: json

    {
      "main_data": [...],
      "items": [...]
    }

``main_data`` プロパティの配列を加工したい
--------------------------------------------------

* 配列の要素1つ1つは ``item_id`` を含む
* 他にitemの情報はない
* 👉 ``items`` プロパティの配列から該当するitemを探す必要がある

``item_id`` でitemを探すために辞書を作ろう！
--------------------------------------------------

* ``items`` プロパティ＝itemの一覧
* キー（itemの ``id``）と値（item）をペアにする＝ **辞書** （というデータ構造）
* ※Pythonの「辞書」は、他の言語では「マッピング」や「連想配列」です

``items`` プロパティの配列の例
--------------------------------------------------

登壇者（Speaker）を表すデータ

.. literalinclude:: students.json
    :language: python

💡 ``items`` プロパティの配列から **辞書** を作ろう！
------------------------------------------------------------

* キーはitemの ``id``
* 値は ``id`` に対応するitem
* ``main_data`` プロパティのデータの処理で、この辞書を使う（ ``item_id`` で参照）

.. doctestを通すためのコード
    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class Speaker:
    ...     name: str
    ...     profile: str

今回、辞書の値は、Pythonの「データクラス」で実装
--------------------------------------------------

.. code-block:: python

    from dataclasses import dataclass
    @dataclass
    class Speaker:
        """
        >>> Speaker("nikkie", "アイの歌声を聴かせてが好き")
        Speaker(name='nikkie', profile='アイの歌声を聴かせてが好き')

        """
        name: str
        profile: str

インスタンスを操作して、ほしいデータを入手する想定です

.. doctestを通すためのコード
    >>> import json
    >>> with open("students.json", encoding="utf8") as f:
    ...     data = json.load(f)

``id`` をキー、 ``Speaker`` インスタンスを値とする辞書を作る
------------------------------------------------------------

.. code-block:: python

    >>> speakers = {}  # 空の辞書で初期化
    >>> for obj in data:  # dataは先ほどの「登壇者を表すデータ」
    ...     speakers[obj["id"]] = Speaker(obj["fullName"], obj["bio"])
    >>> speakers["1231"]
    Speaker(name='satomi', profile='抹茶アイスが好き')

tips: Pythonでは、内包表記で書ける🐍
--------------------------------------------------

.. code-block:: python

    >>> speakers = {  # for文で作ったのと同様に辞書ができます
    ...     obj["id"]: Speaker(obj["fullName"], obj["bio"])
    ...     for obj in data
    ... }
    >>> speakers["1231"]
    Speaker(name='satomi', profile='抹茶アイスが好き')

for文より内包表記の方が性能がよいと言われます

スクリプトに書く
--------------------------------------------------

.. code-block:: python

    # ... 省略 ...

    speakers = {
        obj["id"]: Speaker(obj["fullName"], obj["bio"])
        for obj in data
    }
    # speakers を使った処理が続く

    # ... 省略 ...

読みやすく：辞書を作る処理を関数に切り出す
--------------------------------------------------

.. code-block:: python

    def create_mapping(data):
        return {
            obj["id"]: Speaker(obj["fullName"], obj["bio"])
            for obj in data
        }

    # ... 省略 ...

    speakers = create_mapping(data)
    # speakers を使った処理が続く

    # ... 省略 ...

実例：PyCon JP 2021スタッフ活動と辞書
========================================

* ウェブサイトの `タイムテーブル <https://2021.pycon.jp/time-table>`_ に載せるデータを作りたい
* `sessionize <https://sessionize.com/>`_ というサービスの **APIの返り値をパース** する
* 例：登壇者の情報は、スピーカーIDから取得する

sessionize APIの返り値
--------------------------------------------------

* https://sessionize.com/api/v2/{endpoint_id}/view/All
* プロパティ ``sessions`` （トーク情報）、 ``speakers`` （登壇者情報）, ``rooms`` （部屋情報）などを持つ

返り値のJSONを加工していく
--------------------------------------------------

各プロパティは、（先ほど見た） **JSONオブジェクトが入った配列**

.. code-block:: json

    {
      "sessions": [... (先のmain_data)],
      "speakers": [... (items その1)],
      "rooms": [... (items その2)],
    }

加工処理の実装 1/2
--------------------------------------------------

.. code-block:: python
    :linenos:

    def create_speakers(speaker_data):
        return {
            d["id"]: Speaker(d["fullName"], d["bio"])
            for d in speaker_data
        }
    
    data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    speakers = create_speakers(data["speakers"])

加工処理の実装 2/2
--------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 3-

    data = fetch_from_sessionize()
    speakers = create_speakers(data["speakers"])  # spaakersは辞書
    rooms = create_rooms(data["rooms"])  # roomsも辞書

    # data["sessions"]からトークの情報を構築
    for session in data["sessions"]:
        # 各sessionはroomやspeakerのIDを持つので、
        # roomsやspeakersを使ってIDに対応する値を取り出す。
        # speakerのidに対応するnameを取得
        main_speaker_name = speakers[session["speakers"][0]].name

実装直後の所感
--------------------------------------------------

* ``speakers`` , ``rooms`` **いくつもの辞書** を書いた
* 💡 ``id`` に対応する値を取り出すための辞書を、 *スクリプトのメイン処理で取り扱う必要はない* のでは
* 👉 **辞書を隠せれば** コードがスッキリしそう

辞書をオブジェクトに隠した実装 1/2
========================================

.. code-block:: diff

     data = fetch_from_sessionize()  # sessionize APIから取得したJSON
    -# 辞書を作る関数
    -speakers = create_speakers(data["speakers"])
    +# 辞書をラップしたオブジェクトを作る
    +speaker_factory = SpeakerFactory.from_(data["speakers"])

辞書をオブジェクトに隠した実装 2/2
--------------------------------------------------

.. code-block:: diff

     # data["sessions"]からトークの情報を構築するコードの一部抜粋
    -# 辞書を使う
    -[speakers[speaker_id] for speaker_id in session["speakers"]]
    +# 辞書をラップしたオブジェクトを使う
    +[speaker_factory.create(speaker_id) for speaker_id in session["speakers"]]

辞書を保持するオブジェクト ``SpeakerFactory``
--------------------------------------------------

.. code-block:: python

    class SpeakerFactory:
        def __init__(self, speakers_raw_map: Mapping):
            # インスタンス変数として、辞書を持つ（ラップしている）
            self._speakers = speakers_raw_map

辞書を保持するオブジェクト ``SpeakerFactory``
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

辞書を保持するオブジェクト ``SpeakerFactory``
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

* 「Speakerの *作り方を知っている* モノ」（スピーカーの *ファクトリ*）
* スクリプトのメイン処理で持っていた辞書が、 **ファクトリの属性に移った**
* スクリプトが知りすぎていなくてスッキリ！✨（変更する場合も箇所が絞られた）

まとめ🌯： **辞書を保持するオブジェクト** で読みやすく
============================================================

* APIが返すJSONのパースのメインの処理で、辞書を扱わなくてよくなり、スッキリした✨
* このオブジェクトに実装したメソッドは2つ

  * APIの返り値から自身のオブジェクトを作るメソッド（``from_``）
  * idに対応するオブジェクトを返すメソッド（``create``）

ご清聴ありがとうございました
------------------------------------------------

1つの実装例にすぎませんので、ちょっとしたことでも **コメント大歓迎** です
