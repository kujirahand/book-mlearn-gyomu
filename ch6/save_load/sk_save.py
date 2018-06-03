from sklearn import datasets, svm
from sklearn.externals import joblib

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()

# データを学習
clf = svm.SVC()
clf.fit(iris.data, iris.target)

# 学習済みデータを保存
joblib.dump(clf, 'iris.pkl', compress=True)

