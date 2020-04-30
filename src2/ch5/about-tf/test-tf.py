import tensorflow as tf
sess = tf.Session()
hello  = tf.constant('Hello')
print(sess.run(hello))

