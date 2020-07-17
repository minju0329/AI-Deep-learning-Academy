
def twice(n):
    return n*2

def proxy(f):
    f(3)            # 함수를 저장하는 이유 ==> 매개변수를 전달하기 위해서
                    # callback 함수 : 직접 호출 하지 않고 대신 호출한다. C언어: 함수 포인터
                    # 이 함수의 잘못된 점 1) 함수의 가치가 없다. '3'을 변경하지 못하니까
                    # 이 함수의 잘못된 점 2) return값이 없다.
def proxy2(f, n):
    return f(n)            # 변수를 받고 값을 return함



print(twice)
print(twice(3))

f = twice           # 함수를 어딘가에 넣어 줄수 있다
print(f(3))         # 함수를 넘겨 받았기 때문에 함수처럼 사용할 수 있다. => 함수를 저장하는 이유는 무엇일까?

print(proxy2(f, 7))

lam = lambda n : n * 2          # 함수를 한줄로 표현할수 있다.
print(lam(7))
print(proxy2(lam, 7))
print(proxy2(lambda n : n * 2, 7))  # lamda함수를 따로 정의하지 않는다. => 한줄짜리 코드를 따로 저장하면 가독성과 성능면에서 좋지 않음
                                    # 매개변수는 : 왼쪽, 함수코드: 오른쪽 , return은 생략되어 있음
print('-' * 50)

# 문제
# 리스트를 오름차순으로 정렬하세요
# 리스트를 내림차순으로 정렬하세요
a = [5,1,9,3]
# a.sort()                  # inplace 정렬
# b = sorted(a)             # 원본 유지
# print(a)
# print(b)

print(sorted(a))
print(sorted(a)[::-1])      # 역정렬
print(sorted(a, reverse = True))

# 문제
# colors를 오름차순, 내림차순으로 정렬하시오
colors = ['Red', 'green', 'blue', 'YELLOW']
print(sorted(colors))
print(sorted(colors, reverse=True))

def make_lower(s):
    return s.lower()            # 대문자 -> 소문자 변환

print(sorted(colors, key=make_lower))   # colors를 대소문자 구분없이 정렬(알파벳순서대로)
print(sorted(colors, key=str.lower))    # 굳이 make_lower 함수 안만들어도 됨
print(sorted(colors, key=lambda s:s.lower()))   # key=함수

# 문제
# colors를 길이순으로 정렬하세요(내림차순)

print(sorted(colors, key=lambda s: len(s),reverse=True))
print(sorted(colors, key=lambda s: -len(s)))
print(sorted(colors, key=len))      # 오름차순



