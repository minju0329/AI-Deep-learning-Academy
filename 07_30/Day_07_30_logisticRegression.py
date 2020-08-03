import tensorflow as tf
import numpy as np
from sklearn import datasets, model_selection

def logistic_regression():
    x = [[1.,1.,2.],
         [1.,2.,1.],
         [1.,4.,5.],
         [1.,5.,4.],
         [1.,8.,9.],
         [1.,9.,8.]]
    # 위에 두명 탈락, 4명 합격  # x : 3*6 --> y :6*1

    y = [[0.],
         [0.],
         [1.],
         [1.],
         [1.],
         [1.]]

    y = np.float32(y)     # 없으면 밑에서(1-y) 에러발생

    w = tf.Variable(tf.random_uniform([3,1]))  # x1과 차원을 맞춰준다 [1,3]*[3,5]

    # (6*1) = (6*3) @ (3,1)
    # z ==> 결과(y)
    z = tf.matmul(x, w)
    #hx = 1 / (1 + tf.exp(-z))       # ==> sigmoid식
    hx = tf.sigmoid(z)

    #loss_i = y * -tf.log(hx) + (1-y) * -tf.log(1-hx)    # y가 1이면 앞의 식 0이면 뒤의 식
    loss_i = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=z)
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train)
        print(i, sess.run(loss))

    preds = sess.run(hx)
    print(preds)

    preds_1 = (preds.reshape(-1) > 0.5)  # 0.5보다 크면 1에 가까우니까 참, 작으면 거짓
    y_1 = y.reshape(-1)

    print(preds_1)
    print(y_1)

    print('acc:',np.mean(preds_1==y_1))
    sess.close()

# 문제
# iris 데이터에서 2개의 품종을 골라서
# 70%로 학습하고 30%에 대해 예측한 결과를 정확도로 표시하세요
def logistic_regression_iris():
    x, y = datasets.load_iris(return_X_y=True)
    x = x[:,:2]
    y1 = np.reshape(y,(len(y),1))
    print(x.shape, y1.shape)     # (150,2) (150,)

    data = model_selection.train_test_split(x,y, train_size=0.7)
    x_train, x_test, y_train, y_test = data

    w = tf.Variable(tf.random_uniform([x.shape[0], 1]))
    ph_x = tf.placeholder(tf.float32)

    z = tf.matmul(ph_x, w)
    hx = tf.sigmoid(z)

    loss_i = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=z)
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train)
        print(i, sess.run(loss))

    preds = sess.run(hx)
    print(preds)

    preds_1 = (preds.reshape(-1) > 0.5)
    y_1 = y.reshape(-1)

    print(preds_1)
    print(y_1)

    print('acc:', np.mean(preds_1 == y_1))
    sess.close()

logistic_regression_iris()