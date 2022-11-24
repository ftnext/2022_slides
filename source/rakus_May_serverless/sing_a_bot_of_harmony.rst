:ogp_title: 「お役立ち Twitter Bot を作りながら学ぶ AWS ドリル」を元に作ったBotを紹介します
:ogp_event_name: rakus_May_serverless
:ogp_slide_name: sing_a_bot_of_harmony
:ogp_description: 2022/05 サーバーレス LT vol.2 LT スライド

================================================================================
「お役立ち Twitter Bot を作りながら学ぶ AWS ドリル」を元に作ったBotを紹介します
================================================================================

アイの歌声を聴かせて応援Botの秘密はね、最後じゃないけど明かされるんだよ
================================================================================

これがシン・タイトル！

:Event: サーバーレス LT vol.2
:Presented: 2022/05/26 nikkie

お前、誰よ（自己紹介）
============================================================

* Python大好き **にっきー**

  * Twitter `@ftnext <https://twitter.com/ftnext>`__ ／ GitHub `@ftnext <https://github.com/ftnext>`__

* 株式会社ユーザベースのデータサイエンティスト（NLPer）

ラクスさんのLT会、お世話になっております
--------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2022_slides/rakus_May_pythontips/superstar.html"
        title="*と**"></iframe>

.. _アイの歌声を聴かせて: https://ainouta.jp/

映画『`アイの歌声を聴かせて`_』🤖🎤🎼
--------------------------------------------------

.. raw:: html

    <iframe width="640" height="480" src="https://ainouta.jp/" title="アイの歌声を聴かせて 公式サイト"></iframe>

アイの歌声を聴かせて
--------------------------------------------------

* SF × 学園 × ミュージカル！
* *最後にきっと、笑顔になれる*
* 面白いから、みんな観て！ 6/10(金)まで `配信 <https://ainouta.jp/ondemand.html>`_ 、7/27(水) `円盤発売 <https://ainouta.jp/bddvd.html>`_

このLTの目的
========================================

- PythonとAWS LambdaでTwitter Bot **簡単** かもと思っていただく
- AWSは独学なので、自分よりも詳しい方から、実装へのフィードバックを得たい
- `アイの歌声を聴かせて`_ を知っていただく（達成）

Python、あんまり使わないんだよなという方へ
--------------------------------------------------

* Pythonに限らない話題（AWSの構成など）を聞いていただければ！
* 本当に簡単だと思うので、Pythonの素振りとして試してみては（またはお使いの言語で書き換えてみては）
* `アイの歌声を聴かせてのおすすめリンク <https://nikkie-ftnext.hatenablog.com/entry/ainouta-music-list>`_ 見ます？

本題へ：こんなTwitter Bot作りました
========================================

その名も `@harmonizer_bot <https://twitter.com/harmonizer_bot>`_

その責務は、『アイの歌声を聴かせて』を応援！
--------------------------------------------------

カウントダウンして応援
--------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">5/26は <a href="https://twitter.com/hashtag/%E3%82%A2%E3%82%A4%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%E8%81%B4%E3%81%8B%E3%81%9B%E3%81%A6?src=hash&amp;ref_src=twsrc%5Etfw">#アイの歌声を聴かせて</a> 公開🎬から210日目です。<br>Blu-ray&amp;DVDリリース📀まで今日を含めてあと62日です(7/27発売。現在予約期間)。<br><br>今日も、元気で、頑張るぞっ、おーっ</p>&mdash; sing_a_bot_of_harmony (@harmonizer_bot) <a href="https://twitter.com/harmonizer_bot/status/1529598200700862467?ref_src=twsrc%5Etfw">May 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

秘密を明かしていきます
--------------------------------------------------

* 秘密1
* 秘密2
* 秘密3

.. include:: aws_drill.rst.txt

.. include:: tweets_per_day.rst.txt

.. include:: development_tips.rst.txt

まとめ🌯 アイの歌声を聴かせて応援Botの秘密はね、最後じゃないけど明かされるんだよ
================================================================================

* AWSドリル（の第1回）を参考に、アイうた応援Botを爆誕させました

  * AWS Lambda
  * Amazon EventBridge

.. revealjs-break::

* eventの種類を変えて、1日複数回ツイートさせています

  * 1つのLambda関数、複数種のevent
  * 入力トランスフォーマー

.. revealjs-break::

* Twitter Bot開発生産性アップtips！

  * ドリルのCloudShellのスクリプトをGitHub Actionsに移植
  * 自動デプロイと開発、アカウントが分かれそう

ご清聴ありがとうございました
------------------------------------------------

あなたの応援したいものにTwitter Botを試してもらえたら嬉しいです（驚くくらい簡単でした！）

EOF
============================================================
