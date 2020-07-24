import requests
import re


payload = { 'S_PAGENUMBER': 1,
            'S_MB_CD': 'W0726200',
            'S_HNAB_GBN': 'I',
            'hanmb_nm': '권지용',
            'sort_field': 'SORT_PBCTN_DAY',
}

# 문제
# 찾아놓은 지드래곤 페이지로부터 데이터를 가져오세요

url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'   # 페이지 주소 입력
received = requests.post(url, data=payload).text       # post 방식 사용


# get 방식
# https://www.google.com/search?q=청주맛집

# post 방식
# get 방식 사용할 수 없을 때 사용
# 1. 암호화가 필요할 때
# 2. 많은 데이터를 전달할 때
# 3. 폼을 전송할 때

# 문제
# 지드래곤의 노래 제목 등등의 데이터만 출력하세요

data = re.findall(r'<td>([A-Za-z가-힇- ]+)', received)
#print(data)

# 해답
tbody = re.findall(r'<tbody>(.+?)</tbody>',received, re.DOTALL)
# print(len(tbody))
# print(tbody[1])

trs = re.findall(r'<tr>(.+?)</tr>',tbody[1],re.DOTALL)

for tr in trs:
    tds = re.findall(r'<td>(.+)</td>',tr)
    print(tds)