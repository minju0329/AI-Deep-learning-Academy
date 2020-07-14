# Day_07_14_comprehension.py
import random

a=[]
for i in range(10):
    if i%2:
        a.append(i)

b= [i for i in range(10) if i%2]

print(a)
print(b)

a1 = [random.randrange(100) for _ in range(10)]
a2 = [random.randrange(100) for _ in range(10)]
a3 = [random.randrange(100) for _ in range(10)]

c = [a1, a2, a3]

print([sum(a1) + sum(a2) + sum(a3)])
print(sum(a1) + sum(a2) + sum(a3))
print([sum(i) for i in c])
print(sum([sum(i) for i in c]))             # 2차원 배열 합
print('-'*50)

# 문제
# 2차원 리스트를 1차원으로 만드세요
print(c)
print(a1+a2+a3)
print(list(j for i in c for j in i))
print([j for i in c for j in i])

# 문제
# 2차원 리스트에서 홀수만으로 1차원 리스트를 만드세요
# 2차원 리스트에서 가장 큰 숫자를 찾으세요
print([j for i in c for j in i if j%2])
print(max([j for i in c for j in i]))
print('-'*50)

# 문제(구글 입사)
# 1~10000 사이에 들어있는 8의 갯수는?

def count_8(n):
    c1 = (n%10==8)
    c2 = (n//10%10==8)
    c3 = (n//100%10==8)
    c4 = (n//1000%10==8)

    return c1+c2+c3+c4

print(sum([count_8(i) for i in range(10000)]))
# 문자열 함수를 쓰면 함수를 만들지 않고 찾을 수 있다.
# 문자열 함수 = count / 정수를 str 형변환 해야함
print(sum([str(i).count('8') for i in range(10000)]))
print('-'*50)

#화면에 출력되는 값은 문자열이다.

