import re
def read_2():
    f = open('./data/poem', 'r', encoding='utf-8')

    while True:
        line = f.readline()
        print(line.strip())         # 문자열 양쪽의 공백을 제거 = strip()
        #if len(line) == 0:         # 파이썬에서 쓰는 방식이 아님
        if not line:
            break

    f.close()

def read_3():
    f = open('./data/poem', 'r', encoding='utf-8')

    lines = []
    for line in f:
        #print(line.strip())
        lines.append(line)

    f.close()
    return lines

def read_4():
    with open("./data/poem", 'r', encoding='utf-8') as f:        # with을 쓰면 끝에 : 붙여야함 f는 변수
        for line in f:
            line.strip()

        #f.close()             # with를 쓰면 close안써도 알아서 닫아줌

#read_2()
#read_3()
#read_4()

lines = read_3()

# 문제
# 파일에 들어있는 단어 갯수는 몇 개입니까?

sum = 0
for line in lines:
    #print(line.split(' '))
    sum+=len(line.split(' '))

#====================================
count = 0
for line in lines:
    #print(line)
    words = re.findall(r'[가-힣]+',line)
    count += len(words)

def write():
    f = open('./data/sample.txt', 'w', encoding='utf-8')

    f.write('hello\n')
    f.write('python')

    f.close()

write()