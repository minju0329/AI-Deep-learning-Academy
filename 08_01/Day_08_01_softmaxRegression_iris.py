import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import datasets, svm, model_selection, preprocessing

# 문제 1
# 붓꽃 데이터 파일을 읽어오세요

file = pd.read_csv('../data/iris(150).csv', index_col=0)

# 문제 2
# x, y를 만드세요 (y는 인코딩)

# data = file.values
# le  = preprocessing.LabelEncoder()
# le.fit(file.Species)
# x = data[:,:-1]
# y = le.transform(file.Species)

# answer 2-1
enc = preprocessing.LabelBinarizer()
y = enc.fit_transform(file.Species)
# print(y[:5]) # 150행 5열 만 출력

# df = file.values[:, :-1]
# file.dropna(['Species'])   # na가 붙으면 결측치를 없앰
# x = df.values
# print(x.shape)
# print(x[:3])

# answer 2-2 원본을 바꾸는 코드
file.drop(['Species'], axis=1, inplace=True)
x = file.values
# print(x[:3])

# 문제 3
# 7대 3으로 나눠서 정확도를 구하시오
x = np.float32(x) # [150,4]
y = np.float32(y) # [150,3]

data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data

w = tf.Variable(tf.random_uniform([x.shape[1], 1]))  # 8
b = tf.Variable(tf.random_uniform([1]))

ph_x = tf.placeholder(tf.float32)

z = tf.matmul(ph_x, w) + b
hx = tf.matmul(ph_x, w)

loss_i = tf.nn.sigmoid_cross_entropy_with_logits(labels=y_train, logits=z)
loss = tf.reduce_mean(loss_i)

optimizer = tf.train.GradientDescentOptimizer(0.0001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(100):
    sess.run(train, {ph_x: x_train})

    if i % 10 == 0:
        print(i, sess.run(loss, {ph_x: x_train}))

preds = sess.run(hx, {ph_x: x_test})
preds_1 = (preds.reshape(-1) > 0.5)
y_1 = y_test.reshape(-1)

preds_1 = np.int32(preds_1)
y_1 = np.int32(y_1)

print('acc :', np.mean(preds_1 == y_1))
sess.close()