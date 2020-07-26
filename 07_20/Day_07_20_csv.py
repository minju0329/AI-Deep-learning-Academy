import csv

# 문제
# weather.csv 파일을 읽어서 결과를 반환하세요
def read_csv_1():
    f = open('../data/weather.csv', 'r', encoding='utf-8')
    # rows = []
    # for line in f:
    #     # print(line.strip().split(','))
    #     rows.append(line.strip().split(','))
    rows = [line.strip().split(', ') for line in f]     # for문 사용하지말고 comprehension 사용하기

    f.close()
    return rows


rows = read_csv_1()         # 2차원 배열 형대
#
# # 문제
# # rows를 이전에 출력했던 형태로 출력하시오.
# for row in rows:        # row: list
#     for col in row:     # col: 안에 내용
#         print(col, end='')
#         print()

# def read_csv_2():
#     f = open('../data/weather.csv', 'r', encoding='utf-8')
#
#     rows = []
#     for line in csv.reader(f):
#         rows.append(line)
#
#     f.close()
#     return rows
# #
# # rows = read_csv_1()
# rows = read_csv_2()
