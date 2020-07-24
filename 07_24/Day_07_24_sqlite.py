import sqlite3

def read_weather():
    f = open('../data/weather.csv','r', encoding='utf-8')

    data = []
    for row in f:
        data.append(row.strip().split(','))

    f.close()
    return data

def insert_row(row):
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()

    #INSERT INTO SUTDENT VALUES()
    base = 'INSERT INTO kma VALUES ("{}","{}","{}","{}","{}","{}","{}","{}")'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cur.execute(query)

    conn.commit()
    conn.close()

# 문제
# 한번에 넣은 함수를 만드세요
def insert_rows(rows):
    conn = sqlite3.connect('../data/weather.sqlite3')
    cur = conn.cursor()

    base = 'INSERT INTO kma VALUES ("{}","{}","{}","{}","{}","{}","{}","{}")'

    for row in rows:
        query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        query = base.format(*row)
        cur.execute(query)
    conn.commit()
    conn.close()


def create_db():
    conn = sqlite3.connect('../data/weather.sqlite3')
    cur = conn.cursor()

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEF TEXT, wf TEXT, tmn TEXT, tmax TEXT, rnSt TEXT)'
    cur.execute(query)

    conn.commit()
    conn.close()

# 문제
# sqlite3을 검색해서 데이터를 읽어오는 쿼리를 추가하세요
def show_db():
    conn = sqlite3.connect('../data/weather.sqlite3')
    cur = conn.cursor()

    query = 'SELECT * FROM kma'     # * : 전체를 의미
    for row in cur.execute(query):
        print(row)

    # rows = [row for row in cur.execute(query)]

    conn.commit()
    conn.close()


#create_db()
#data =read_weather()

# for row in data:
#     insert_row(row)
#
#insert_rows(data)
#
#show_db()

# 문제
# 특정 도시의 데이터를 가져오는 함수를 만드세요
def search_city(City):
    conn = sqlite3.connect('../data/weather.sqlite3')
    cur = conn.cursor()

    query = 'SELECT * FROM kma WHERE city = "{}"'.format(City)     # * : 전체를 의미, 문자열 검색은 반드시 <"{}">필요!
    for row in cur.execute(query):
        print(row)

    conn.commit()
    conn.close()

search_city("부산")
search_city("청주")