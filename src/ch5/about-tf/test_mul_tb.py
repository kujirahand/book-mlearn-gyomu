import tensorflow as tf

# 定数を定義 --- (*1)
a = tf.constant(10, name='10')
b = tf.constant(20, name='20')
c = tf.constant(30, name='30')

# 演算を定義 --- (*2)
add_op = tf.add(a, b, name='add')
mul_op = tf.multiply(add_op, c, name='mul')

# セッションを開始する --- (*3)
sess = tf.Session()
res = sess.run(mul_op)
print(res)

# TensorBoardのためにグラフを出力 --- (*4)
tf.summary.FileWriter('./logs', sess.graph)

