from sklearn import datasets, svm, model_selection, preprocessing
import numpy as np
import pandas as pd

# 문제
# leaf.csv 파일을 읽어서
# 70%의 데이터로 학습하고 30%의 데이터에 대해 예측하세요
# 정확도를 알려주세요

# 1. 판다스로 파일 읽기
# 2. x와 y데이터 만들기
# 3. 학습과 검사 데이터셋으로 분할하기
# 4. 학습하기
# 5. 예측해서 정확도 계산하기


# 1. 판다스로 파일 읽기
leaf = pd.read_csv('../data/leaf.csv')
#print(leaf)

le  = preprocessing.LabelEncoder()
le.fit(leaf.species)


data = leaf.values;

x = data[:, 2:]
y = le.transform(leaf.species)
print(x.shape, y.shape)
print(y[:5])

data = model_selection.train_test_split(x,y,train_size=0.7)
x_train, x_test, y_train, t_test = data

