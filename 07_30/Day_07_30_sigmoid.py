import numpy as np
import matplotlib.pyplot as plt
def sigmoid(z):
    return 1/(1+np.e**-z)       # z = wx + b

print(np.e)

print(sigmoid(-1))  #0.2689414213699951
print(sigmoid(0))   #0.5
print(sigmoid(1))   #0.7310585786300049


# 문제
# -10 ~ 10에 대해 시그모이드 그래프를 그리세요
def plot():
    x = np.arange(-10, 10, 0.2)
    plt.plot(sigmoid(0))
    plt.show()

def sol_plot():
    for z in np.arange(-10,10,0.2):
        s = sigmoid(z)
        plt.plot(z,s,'ro')
    plt.show()

def sol_plot2():
    z=np.arange(-10,10,0.2)
    s = sigmoid(z)
    plt.plot(z,s,'ro')
    plt.show()

def show_logistic():
    def log_a():
        return 'A'

    def log_b():
        return 'B'

    y= 0    # 조건 y=0 or y=1
    print(y * log_a() + (1-y) * log_b())

    y=1
    print(y * log_a() + (1-y) * log_b())

# sol_plot()
# sol_plot2()
show_logistic()