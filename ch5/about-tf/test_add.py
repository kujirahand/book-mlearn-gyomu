# TensorFlowを取り込む --- (*1)
import tensorflow as tf

# 定数を定義 --- (*2)
a = tf.constant(100)
b = tf.constant(30)

# 演算を定義 --- (*3)
add_op = a + b

# セッションを開始する --- (*4)
sess = tf.Session()
res = sess.run(add_op) # 式を評価する
print(res)

