from gensim.models import word2vec
model = word2vec.Word2Vec.load("./wiki.model")
results = model.wv.most_similar(positive=['王','女'], negative=['男'])
for result in results:
    print(result)
