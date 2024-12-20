# Rediscogs - PyQt6 based client for scraping Discogs Database

Example image of the GUI.
![Example Image](https://github.com/gkanba/Rediscogs/blob/master/examples/example_1.png)
Example output of the text file.
![Example Text](https://github.com/gkanba/Rediscogs/blob/master/examples/example_2.png)

## 概要

検索した該当リリースの情報をまとめて表示し、任意のテキストファイルとして保存できます。LP / VinylやCD等のデータ整理において、毎回Discogs(https://www.discogs.com/) で検索したデータをテキストファイルにコピーしてくるのが大変だったため作成しました。個人利用に限りご自由にご使用ください。また本プログラムを利用したことによるいかなる問題について著作者は責任を負いません。

## 対応検索フォーマット

以下の多重検索条件に対応しています。 最低一つから検索できますが、趣味程度の作りでコードが堅牢でないため"Love"等の普遍的なTitleのみで検索するとrequestが終了しない問題があります(Discogs APIのrequest制限により永遠に検索が終了しないため)。できる限り検索条件を絞れるように条件を設定してご利用ください。
(これはDiscogs APIのrate limittingが原因で、修正可能ではあるがそもそも検索結果が多量になってしまうような検索をかけないほうがよい)

+ Catalog No.         (カタログナンバー : 基本的にこれがわかればほかの条件は必要ありません)
+ Release Title       (タイトル : 五万とある重複タイトルに注意)
+ Release Artist      (アーティスト名 : 検索が絞れない際に使用)
+ Release Country     (リリース国名 : 同名盤等の国を絞る際に使用)
+ Release Year        (リリース年 : 同名盤 (Remaster) 等のリリース年を絞るのに使用)

## 動作環境

Windows 10/11 (using exe file)

or

python3.12 with libraries (directly run rediscogs.py)
+ PyQt6                    (https://www.riverbankcomputing.com/software/pyqt/)
+ python3-discogs-client   (https://github.com/joalla/discogs_client)
+ urllib                   (https://docs.python.org/3/library/urllib.html)

## 使用リソース

Fonts : Iosevka Nerd Font, Sarasa J Nerd Font

Free Web Icons : https://www.flaticon.com/ 
