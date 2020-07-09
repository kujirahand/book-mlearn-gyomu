from gensim.models import word2vec
#コーパスの読み込み --- (*1)
sentences = word2vec.Text8Corpus('./wiki_wakati.txt')
#モデルの作成 --- (*2)
model = word2vec.Word2Vec(sentences, sg=0, size=100, window=5, min_count=5)
#モデルの保存 --- (*3)
model.save("./wiki.model")
