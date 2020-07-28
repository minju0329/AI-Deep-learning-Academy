import tensorflow as tf # 1.14버전
import numpy as np

def lenear_regression_1():
    x = [1,2,3]
    y = [1,2,3]

    w = tf.Variable(5.0)
    b = tf.Variable(-3.0)
    # 5, -3으로 쓰면 에러발생 ==> 파이썬은 가능하지만 tensorflow 객체에서는 성능저하때문에 error

    hx = w * x + b      # (*: multipliy, +:add)
    # hx = tf.add(tf.multiply(w,x),b) #w:스칼라, x:배열  -> 브로드캐스트와 같은 결과 , broadcast가 두번실행
                                    # x 와 hx의 shape의 모양이 같아야 함 --> 정답과 비교할 수 있기때문에

    # loss_i = tf.square(hx-y)        # hx: 배열, y: 배열  --> vector operation, 뺀거에 제곱pip
    loss_i = (hx-y)**2
    loss = tf.reduce_mean(loss_i)   # reduce하면 차원이 축소된다. 3차원-->2차원,  2차원-->1차원, 1차원-->스칼라

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    train = optimizer.minimize(loss=loss)
    # train = tf.train.GradientDescentOptimizer(0.1).minimize(tf.reduce_mean(tf.square(tf.add(tf.multiply(w,x),b)-y))) # reduce_mean 먼저 호출

    sess = tf.Session()             # 객체
    sess.run(tf.global_variables_initializer())   # 이 안에 있는 모든 것들을 초기화

    # 학습
    for i in range(10):
        sess.run(train)
    #    print(i, sess.run(loss))    #loss를 확인해야함

    print(w)
    print(sess.run(w))
    print(sess.run(b))
    print(sess.run(hx))             # 1일때 결과 값, 2일때 결과 값, 3일때 결과 값 : [-0.75118184  1.624198    3.999578  ]
    print(sess.run(loss_i))         # 각각의 정답까지의 거리
    print(sess.run(loss))           # 정답까지의 거리의 평균: loss_i들의 평균값

    # 문제
    # x가 5와 7인 경우에 대해 예측하세요 (2가지)
    # 1. 계산식을 사용
    print(sess.run(w * x + b))
    print(sess.run(w * [1,2,3] + b))

    print('5:', sess.run(w * 5 + b))
    print('7:', sess.run(w * 7 + b))
    print('*:', sess.run(w * [5,7] + b))

    # 2. 계산 결과 이용
    ww, bb = sess.run(w), sess.run(b)
    print(ww,bb)

    print('5:',ww*5+bb)
    print('7:',ww*7+bb)

    sess.close()

def lenear_regression_2():
    x = [1, 2, 3]
    y = [1, 2, 3]

    # tf : 32bit 사용
    # np : 64bit 사용
    # w = tf.Variable(np.float32(np.random.rand(1)))      # np.random.rand(1): 64bit
    # b = tf.Variable(np.float32(np.random.rand(1)))

    w = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    ph_x = tf.placeholder(tf.float32)
    ph_y = tf.placeholder(tf.float32)

    hx = w * ph_x + b                   # x를 change

    loss_i = (hx - ph_y) ** 2           # y를
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    train = optimizer.minimize(loss=loss)    # train = tf.train.GradientDescentOptimizer(0.1).minimize(tf.reduce_mean(tf.square(tf.add(tf.multiply(w,x),b)-y))) # reduce_mean 먼저 호출

    sess = tf.Session()  # 객체
    sess.run(tf.global_variables_initializer())  # 이 안에 있는 모든 것들을 초기화

    # 학습
    for i in range(10):
        sess.run(train, feed_dict={ph_x:x, ph_y:y})
        print(i, sess.run(loss, {ph_x:x, ph_y:y}))

    # 문제
    # x가 5와 7인 경우에 대해 예측하세요
    print('x:5', sess.run(hx, {ph_x:5, ph_y:y}))
    print('x:7', sess.run(hx, {ph_x:7, ph_y:y}))

    print(sess.run(hx, {ph_x:x, ph_y:y}))
    print(sess.run(hx, {ph_x:[5,7], ph_y:y}))

    # 위 두개의 코드에서 틀린 부분 찾기 --> y값을 넣을 필요가 없음
    print(sess.run(hx, {ph_x: x}))
    print(sess.run(hx, {ph_x: [5, 7]}))

    sess.close()

def lenear_regression_3():
    x = [1, 2, 3]
    y = [1, 2, 3]

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
        print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x:x}))
    print(sess.run(hx, {ph_x:[5,7]}))

#lenear_regression_1()
#lenear_regression_2()
lenear_regression_3()
