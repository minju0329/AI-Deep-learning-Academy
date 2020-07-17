class Info:
    # 파이썬에서는 class안에 변수를 생성할 수 없다 ==> 생성자 안에서 생성해야함
    def __init__(self):
        print('init')
        self.age = 12           # class를 생성할때마다 age변수 생성
                                # 단, 멤버 변수를 생성할 때 self.변수명으로 선언해야함

    def show(self):         # 'self' = 자기자신을 의미
        print('show',self.age)
                    # class안에는 멤버함수, 멤버 변수가 들어갈 수있다.

i1 = Info()  # 프로그래밍에서 ()는 함수 호출을 의미 --> 생성자
i2 = Info()
i2.addr = 'jeju'               # 멤버변수를 밖에서 선언 (원래는 생성자에서 생성해야하는데)
print(i1)

i1.show()           # 멤버함수, # .의 왼쪽은 매개변수
#Info.show('abc')    # 'abc'는 적절한 매개변수가 아니다. => error 발생, self.age 변수가 없어서
Info.show(i1)

print(i1.age)