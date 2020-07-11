import urllib.request as req
import zipfile
import os.path 
import MeCab
from gensim import models

#Mecabの初期化
mecab = MeCab.Tagger()
mecab.parse("")

#保存したDoc2Vec学習モデルを読み込み --- (*7)
model = models.Doc2Vec.load('aozora.model')

#分類用のZipファイルを開き、中の文書を取得する --- (*8)
def read_book(url, zipname):
    if not os.path.exists(zipname):
        req.urlretrieve(url, zipname)

    with zipfile.ZipFile(zipname,"r") as zf:
        for filename in zf.namelist():
            with zf.open(filename,"r") as f:
                return f.read().decode("shift-jis")

#引数のテキストを分かち書きして配列にする
def split_words(text):
    node = mecab.parseToNode(text)
    wakati_words = []
    while node is not None:
        hinshi = node.feature.split(",")[0]
        if  hinshi in ["名詞"]:
            wakati_words.append(node.surface)
        elif hinshi in ["動詞", "形容詞"]:
            wakati_words.append(node.feature.split(",")[6])
        node = node.next
    return wakati_words

#引数のタイトル、URLの作品を分類する --- (*9)
def similar(title, url):
    zipname = url.split("/")[-1]
        
    words = read_book(url, zipname)
    wakati_words = split_words(words)
    vector = model.infer_vector(wakati_words)
    print("--- 「" + title + '」 と似た作品は? ---')
    print(model.docvecs.most_similar([vector],topn=3))
    print("")

#各作家の作品を１つずつ分類 --- (*10)
similar("宮沢 賢治:よだかの星",
        "https://www.aozora.gr.jp/cards/000081/files/473_ruby_467.zip")

similar("芥川 龍之介:犬と笛",
        "https://www.aozora.gr.jp/cards/000879/files/56_ruby_845.zip")

similar("ポー エドガー・アラン:マリー・ロジェエの怪事件",
        "https://www.aozora.gr.jp/cards/000094/files/4261_ruby_54182.zip")

similar("紫式部:源氏物語 06 末摘花",
        "https://www.aozora.gr.jp/cards/000052/files/5021_ruby_11106.zip")