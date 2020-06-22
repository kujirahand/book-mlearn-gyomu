from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score

# データを読み込む --- (*1)
digits = datasets.load_digits()
x = digits.images
y = digits.target
x = x.reshape((-1, 64)) # 二次元配列を一次元配列に変換 --- (*2)

# データを学習用とテスト用に分割する --- (*3)
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2)

# データを学習 --- (*4)
clf = svm.SVC()
clf.fit(x_train, y_train)

# 予測して精度を確認する --- (*5)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))
