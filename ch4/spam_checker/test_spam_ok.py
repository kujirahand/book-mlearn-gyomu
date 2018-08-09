import pickle
import MeCab
import numpy as np
from sklearn.naive_bayes import GaussianNB

# テストするテキスト --- (※1)
test_text1 = """
会社から支給されているiPhoneの調子が悪いのです。
修理に出すので、しばらくはアプリのテストができません。
"""
test_text2 = """
億万長者になる方法を教えます。
すぐに以下のアドレスに返信して。
"""
# ファイル名
data_file = "./ok-spam.pickle"
model_file = "./ok-spam-model.pickle"
label_names = ['OK', 'SPAM']
# 単語辞書を読み出す --- (※2)
with open(data_file, "rb") as f:
    data = pickle.load(f)
word_dic = data[2]
# MeCabの準備
tagger = MeCab.Tagger()
# 学習済みモデルを読み出す --- (※3)
with open(model_file, "rb") as f:
    model = pickle.load(f)


# テキストがスパムかどうか判定する ---(*4)
def check_spam(text):
    # テキストを単語IDのリストに変換し単語の頻出頻度を調べる
    zw = np.zeros(word_dic['__id'])
    count = 0
    s = tagger.parse(text)
    # 単語毎の回数を加算 --- (※5)
    for line in s.split("\n"):
        if line == "EOS": break
        params = line.split("\t")[1].split(",")
        org = params[6] # 単語の原型
        if org in word_dic:
            id = word_dic[org]
            zw[id] += 1
            count += 1
    zw = zw / count # --- (※6)
    # 予測 --- (※7)
    pre = model.predict([zw])[0]
    print("- 結果=", label_names[pre])

if __name__ == "__main__": # --- (※8)
    check_spam(test_text1)
    check_spam(test_text2)
