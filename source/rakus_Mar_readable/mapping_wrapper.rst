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

本題：こんなシーンありませんか？
========================================

* データの加工
* JSONオブジェクトが入った配列から **辞書** を作りたい
* Pythonの「辞書」は、他の言語では「マッピング」や「連想配列」です

加工したいデータ
--------------------------------------------------

.. code-block:: json

    [
      {"id": "0606", "name": "shion"},
      {"id": "1231", "name": "satomi"},
      {"id": "0410", "name": "toma"},
      {"id": "1120", "name": "gocchan"},
      {"id": "0708", "name": "aya"},
      {"id": "0309", "name": "thunder"},
    ]

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
