# 문제
# cars.csv 파일을 학습해서 속도가 30과 50일 때의 제동 거리를 구하세요

import tensorflow as tf
import pandas as pd

def read_csv_():
    f = open('../data/cars.csv', 'r', encoding='utf-8')
    x = []
    y = []
    for line in f:
        x.append((line.strip().split(','))[1])
        y.append((line.strip().split(','))[2])
    f.close()
    return x[1:],y[1:]


def linear_regression_3():
    xx, yy = read_csv_()
    x = []
    y = []
    for i,j in zip(xx, yy):
        x.append(int(i))
        y.append(int(j))

    w = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    ph_x = tf.placeholder(tf.float32)
    #ph_y = tf.placeholder(tf.float32)

    hx = w * ph_x + b

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    train = optimizer.minimize(loss=loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train, feed_dict={ph_x : x})
        #print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x:[30,50]}))

    sess.close()

def get_xy_1():                 # 파일 open
    f = open('../data/cars.csv','r', encoding='utf-8')
    f.readline()            # 헤더를 읽어서 for문에서 제외
    speeds, dists=[],[]
    for line in f:
        item = line.strip().split(',')
        speeds.append(int(item[1]))     # 딥러닝은 숫자만 가능 int형으로 변환
        dists.append(int(item[2]))
    return speeds.values, dists.values

def get_xy_2():                 # 파일 open
    cars = pd.read_csv('../data/cars.csv', index_col=0)
    return cars.speed.values, cars.dist.values

def linear_regression_cars():

    x,y = get_xy_2()
    w = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    ph_x = tf.placeholder(tf.float32)
    #ph_y = tf.placeholder(tf.float32)

    hx = w * ph_x + b

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)  # 데이터의 편차가 너무 크기 때문에 줄여준다
    train = optimizer.minimize(loss=loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        sess.run(train, feed_dict={ph_x : x})
        print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x:[30,50]}))

    sess.close()

linear_regression_cars()