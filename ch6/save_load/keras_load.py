from sklearn import datasets
import keras
from keras.models import load_model
from keras.utils.np_utils import to_categorical

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()
in_size = 4
nb_classes=3
# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを読込 --- (*1)
model = load_model('iris_model.h5')
# 重みデータを読込 --- (*2)
model.load_weights('iris_weight.h5')

# モデルを評価 --- (*3)
score = model.evaluate(x, y, verbose=1)
print("正解率=", score[1])

