# Day_16_01_DL_basic.py
# import tensorflow as tf         # 1.14.0
import matplotlib.pyplot as plt


def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) ** 2
        c += loss

    return c / len(x)


def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) * x[i]
        c += loss

    return c / len(x)


def show_cost():

    x = [1, 2, 3]
    y = [1, 2, 3]

    print(cost(x, y, w=0))
    print(cost(x, y, w=1))
    print(cost(x, y, w=2))
    print('-' * 30)

    for i in range(-30, 50):
        w = i / 10
        c = cost(x, y, w)
        print(w, c)

        plt.plot(w, c, 'ro')
    plt.show()


def show_gradient():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = 5
    # for i in range(100000):   실무에서는 이렇게 쓴다 --> 무한루프
    for i in range(10):
        c = cost(x, y, w=w)
        g = gradient_descent(x, y, w)
        w -= 0.1 * g
        print(i, c)

show_gradient()


# 문제
# x=5, x=7 인 경우에 대해 y값을 예측하세요

# cost값이 반드시 필요  --> 내가 만든 모델이 정답과 근접한지 아닌지 알아내는 방법