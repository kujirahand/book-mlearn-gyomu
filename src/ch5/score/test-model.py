import numpy as np
import cv2, pickle
from sklearn.model_selection import train_test_split
import keras

# データファイルと画像サイズの指定 --- (*1)
data_file = "./png-etl1/katakana.pickle"
im_size = 25
in_size = im_size * im_size
out_size = 46 # ア-ンまでの文字の数

# 保存した画像データ一覧を読み込む --- (*2)
data = pickle.load(open(data_file, "rb"))

# 画像データを0-1の範囲に直す --- (*3)
y = []
x = []
for d in data:
    (num, img) = d
    img = img.reshape(-1).astype('float') / 255
    y.append(keras.utils.to_categorical(num, out_size))
    x.append(img)
x = np.array(x)
y = np.array(y)

# 学習用とテスト用に分離する --- (*4)
x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

# モデル構造を定義 --- (*5)
Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(out_size, activation='softmax'))

# モデルをコンパイルして学習を実行 --- (*6)
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
model.fit(x_train, y_train,
    batch_size=20, epochs=50, verbose=1,
    validation_data=(x_test, y_test))

# モデルを評価 --- (*7)
score = model.evaluate(x_test, y_test, verbose=1)
print('正解率=', score[1], 'loss=', score[0])

