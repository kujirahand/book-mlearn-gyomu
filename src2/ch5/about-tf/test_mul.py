import tensorflow as tf

# 定数を定義 --- (*1)
a = tf.constant(10)
b = tf.constant(20)
c = tf.constant(30)

# 演算を定義 --- (*2)
mul_op = (a + b) * c

# セッションを開始する --- (*3)
sess = tf.Session()
res = sess.run(mul_op)
print(res)

