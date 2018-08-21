import tensorflow as tf

# プレースホルダを定義 --- (*1)
a = tf.placeholder(tf.int32, [None, 2])

# ベクトルを二倍にする演算を定義 --- (*2)
two = tf.constant(2)
x2_op = a * two

# セッションを開始 --- (*3)
sess = tf.Session()

# プレースホルダに値をあてはめて実行 --- (*4)
sample_list = [[1, 1], [2, 2], [3, 3], [4, 4]]
res = sess.run(x2_op, feed_dict={ a: sample_list })
print(res)


