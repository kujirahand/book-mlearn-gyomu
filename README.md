# すぐに使える！業務で実践できる！Pythonによる AI・機械学習・深層学習アプリのつくり方

このリポジトリは、下記の書籍のサンプルプログラム一覧です。

- 書籍名: すぐに使える!業務で実践できる! PythonによるAI・機械学習・深層学習アプリのつくり方 TensorFlow2対応
- 単行本: 414ページ
- 出版社: ソシム (2020/10/22)
- ISBN-10: 4802612796 (改訂前: 4802611641)
- ISBN-13: 978-4802612791 (改訂前: 978-4802611640)

なお、書籍のAPENDIXに開発環境のセットアップについて、まとめられています。

- 書籍の購入→ http://amzn.to/2HKmTYd (改訂前)→ https://amzn.to/2sWAMrM
- 書籍の正誤表 → https://kujirahand.com/blog/go.php?764

## ソースコードを取得するには？

GitHubを訪問し、画面の右上の緑色のボタン[Code]をクリックし、[Download ZIP]から、最新のソースコードをダウンロードできます。

書籍の最後に第n刷と書かれています。

なお、旧版(Tensorflow1対応版)の場合のソースコードが必要な場合は、[こちら](https://github.com/kujirahand/book-mlearn-gyomu/releases/tag/1.0.0)よりソースコードをダウンロードしてください。

## 対応ライブラリのバージョン

[Ubuntu18.04用のインストールスクリプト](https://github.com/kujirahand/book-mlearn-gyomu/blob/master/src/vagrant/ubuntu-install.sh)を用意しています。

```pip-install.bash
pip install --upgrade scikit-learn==0.22.2.post1
pip install --upgrade opencv-python==4.1.2.30
pip install --upgrade tensorflow-cpu==2.2.0
pip install --upgrade keras==2.4.3
pip install --upgrade flask==1.1.1
pip install --upgrade pydot==1.4.1
pip install --upgrade dlib==19.20.0
```

## リポジトリを取得する場合

Gitでリポジトリを取得する場合、ターミナルで以下のコマンドを実行してください。

```
git clone https://github.com/kujirahand/book-mlearn-gyomu.git
```

## Vagrantで環境を構築する場合 (Windows/Intel Macの場合)

以下、VagrantにUbuntuをセットアップする方法が参考になります。

- [VagrantでUbuntuをセットアップする方法](https://kujirahand.com/blog/go.php?748)

## Apple M1チップ搭載のMacを利用する場合 (2021/11/01追加)

ネイティブ環境にTensorflowなどをインストールすることもできます。こちらは若干インストールに手間がかかりますが、最もマシンの性能を活用できます。今後インストール方法が整備されていくと思いますが、流動的なのでこの方法は本書ではサポート対象外とさせてください。

 - [参考リンク:Apple M1環境のrosettaなしでpandas,numpy,Scikit-learn, matplotlibの使用。](https://qiita.com/cheuora/items/c2111ed4d9956e804100)
 - [参考リンク:M1 Macでディープラーニングしてみる](https://zenn.dev/karaage0703/articles/0ab9e654cfb0ec)

### Dockerイメージを利用して環境を作る

そこで、オススメなのが、Dockerを使う方法です。以下の記事が参考になります。

 - [参考リンク:M1搭載Macでも環境を汚さずにDeep Learningしたい！](https://qiita.com/sonoisa/items/6d6b4a81169397a96dd8)

最初に[DockerのM1 Mac版](https://docs.docker.com/desktop/mac/apple-silicon/)をインストールしてください。

そして、上記の記事にある、イメージを利用させていただきます。

```
# イメージをダウンロード
docker pull sonoisa/deep-learning-coding:pytorch1.6.0_tensorflow2.3.0
# コンテナを開始
cd src
docker run -it -p 8888:8888 -v `pwd`:/src sonoisa/deep-learning-coding:pytorch1.6.0_tensorflow2.3.0
```

Dockerが動き出したら以下のコマンドを実行して必要なソフトウェアをインストールします。または、上記の対応ライブラリより手動でソフトウェアをインストールしてください。

```
cd /src/vagrant
bash docker-install.sh
```





