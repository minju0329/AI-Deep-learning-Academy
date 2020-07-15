import json
import requests
import re

d = {"ip": "8.8.8.8"}
print(d)
print(d['ip'])

d2 = json.dumps(d)      #dump 파일, dumps 문자열 -> 리스트 형태로 trans
print(d2)
print(type(d2))

d3 = json.loads(d2)     #load 파일, loads 문자열 -> dict 형태로 trans
print(d3)
print(type(d3))
print('-'*50)

# 문제
# dt 변수로부터 값만 뽑아서 출력하세요
dt = '{"time": "03:53:25 AM","milliseconds_since_epoch": 1362196405309,"date": "03-02-2013"}'
dt2 = json.loads(dt)
print(dt2)
print(type(d2))
print(dt2["time"], dt2["milliseconds_since_epoch"], dt2["date"])
print('-'*50)

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'

received = requests.get(url)
origin = received.content

text = bytes.decode(origin, encoding='utf-8')
print(text)
# 문제
# 정규표현식을 사용해서 똑같은 결과를 출력하세요
Code=re.findall(r'[0-9]+',text)
value=re.findall(r'[가-힣]+',text)
print(Code)
print(value)      # 결과는 나오지만 여기서만 사용가능

binds = zip(Code,value)
print(list(binds))

print(re.findall(r'"code":"([0-9]+)"',text))
print(re.findall(r'"value":"([가-힣]+)"',text))
print('-'*50)
# 문제
# code와 value를 한번에 찾으세요
print(re.findall(r'"([0-9가-힣]+)"',text))
print(re.findall(r'"code":"([0-9]+)","value":"([가-힣]+)"',text))
