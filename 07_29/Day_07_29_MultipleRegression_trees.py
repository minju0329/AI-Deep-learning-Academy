import pandas as pd
import tensorflow as tf


# 문제
# trees.csv 파일을 읽어서
# girth가 10이고 height가 70일 때와
# girth가 20이고 height가 80일 때의 volume을 구하시오.


def get_xy():                 # 파일 open
    trees = pd.read_csv('../data/trees.csv', index_col=0)
    a = [1.0 for i in range(31)]
    return [a, trees.Girth.values, trees.Height.values], trees.Volume.values

def Multiple_Regression_trees():

    x, y = get_xy()

    w = tf.Variable(tf.random_uniform([1,3]))  # x1과 차원을 맞춰준다 [1,3]*[3,5]
    ph_x = tf.placeholder(tf.float32)

    hx = tf.matmul(w, ph_x)

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)  # 데이터의 편차가 너무 크기 때문에 줄여준다
    train = optimizer.minimize(loss=loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, feed_dict={ph_x : x})
        print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x: [[1, 1],
                               [10.4, 19.4],
                               [70, 80]]}))

    sess.close()

Multiple_Regression_trees()