from sklearn import datasets
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()
in_size = 4
nb_classes=3
# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを定義 --- (*1)
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))
# コンパイル --- (*2)
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
# 学習を実行 --- (*3)
model.fit(x, y, batch_size=20, epochs=50)

# モデルを保存 --- (*4)
model.save('iris_model.h5')
# 学習済み重みデータを保存 --- (*5)
model.save_weights('iris_weight.h5')

