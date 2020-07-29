import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, font_manager, rc



def get_xy_2():                 # 파일 open
    cars = pd.read_csv('../data/cars.csv', index_col=0)
    return cars.speed.values, cars.dist.values

def linear_regression_cars():

    x,y = get_xy_2()

    w = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    ph_x = tf.placeholder(tf.float32)

    hx = w * ph_x + b

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)  # 데이터의 편차가 너무 크기 때문에 줄여준다
    train = optimizer.minimize(loss=loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, feed_dict={ph_x : x})
        print(i, sess.run(loss, {ph_x:x}))

    y_hat0, y_hat1, y_hat2 = sess.run(hx, {ph_x:[0, 30,50]})
    print(y_hat1, y_hat2)
    sess.close()

    # 문제
    # cars.csv 파일을 그래프에 표시하고
    # 위에서 학습한 1차원 방정식을 직선으로 표시하세요
    plt.plot(x, y, 'ro')        # 'ro'를 적으면 빨간색원으로 표시됌
    plt.plot([0,30], [0, y_hat1], 'g')        # 'g'를 적으면 초록색 직선으로 표시됌 #--> 이 코드는 bias가 적용이 안됐음
    plt.plot([0,30], [y_hat0, y_hat1], 'b')   # 'b'를 적으면 파란색 직선으로 표시됌
    plt.show()


linear_regression_cars()