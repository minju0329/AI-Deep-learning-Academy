import tensorflow as tf

# 문제
# 피처를 두 개로 늘리세요(공부한 시간, 출석한 일수)
def multiple_regression_1():
    x1 = [1,0,3,0,5]        # 공부한시간
    x2 = [0,2,0,4,0]        # 출석한 일수
    y = [1,2,3,4,5]         # 성적

    w1 = tf.Variable(tf.random_uniform([1]))
    w2 = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    hx = w1 * x1 + w2* x2 + b

    loss_i = (hx-y)**2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()

# 문제
# x1과 x2를 변수 1개로 만드세요
def multiple_regression_2():
    x1 = [[1,0,3,0,5],[0,2,0,4,0]]  # 공부한시간
    y = [1,2,3,4,5]         # 성적

    w1 = tf.Variable(tf.random_uniform([2]))
    b = tf.Variable(tf.random_uniform([1]))


    hx = w1[0] * x1[0] + w1[1]* x1[1] + b

    loss_i = (hx-y)**2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()

# 문제
# bias 없애기
def multiple_regression_3():
    # x1 = [[1,0,3,0,5],[0,2,0,4,0],[1,1,1,1,1]]  # 공부한시간       # pitcher의 수가 많아졌을때, bias가 보이지 않으니까
    # x1 = [[0,2,0,4,0],[1,1,1,1,1],[1,0,3,0,5]]  # 공부한시간
    x1 = [[1,1,1,1,1],[1,0,3,0,5],[0,2,0,4,0]]  # 공부한시간         # bias가 잘보일수 있게 맨 앞에 둔다.
    y = [1, 2, 3, 4, 5]  # 성적

    # bias를 어디에 넣어도 loss가 줄어들면 상관없다
    # bias의 위치는 제일 앞에 위치하는 게 일반적이다

    w = tf.Variable(tf.random_uniform([3]))
    # b = tf.Variable(tf.random_uniform([1]))

    # hx = w1[0] * x1[0] + w1[1]* x1[1] + b
    # hx = w1[0] * x1[0] + w1[1]* x1[1] + w1[2]
    # hx = w1[0] * x1[0] + w1[1]* x1[1] + w1[2]*1
    hx = w[0] * w[0] + w[1]* x1[1] + w[2]*x1[2]


    loss_i = (hx-y)**2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()

# 문제
# hx 연산을 행렬 곱셈으로 바꾸세요 (tf.matmul)
def multiple_regression_4():
    x1 = [[1.0, 1.0, 1.0, 1.0, 1.0],
          [1.0, 0.0, 3.0, 0.0, 5.0],
          [0.0, 2.0, 0.0, 4.0, 0.0]]  # 공부한시간         # bias가 잘보일수 있게 맨 앞에 둔다.
    y = [1, 2, 3, 4, 5]  # 성적

    w = tf.Variable(tf.random_uniform([1,3]))      # x1과 차원을 맞춰준다 [1,3]*[3,5]

    # hx = w[0] * x[0] + w[1] * x1[1] + w[2] * x1[2]
    # hx = w @ x
    # () = [3], [3,5]
    hx = tf.matmul(w,x1)

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()


# 문제
# 3시간 공부하고 4번 출석한 학생과
# 5시간 공부하고 1번 출석한 학생의 성적을 구하세요.(placeholder)
def multiple_regression_5():
    x = [[1.0, 1.0, 1.0, 1.0, 1.0],
          [1.0, 0.0, 3.0, 0.0, 5.0],
          [0.0, 2.0, 0.0, 4.0, 0.0]]  # 공부한시간         # bias가 잘보일수 있게 맨 앞에 둔다.
    y = [1, 2, 3, 4, 5]  # 성적

    w = tf.Variable(tf.random_uniform([1,3]))      # x1과 차원을 맞춰준다 [1,3]*[3,5]
    ph_x = tf.placeholder(tf.float32)

    hx = tf.matmul(w, ph_x)

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        sess.run(train, {ph_x: x})
        print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x:x}))
    # [[1.3266822 2.166874  3.0911415 3.8892953 4.855601 ]]
    print(sess.run(hx, {ph_x: [[1,1],
                               [3,4],
                               [4,1]]}))
    # [[6.716365  4.8991637]]   : 10번 돌렸을 때
    # [[6.972934 4.990508]]     : 100번 돌렸을 때
    # [[7.0 5.0]]               : 1000번 돌렸을때
    sess.close()

# 문제
# 행렬 곱셈에서 w와 x의 위치를 바꾸세요
# 문제
# 3시간 공부하고 4번 출석한 학생과
# 5시간 공부하고 1번 출석한 학생의 성적을 구하세요
def multiple_regression_6():

    x =  [[1.0,1.0,0.0],
          [1.0,0.0,2.0],
          [1.0,3.0,0.0],
          [1.0,0.0,4.0],
          [1.0,5.0,0.0]]
    # (1, 5)
    y = [[1],
         [2],
         [3],
         [4],
         [5]]  # 성적

    w = tf.Variable(tf.random_uniform([3,1]))      # x1과 차원을 맞춰준다 [1,3]*[3,5]
    ph_x = tf.placeholder(tf.float32)

    # (1, 5) = (5, 3)* (3, 1)
    hx = tf.matmul(ph_x, w)


    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        sess.run(train, {ph_x: x})
        print(i, sess.run(loss, {ph_x:x}))

    print(sess.run(hx, {ph_x: [[1, 3, 4],
                               [1, 5, 1]]}))
    sess.close()
    # [[6.260023 ] [5.553002]]      10번 일 때
    # [[6.9773846] [5.9863315]]     100번 일 때
    # [[7.] [5.]]                   1000번 일 때

# multiple_regression_1()
# multiple_regression_2()
# multiple_regression_3()
# multiple_regression_4()
# multiple_regression_5()
multiple_regression_6()