import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import datasets, svm, model_selection, preprocessing


def show_accuracy(preds, labels):
    preds_arg = np.argmax(preds, axis=1)
    y_arg = np.argmax(labels, axis=1)

    equals = (preds_arg == y_arg)
    print('acc :', np.mean(equals))

def show_accuracy_sparse(preds, labels):
    preds_arg = np.argmax(preds, axis=1)

    equals = (preds_arg == labels)
    print('acc :', np.mean(equals))

# 문제 1
# 붓꽃 데이터 파일을 읽어오세요
def softmax_iris():
    file = pd.read_csv('../data/iris(150).csv', index_col=0)

    enc = preprocessing.LabelBinarizer()  # 0과 1로만 표기
    y = enc.fit_transform(file.Species)

    file.drop(['Species'], axis=1, inplace=True)   # 내가 가진 파일의 Species열이 삭제된다
    x = file.values
    x = np.float32(x)

    data = model_selection.train_test_split(x,y, train_size=0.7)
    x_train, x_test, y_train, y_test = data

    n_features = x.shape[1]
    n_classed = y.shape[1]
    w = tf.Variable(tf.random_uniform([n_features, n_classed]))

    ph_x = tf.placeholder(tf.float32)

    z = tf.matmul(ph_x, w)
    hx = tf.nn.softmax(z)

    loss_i = tf.nn.softmax_cross_entropy_with_logits(labels=y_train, logits=z)
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, {ph_x:x_train})
        print(i, sess.run(loss, {ph_x:x_train}))


    # 문제 4
    # 30%의 데이터에 대해 정확도를 구하시오
    preds_train = sess.run(hx, {ph_x: x_train})
    preds_test = sess.run(hx, {ph_x: x_test})

    show_accuracy(preds_train, y_train)
    show_accuracy(preds_test, y_test)
    sess.close()

def softmax_iris_sparse():
    file = pd.read_csv('../data/iris(150).csv', index_col=0)

    enc = preprocessing.LabelEncoder()  # 0과 1로만 표기
    y = enc.fit_transform(file.Species)

    file.drop(['Species'], axis=1, inplace=True)  # 내가 가진 파일의 Species열이 삭제된다
    x = file.values
    x = np.float32(x)

    data = model_selection.train_test_split(x, y, train_size=0.7)
    x_train, x_test, y_train, y_test = data
    print(y_train.shape, x_train.shape) #(105,)(45,)

    n_features = x.shape[1]
    n_classed = 3
    w = tf.Variable(tf.random_uniform([n_features, n_classed]))
    b = tf.Variable(tf.random_uniform([n_features, n_classed]))         # class의 개수가 bias의 갯수이다.

    ph_x = tf.placeholder(tf.float32)

    z = tf.matmul(ph_x, w)+b
    hx = tf.nn.softmax(z)

    loss_i = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y_train, logits=z)
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, {ph_x: x_train})
        print(i, sess.run(loss, {ph_x: x_train}))

    # # 문제 4
    # # 30%의 데이터에 대해 정확도를 구하시오
    preds_train = sess.run(hx, {ph_x: x_train})
    preds_test = sess.run(hx, {ph_x: x_test})

    show_accuracy_sparse(preds_train, y_train)
    show_accuracy_sparse(preds_test, y_test)

    sess.close()

softmax_iris()
#softmax_iris_sparse()