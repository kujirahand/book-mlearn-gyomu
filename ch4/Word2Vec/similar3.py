import MeCab
from gensim.models import word2vec

#Word2Vecのmodelとmecabの用意
model = word2vec.Word2Vec.load("./wiki.model")
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
tagger.parse("")

#渡されたテキストに含まれる各単語と「至急」の類似度を表示する
def print_emargency(text):
    print(text)
    #渡されたテキストを形態素解析
    node = tagger.parseToNode(text)
    while node is not None:
        #ストップワードを除く
        fields = node.feature.split(",")
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
            #至急との類似度を表示する
            print(model.wv.similarity(node.surface, '至急'))
        node = node.next

print_emargency("PCが起動しなくなりました。急いでいます。")
print_emargency("使い方がよくわかりません。")
