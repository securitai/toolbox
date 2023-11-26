# import os
# import sys
# os.environ["CUDA_VISIBLE_DEVICES"]="1"
# import tensorflow as tf
# import time

# n = 8192
# dtype = tf.float32
# with tf.device("/gpu:0"):
#     matrix1 = tf.Variable(tf.ones((n, n), dtype=dtype))
#     matrix2 = tf.Variable(tf.ones((n, n), dtype=dtype))
#     product = tf.matmul(matrix1, matrix2)


# # avoid optimizing away redundant nodes
# config = tf.ConfigProto(graph_options=tf.GraphOptions(optimizer_options=tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)))
# sess = tf.Session(config=config)

# sess.run(tf.global_variables_initializer())
# iters = 100

# # pre-warming
# sess.run(product.op)

# start = time.time()
# for i in range(iters):
#   sess.run(product.op)
# end = time.time()
# ops = n**3 + (n-1)*n**2 # n^2*(n-1) additions, n^3 multiplications
# elapsed = (end - start)
# rate = iters*ops/elapsed/10**9
# print('\n %d x %d matmul took: %.2f sec, %.2f G ops/sec' % (n, n,
#                                                             elapsed,
#                                                             rate,))


import tensorflow as tf
import time

n = 8192
dtype = tf.float32

with tf.device("/gpu:0"):
    matrix1 = tf.Variable(tf.ones((n, n), dtype=dtype))
    matrix2 = tf.Variable(tf.ones((n, n), dtype=dtype))
    product = tf.matmul(matrix1, matrix2)

# Avoid optimizing away redundant nodes
# Note: In TensorFlow 2.x, session and config are not needed for eager execution
# So, we can skip these lines

# Pre-warming
product.numpy()

iters = 100

start = time.time()
for i in range(iters):
    product.numpy()
end = time.time()

ops = n**3 + (n-1)*n**2  # n^2*(n-1) additions, n^3 multiplications
elapsed = (end - start)
rate = iters * ops / elapsed / 10**9

print('\n %d x %d matmul took: %.2f sec, %.2f G ops/sec' % (n, n, elapsed, rate))
