import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils.testing import all_estimators

import warnings
warnings.filterwarnings('ignore')

# アヤメデータの読み込み
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

# アヤメデータをラベルと入力データに分離する 
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

# 学習用とテスト用に分離する 
warnings.filterwarnings('ignore')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

# classifierのアルゴリズム全てを取得する --- (*1)
warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter="classifier")

for(name, algorithm) in allAlgorithms:
    # 各アリゴリズムのオブジェクトを作成 --- (*2)
    clf = algorithm()

    # 学習して、評価する --- (*3)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print(name,"の正解率 = " , accuracy_score(y_test, y_pred))