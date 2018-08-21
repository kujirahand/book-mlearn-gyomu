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
        "name":"太宰 治",
        "url":"https://www.aozora.gr.jp/cards/000035/files/"}, 
     "books":[
        {"name":"斜陽","zipname":"1565_ruby_8220.zip"},
        {"name":"走れメロス","zipname":"1567_ruby_4948.zip"},
        {"name":"津軽","zipname":"2282_ruby_1996.zip"},
        {"name":"お伽草紙","zipname":"307_ruby_3042.zip"},
        {"name":"人間失格","zipname":"301_ruby_5915.zip"},
    ]},
    {"auther":{
        "name":"夏目 漱石",
        "url":"https://www.aozora.gr.jp/cards/000148/files/"}, 
     "books":[
        {"name":"吾輩は猫である","zipname":"789_ruby_5639.zip"},
        {"name":"坊っちゃん","zipname":"752_ruby_2438.zip"},
        {"name":"草枕","zipname":"776_ruby_6020.zip"},
        {"name":"虞美人草","zipname":"761_ruby_1861.zip"},
        {"name":"三四郎","zipname":"794_ruby_4237.zip"},
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
        #Zipファイルに含まれるファイルを開く。今回のZIPは一つのテキストファイルのみ含む。
        for filename in zf.namelist():
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
    documents, dm=1, vector_size=300, window=5, min_count=1)

#Doc2Vecの学習モデルを保存
model.save('aozora.model')

print("モデル作成完了")