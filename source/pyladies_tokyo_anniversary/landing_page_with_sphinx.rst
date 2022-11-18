================================================================================
Sphinxで作るランディングページ
================================================================================

:Event: PyLadies Tokyo - 8周年記念オンラインパーティ
:Presented: 2022/11/19 nikkie

8周年、おめでとうございます！🎂🎂🎂🎂🎂🎂🎂🎂
================================================================================

本編：この話をします
================================================================================

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyconjp?src=hash&amp;ref_src=twsrc%5Etfw">#pyconjp</a><br>Python Boot Campのページ（静的なHTML）は<br>実は今年にっきーがSphinxに移行しました✌️（GitHub Pagesでサーブ）<a href="https://t.co/0QTfwXGxBh">https://t.co/0QTfwXGxBh</a><br><br>📣なんとSphinxでLPが作れちゃうんです！</p>&mdash; nikkie にっきー 🎤10/1 XP祭り 10/14-15 PyCon JP (@ftnext) <a href="https://twitter.com/ftnext/status/1581201590957924353?ref_src=twsrc%5Etfw">October 15, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Python Boot Camp (#pycamp)
================================================================================

* *日本各地での初心者向けPythonチュートリアルイベント*
* 詳しくは https://www.pycon.jp/support/bootcamp.html
* 概要を伝える **ランディングページ** がある

pycampのランディングページについての議論
--------------------------------------------------

    ペライチの仕様が3月28日から変更になり、無料プランは累計10,000PVを超えると有料プランへの切り替えが必要になった（切り替えないとページが強制的に非公開になる）。

2022/03 `一般社団法人PyCon JP Association運営会議#52 <https://www.pycon.jp/committee/meeting/minutes52.html#pycamp-ryu22e>`_ で相談

手を挙げたnikkie氏🙋‍♂️「まかせて！」
--------------------------------------------------

    Sphinxを使ってGitHub Pagesに移すなら、個人的な型があるので、私はやってみたいです (nikkie

ドキュメンテーションツール Sphinx
================================================================================

TODO 補足

* reST (reStructuredText) を書く
* HTMLをビルド
* 作ったHTMLをGitHub Pagesでホスティングする（＝Webに公開）

ランディングページのこの要素、Sphinxでもできるんですか？
================================================================================

ボタン
--------------------------------------------------

TODO 画像

カードの並び
--------------------------------------------------

``sphinx_design`` も使ってできます！
================================================================================

https://github.com/executablebooks/sphinx-design

ボタンできます！
--------------------------------------------------

TODO 書き方と画像入れていく

カードの並びもできます！
--------------------------------------------------

Sphinxのデフォルトテーマ Alabastar
================================================================================

Alabastarは簡単にスタイル変更できます！
--------------------------------------------------

細かいところに **自作Sphinx拡張**
================================================================================

h1, h2の中央寄せ
================================================================================

誰でも更新できる、参加人数の表
================================================================================

外部へのリンクをブラウザの別のタブで開く
================================================================================