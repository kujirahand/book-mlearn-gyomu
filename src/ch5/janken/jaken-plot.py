import tensorflow as tf
import numpy as np
import pickle

# 保存したジャンケンのデータを読み込む 
with open("janken-data.pkl", "rb") as fp:
    data = pickle.load(fp)
(x_train, y_train), (x_test,y_test) = data

# 学習モデルを構築 
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(30, activation='relu', input_dim=2),
  tf.keras.layers.Dense(3, activation='softmax')
])

# モデルをコンパイル
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# モデルの概要を表示 --- (*1)
model.summary()
# 図でモデルを出力 --- (*2)
tf.keras.utils.plot_model(model, to_file='janken-model.png')

# 学習と評価 
model.fit(x_train, y_train, epochs=20)
# テストデータを評価 
model.evaluate(x_test, y_test, verbose=2)


