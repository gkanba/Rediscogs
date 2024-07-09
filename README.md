# Rediscogs - PyQt6 based client for scraping Discogs Database

Example image of the GUI.
![Example Image](https://github.com/gkanba/Rediscogs/blob/master/examples/example_1.png)
Example output of the text file.
![Example Text](https://github.com/gkanba/Rediscogs/blob/master/examples/example_2.png)

## 概要

LP / VinylやCD等のデータ整理において、毎回Discogs(https://www.discogs.com/) で検索したデータをテキストファイルにコピーしてくるのが大変だったため作成しました。 個人利用に限りご自由にご使用ください。 本プログラムを利用したことによるいかなる問題について本作者は責任を負いません。

## 対応検索フォーマット

以下の多重検索条件に対応. 最低一つから検索できますが、趣味程度の作りでコードが堅牢でないため"Love"等の普遍的なTitleのみで検索すると永遠にrequestが終わりません。
(Discogs APIのrate limittingが原因)そのためできる限り検索条件を絞るようにしてご利用ください。

+ Catalog No.         (カタログナンバー : 基本的にこれがわかればほかの条件は必要ありません)
+ Release Title       (タイトル : 五万とある重複タイトルに注意)
+ Release Artist      (アーティスト名 : 検索が絞れない際に使用)
+ Release Country     (リリース国名 : 同名盤等の国を絞る際に使用)
+ Release Year        (リリース年 : 同名盤 (Remaster) 等のリリース年を絞るのに使用)

## 動作環境

python3.12 with libraries
+ PyQt6                    (https://www.riverbankcomputing.com/software/pyqt/)
+ python3-discogs-client   (https://github.com/joalla/discogs_client)
+ urllib                   (https://docs.python.org/3/library/urllib.html)
