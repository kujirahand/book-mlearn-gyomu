import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# データを読み込む
wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8")

# データをラベルとデータに分離 ---(*1)
y = wine["quality"]
x = wine.drop("quality", axis=1)

# 学習用とテスト用に分割する ---(*2)
x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size=0.2)

# 学習する ---(*3)
model = RandomForestClassifier()
model.fit(x_train, y_train)

# 評価する ---(*4)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
print("正解率=", accuracy_score(y_test, y_pred))
