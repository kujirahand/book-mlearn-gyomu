import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# アヤメデータの読み込み
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
y_nums = list(map(lambda v : labels[v] , y_labels))

# 学習用とテスト用に分離する
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_nums, train_size=0.8)

# アヤメデータの入力値(4次元)と出力値(3次元)を入れる場所を定義
x  = tf.placeholder(tf.float32, [None, 4])
y_ = tf.placeholder(tf.float32, [None, 3])

# 重みとバイアスのための変数を定義
w = tf.Variable(tf.zeros([4, 3])) # 重み
b = tf.Variable(tf.zeros([3])) # バイアス

# ソフトマックス回帰を定義
y = tf.nn.softmax(tf.matmul(x, w) + b)

# モデルを訓練する
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
optimizer = tf.train.AdamOptimizer(0.05)
train = optimizer.minimize(cross_entropy)

# 正解率を求める
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# 変数を初期化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 変数を初期化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 学習を行う
train_feed_dict = {x: x_train, y_: y_train}
for step in range(300):
    sess.run(train, feed_dict=train_feed_dict)

# テストデータで最終的な正解率を求める
acc = sess.run(accuracy, feed_dict={x: x_test, y_: y_test})
print("正解率=", acc)
