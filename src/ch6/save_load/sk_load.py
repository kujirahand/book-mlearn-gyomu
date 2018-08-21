from sklearn import datasets, svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

# 保存した学習済みデータと分類器を読み込む
clf = joblib.load('iris.pkl')

# アヤメのサンプルデータを読み込み
iris = datasets.load_iris()
# 予測する
pre = clf.predict(iris.data)
# 正解率を調べる
print(accuracy_score(iris.target, pre))

