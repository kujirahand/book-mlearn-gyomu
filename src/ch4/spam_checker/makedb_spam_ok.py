# 全てのテキストを巡回して単語データベースを作成する
import os, glob
import MeCab
import numpy as np
import pickle

# 保存ファイル名
savefile = "./ok-spam.pickle"
# MeCabの準備 --- (*1)
tagger = MeCab.Tagger()
# 変数の準備 --- (*2)
word_dic = {"__id": 0} # 単語辞書
files = [] # 読み込んだ単語データを追加する

# 指定したディレクトリ内のファイル一覧を読む --- (*3)
def read_files(dir, label):
    # テキストファイルの一覧を得る
    files = glob.glob(dir + '/*.txt')
    for f in files:
        read_file(f, label)

# ファイルを読む --- (*4)
def read_file(filename, label):
    words = []
    # ファイルの内容を読む
    with open(filename, "rt", encoding="utf-8") as f:
        text = f.read()
    files.append({
        "label": label,
        "words": text_to_ids(text)
    })

# テキストを単語IDのリストに変換
def text_to_ids(text):
    # 形態素解析 --- (*5)
    word_s = tagger.parse(text)
    words = []
    # 単語を辞書に登録 --- (*6)
    for line in word_s.split("\n"):
        if line == 'EOS' or line == '': continue
        word = line.split("\t")[0]
        params = line.split("\t")[4].split("-")
        hinsi = params[0] # 品詞
        hinsi2 = params[1]  if len(params) > 1 else '' # 品詞の説明
        org = line.split("\t")[3]  # 単語の原型
        # 助詞・助動詞・記号・数字は捨てる --- (*7)
        if not (hinsi in ['名詞', '動詞', '形容詞']): continue
        if hinsi == '名詞' and hinsi2 == '数詞': continue
        # 単語をidに変換 --- (*8)
        id = word_to_id(org)
        words.append(id)
    return words

# 単語をidに変換 --- (*9)
def word_to_id(word):
    # 単語が辞書に登録されているか？
    if not (word in word_dic):
        # 登録されていないので新たにIDを割り振る
        id = word_dic["__id"]
        word_dic["__id"] += 1
        word_dic[word] = id
    else:
        # 既存の単語IDを返す
        id = word_dic[word]
    return id

# 単語の頻出頻度のデータを作る --- (*10)
def make_freq_data_allfiles():
    y = []
    x = []
    for f in files:
        y.append(f['label'])
        x.append(make_freq_data(f['words']))
    return y, x

def make_freq_data(words):
    # 単語の出現回数を調べる
    cnt = 0
    dat = np.zeros(word_dic["__id"], 'float')
    for w in words:
        dat[w] += 1
        cnt += 1
    # 回数を出現頻度に直す --- (*11)
    dat = dat / cnt
    return dat

# ファイルの一覧から学習用のデータベースを作る
if __name__ == "__main__":
    read_files("ok", 0)
    read_files("spam", 1)
    y, x = make_freq_data_allfiles()
    # ファイルにデータを保存
    pickle.dump([y, x, word_dic], open(savefile, 'wb'))
    print("単語頻出データ作成完了")