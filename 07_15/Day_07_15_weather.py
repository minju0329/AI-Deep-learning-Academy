import requests
import re

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131'
received = requests.get(url)
#print(received)
#print(received.text)


# 문제
# province를 찾으세요
print(re.findall(r'<province>+',received.text))

temp = re.findall(r'<province>(.+)</province>',received.text)     #'.+'를 사용하면 어떤 글자가 들어가도 찾음, ()를 씌우면 ()안의 글자만 출력됨
print(temp)
print(len(temp))

# 문제
#