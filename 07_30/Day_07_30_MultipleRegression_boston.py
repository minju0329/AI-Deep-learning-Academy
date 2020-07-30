import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import model_selection
# 문제1
# 보스턴 주택가격 파일을 읽어오세요
# excel 파일 읽기

boston = pd.read_excel('../data/BostonHousing.xls')


# 문제2
# 보스턴 데이터를 x, y로 변환하세요.
print(boston.values.shape)

#x = boston.values[:, :-1]   # (506,13)
#y = boston.values[:, -1:]   # (506,1)

y = boston.MEDV.values[:-1]       # (506,)
y = y.reshape(-1,1)          # (506, 1)

x=boston.drop(['MEDV'], axis=1).values[:-1]
print(x.shape, y.shape)

# 문제3
# 보스턴 데이터에서 학습하세요

# 문제4
# 마지막 1개를 제외한 데이터로 학습하고 마지막 1개에 대해 결과를 알려주세요

def test_4():
    x_train, x_test = x[:-1], x[-1:]            # 차원 맞추는 것이 중요 x[-1] : 1차원, x[-1:]: 2차원
    y_train, y_test = y[:-1], y[-1:]

    w = tf.Variable(tf.random_uniform([x.shape[1],1]))      # x1과 차원을 맞춰준다 [1,3]*[3,5]
    ph_x = tf.placeholder(tf.float32)

    # [506,1] = [506, 13] * [13,1]
    hx = tf.matmul(ph_x, w)

    loss_i = (hx - y_train) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.000001)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, {ph_x: x_train})
        print(i, sess.run(loss, {ph_x:x_train}))

    preds = sess.run(hx, {ph_x:x_test})
    print(preds, y_test)

    sess.close()

# 문제5
# 70% 데이터로 학습하고 30% 데이터로 예측하고
# 평균오차를 구하시오
def question_5():
    data = model_selection.train_test_split(x, y, train_size=0.7)
    x_train, x_test, y_train, y_test = data

    w = tf.Variable(tf.random_uniform([x.shape[1], 1]))  # x1과 차원을 맞춰준다 [1,3]*[3,5]
    ph_x = tf.placeholder(tf.float32)

    # [506,1] = [506, 13] * [13,1]
    hx = tf.matmul(ph_x, w)

    loss_i = (hx - y_train) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.000001)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, {ph_x: x_train})
        print(i, sess.run(loss, {ph_x: x_train}))

    preds = sess.run(hx, {ph_x: x_test})
    preds_1 = preds.reshape(-1)
    ytest_1 = y_test.reshape(-1)

    diff = preds_1 - ytest_1
    print(diff[:3])

    diff_abs = np.abs(diff)
    print(diff_abs[:3])

    avg = np.mean(diff_abs)
    print('오차 평균:',avg)
    print('오차 평균: {}달러'.format(int(avg*1000)))
    sess.close()

