import pickle
import tensorflow as tf
import numpy as np

# 保存したジャンケンのデータを読み込む
with open("janken-data.pkl", "rb") as fp:
    data = pickle.load(fp)
(x_train, y_train), (x_test,y_test) = data

# 学習モデルを構築
Dense = tf.keras.layers.Dense
Activation = tf.keras.layers.Activation
model = tf.keras.models.Sequential()
model.add(Dense(300, activation='relu', input_dim=2))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='sgd',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# 学習と評価
model.fit(x_train, y_train, epochs=35)
model.evaluate(x_test, y_test, verbose=2)

# 勝負
def predict(a, b):
    hands = {'グー':0, 'チョキ':1, 'パー':2}
    results = ['あいこ', '負け', '勝ち']
    x = np.array([[hands[a], hands[b]]])
    r = model.predict(x)
    print(r)
    print(a, b, results[r[0].argmax()])

predict('グー', 'グー')
predict('チョキ', 'パー')
predict('パー', 'チョキ')


