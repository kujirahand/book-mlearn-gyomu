import tensorflow as tf
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# アヤメデータの読み込み --- (*1)
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

# アヤメデータをラベルと入力データに分離する
y_labels = iris_data.loc[:,"Name"]
x_data = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

# ラベルデータをone-hotベクトルに直す
labels = {
    'Iris-setosa': [1, 0, 0], 
    'Iris-versicolor': [0, 1, 0], 
    'Iris-virginica': [0, 0, 1]
}
y_nums = np.array(list(map(lambda v : labels[v] , y_labels)))
x_data = np.array(x_data)

# 学習用とテスト用に分割する --- (*2)
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_nums, train_size=0.8)

# モデル構造を定義 --- (*3)
Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(3, activation='softmax')) # ---(*3a)

# モデルを構築 --- (*4)
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# 学習を実行 --- (*5)
model.fit(x_train, y_train,
    batch_size=20,
    epochs=300)

# モデルを評価 --- (*6)
score = model.evaluate(x_test, y_test, verbose=1)
print('正解率=', score[1], 'loss=', score[0])
