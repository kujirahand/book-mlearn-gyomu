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
data = pickle.load(open(data_file, "rb"))
word_dic = data[2]
# MeCabの準備
tagger = MeCab.Tagger()
# 学習済みモデルを読み出す --- (※3) 
model = pickle.load(open(model_file, "rb"))

# テキストがスパムかどうか判定する --- (※4)
def check_spam(text):
    # テキストを単語IDのリストに変換し単語の頻出頻度を調べる
    zw = np.zeros(word_dic['__id'])
    count = 0
    s = tagger.parse(text)
    # 単語毎の回数を加算 --- (※5)
    for line in s.split("\n"):
        if line == "EOS": break
        org =  line.split("\t")[3]# 単語の原型
        if org in word_dic:
            id = word_dic[org]
            zw[id] += 1
            count += 1
    zw = zw / count #  --- (※6)
    # 予測
    pre = model.predict([zw])[0] #  --- (※7)
    print("- 結果=", label_names[pre])

if __name__ == "__main__": #  --- (※8)
    check_spam(test_text1)
    check_spam(test_text2)