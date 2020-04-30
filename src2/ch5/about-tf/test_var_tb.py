import tensorflow as tf

# 変数を定義 --- (*1)
v = tf.Variable(0, name='v')

# 定数を定義
a = tf.constant(10, name='10')
b = tf.constant(20, name='20')

# 演算を定義 --- (*2)
mul_op = tf.multiply(a, b, name='mul')
assign_op = tf.assign(v, mul_op)

# セッションを開始する --- (*3)
sess = tf.Session()
# 変数への代入を実行
sess.run(assign_op)

# TensorBoardのためにグラフを出力 --- (*4)
tf.summary.FileWriter('./logs', sess.graph)

# 変数の結果を得る --- (*5)
res = sess.run(v)
print(res)


