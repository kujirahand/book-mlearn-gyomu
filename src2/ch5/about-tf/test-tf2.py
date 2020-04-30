import tensorflow as tf
sess = tf.Session()
msg  = tf.constant('一握りの憩いは二握りの骨折りに勝る')
print(sess.run(msg).decode('utf-8'))

