import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

in_size = 2 # 身長と体重の二次元
nb_classes = 6 # 体型を6段階に分ける

# MLPモデル構造を定義
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))

# モデルをコンパイル
model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['accuracy'])

model.save('hw_model.h5')
print("saved")