# Day_07_14_JSON.py
import json
import requests

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
print(received.text)

origin = received.content
print(origin)
print(type(origin))

text = bytes.decode(origin, encoding='utf-8')
print(type(text))
# {"code":"11","value":"서울특별시"},
# {"code":"26","value":"부산광역시"},
# {"code":"27","value":"대구광역시"},
# {"code":"28","value":"인천광역시"},
# {"code":"29","value":"광주광역시"},
# {"code":"30","value":"대전광역시"},
# {"code":"31","value":"울산광역시"},
# {"code":"41","value":"경기도"},
# {"code":"42","value":"강원도"},
# {"code":"43","value":"충청북도"},
# {"code":"44","value":"충청남도"},
# {"code":"45","value":"전라북도"},
# {"code":"46","value":"전라남도"},
# {"code":"47","value":"경상북도"},
# {"code":"48","value":"경상남도"},
# {"code":"50","value":"제주특별자치도"}

# 문제
# code와 value에 들어있는 값만 출력하세요

for item in json.loads(text):
    print(item["code"], item["value"])
print('-'*50)
items = json.loads(text)

print([(i['code'], i['value']) for i in items])