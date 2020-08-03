# Day_16_01_DL_basic.py
# import tensorflow as tf         # 1.14.0
import matplotlib.pyplot as plt

def cost(x, y, w,b):
    c = 0
    for i in range(len(x)):
        hx = w * x[i] + b
        loss = (hx - y[i]) ** 2
        c += loss

    return c / len(x)

def gradient_descent(x, y, w, b):
    g0, g1 = 0,0
    for i in range(len(x)):
        hx = w * x[i]+b
        g0=(hx-y[i]) * (x[i])
        g1=(hx-y[i])

    return g0 / len(x), g1/len(x)


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

    w, b = 5, -3
    for i in range(10):
        c = cost(x, y, w=w, b=b)
        g0, g1 = gradient_descent(x, y, w=w, b=b)
        w -= 0.1 * g0
        b -= 0.1 * g1
        print(i, c)

    # 문제
    # w가 1이 되는 코드로 수정하세요 (3가지)

    # 문제
    # x가 5와 7인 경우에 대해 예측하세요
    print('5:', w*5+b)
    print('7:', w*7+b)
show_gradient()


# 문제
# x=5, x=7 인 경우에 대해 y값을 예측하세요

# cost값이 반드시 필요  --> 내가 만든 모델이 정답과 근접한지 아닌지 알아내는 방법