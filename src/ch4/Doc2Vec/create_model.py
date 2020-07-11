import zipfile
import os.path
import urllib.request as req
import MeCab
from gensim import models
from gensim.models.doc2vec import TaggedDocument

#Mecabの初期化
mecab = MeCab.Tagger()
mecab.parse("")

#学習対象とする青空文庫の作品リスト --- (*1)
list = [
    {"auther":{
        "name":"宮澤 賢治",
        "url":"https://www.aozora.gr.jp/cards/000081/files/"}, 
     "books":[
        {"name":"銀河鉄道の夜","zipname":"43737_ruby_19028.zip"},
        {"name":"注文の多い料理店","zipname":"1927_ruby_17835.zip"},
        {"name":"セロ弾きのゴーシュ","zipname":"470_ruby_3987.zip"},
        {"name":"やまなし","zipname":"46605_ruby_29758.zip"},
        {"name":"どんぐりと山猫","zipname":"43752_ruby_17595.zip"},
    ]},
    {"auther":{
        "name":"芥川 竜之介",
        "url":"https://www.aozora.gr.jp/cards/000879/files/"}, 
     "books":[
        {"name":"羅生門","zipname":"127_ruby_150.zip"},
        {"name":"鼻","zipname":"42_ruby_154.zip"},
        {"name":"河童","zipname":"69_ruby_1321.zip"},
        {"name":"歯車","zipname":"42377_ruby_34744.zip"},
        {"name":"老年","zipname":"131_ruby_241.zip"},
    ]},
    {"auther":{
        "name":"ポー エドガー・アラン",
        "url":"https://www.aozora.gr.jp/cards/000094/files/"}, 
     "books":[
        {"name":"ウィリアム・ウィルスン","zipname":"2523_ruby_19896.zip"},
        {"name":"落穴と振子","zipname":"1871_ruby_17551.zip"},
        {"name":"黒猫","zipname":"530_ruby_20931.zip"},
        {"name":"群集の人","zipname":"56535_ruby_69925.zip"},
        {"name":"沈黙","zipname":"56537_ruby_70425.zip"},
    ]},
    {"auther":{
        "name":"紫式部",
        "url":"https://www.aozora.gr.jp/cards/000052/files/"}, 
     "books":[
        {"name":"源氏物語 01 桐壺","zipname":"5016_ruby_9746.zip"},
        {"name":"源氏物語 02 帚木","zipname":"5017_ruby_9752.zip"},
        {"name":"源氏物語 03 空蝉","zipname":"5018_ruby_9754.zip"},
        {"name":"源氏物語 04 夕顔","zipname":"5019_ruby_9761.zip"},
        {"name":"源氏物語 05 若紫","zipname":"5020_ruby_11253.zip"},
    ]},
]

#作品リストを取得してループ処理に渡す --- (*2)
def book_list():
    for novelist in list:
        auther = novelist["auther"]
        for book in novelist["books"]:
            yield auther, book
        
#Zipファイルを開き、中の文書を取得する --- (*3)
def read_book(auther, book):
    zipname = book["zipname"]
    #Zipファイルが無ければ取得する
    if not os.path.exists(zipname):
        req.urlretrieve(auther["url"] + zipname, zipname)
    zipname = book["zipname"]
    #Zipファイルを開く
    with zipfile.ZipFile(zipname,"r") as zf:
        #Zipファイルに含まれるファイルを開く。
        for filename in zf.namelist():
            # テキストファイル以外は処理をスキップ
            if os.path.splitext(filename)[1] != ".txt":
                continue
            with zf.open(filename,"r") as f: 
                #今回読むファイルはShift-JISなので指定してデコードする
                return f.read().decode("shift-jis")

#引数のテキストを分かち書きして配列にする ---(*4)
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

#作品リストをDoc2Vecが読めるTaggedDocument形式にし、配列に追加する --- (*5)
documents = []
#作品リストをループで回す
for auther, book in book_list():
    #作品の文字列を取得
    words = read_book(auther, book)
    #作品の文字列を分かち書きに
    wakati_words = split_words(words)
    #TaggedDocumentの作成　文書=分かち書きにした作品　タグ=作者:作品名
    document = TaggedDocument(
        wakati_words, [auther["name"] + ":" + book["name"]])
    documents.append(document)
    
#TaggedDocumentの配列を使ってDoc2Vecの学習モデルを作成 --- (*6)
model = models.Doc2Vec(
    documents, dm=0, vector_size=300, window=15, min_count=1)

#Doc2Vecの学習モデルを保存
model.save('aozora.model')

print("モデル作成完了")