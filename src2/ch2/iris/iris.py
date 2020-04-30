import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# アヤメデータの読み込み --- (*1)
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

# アヤメデータをラベルと入力データに分離する --- (*2)
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

# 学習用とテスト用に分離する --- (*3)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

# 学習する --- (*4)
clf = SVC()
clf.fit(x_train, y_train)

# 評価する --- (*5)
y_pred = clf.predict(x_test)
print("正解率 = " , accuracy_score(y_test, y_pred))