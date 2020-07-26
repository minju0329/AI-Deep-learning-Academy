def f_1(a, b, c):
    print(a, b, c, end='\n')  # end 도 keyword argument


# 함수를 호출하는 첫번재 방법
f_1(1, 2, 3)        # positional
f_1(a=1, b=2, c=3)  # keyword
f_1(c=3, a=1, b=2)  # 매개변수의 순서를 막 변경할 수 있다.
f_1(1, 2, c=3)
# f_1(a=1, 2, c=3)  # error, keyword 는 positional 뒤에


def f_2(a=0, b=0, c=0):
    print(a, b, c, end='\n')


# 문제
# f_2를 호출하는 6가지 코드를 만드세요.
f_2()
f_2(1)
f_2(1, 2)
f_2(1, 2, 3)
f_2(1, b=2, c=3)
f_2(1, 2, c=3)


def f_3(*args):     # 가변인자(매개변수의 개수가 정해져 있지 않다.
    print(args)


# 문제
# f_3를 호출하는 6가지 코드를 만드세요.
f_3()
f_3(1)
f_3(1, '2')
f_3(4, 5, 6)
f_3(1, 'a')

# print(1, 'a', True)
#
# m, n = 1, 2
# print(m, n)
#
k = 1, 2       # packing
print(k)
print(*k)       # unpacking


def f_4(**kwargs):      # 키워드 가변인자
    print(kwargs)


# 문제
# f_4를 호출하는 3가지 코드를 만드세요.
f_4()
f_4(a=1)
f_4(a=1, b=2)