import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import cv2, glob
import numpy as np

# 画像形式の指定 --- (※1)
in_shape = (50, 50, 3)
nb_classes = 2

# CNNモデル構造を定義 --- (※2)
model = Sequential()
model = Sequential()
model.add(Conv2D(32,
          kernel_size=(3, 3),
          activation='relu',
          input_shape=in_shape))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))

# モデルをコンパイル --- (※3)
model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['accuracy'])

# 画像データをNumpy形式に変換 --- (※4)
x = []
y = []
def read_files(target_files, y_val):
    files = glob.glob(target_files)
    for fname in files:
        print(fname)
        # 画像を読み出し
        img = cv2.imread(fname)
        # 画像サイズを50x50に変換
        img = cv2.resize(img, (50, 50))
        print(img)
        x.append(img)
        y.append(np.array(y_val))

# ディレクトリ内の画像を集める
read_files("imageset/mask_off/*.jpg", [1,0])
read_files("imageset/mask_on/*.jpg", [0,1])
x_train, y_train = (np.array(x), np.array(y))
# テスト用の画像をNumpy形式で得る
x, y = [[], []]
read_files("imageset/mask_off_test/*.jpg", [1,0])
read_files("imageset/mask_on_test/*.jpg", [0,1])
x_test, y_test = (np.array(x), np.array(y))
# データを学習 --- (※5)
hist = model.fit(x_train, y_train,
    batch_size=100,
    epochs=100,
    validation_data=(x_test, y_test))
# データを評価
score = model.evaluate(x_test, y_test, verbose=1)
print("正解率=", score[1], 'loss=', score[0])
# モデルを保存 --- (※6)
model.save('mask_model.h5')
# 学習の様子を描画 --- (※7)
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
