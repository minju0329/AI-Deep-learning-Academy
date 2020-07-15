import re
db = '''
3412    [Bob] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''
# print(db)

finds = re.findall(r'[0-9]+',db)      # 검색할 때는 findall (전부), 따옴표 안에 찾고 싶은 문자를 넣는다
print(finds)                          # [0-9]+ : 숫자를 찾는다(무한대까지) 공백생기면 자름
print('-'*50)
# 문제
# 이름만 찾기
name1 = re.findall(r'[A-z]+',db)       # wrong code
print(name1)

name2 = re.findall(r'[A-Za-z]+', db)    # 맞지만 좋은 코드는 아님
print(name2)

name3 = re.findall(r'[A-Z][a-z]+', db)  # 데이터의 특성을 살린 good code(대문자로 시작하고 뒤에 소문자 여러개)
print(name3)
