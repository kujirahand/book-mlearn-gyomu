from sklearn import datasets, svm
import pickle

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()

# データを学習
clf = svm.SVC()
clf.fit(iris.data, iris.target)

# 学習済みデータを保存
with open('iris.pkl', 'wb') as fp:
    pickle.dump(clf, fp)

