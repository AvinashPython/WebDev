import tensorflow
import keras
import os
os.environ["KMP_WARNINGS"] = "FALSE"
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error



def Lin_Reg(ratio, csv, sep, cols, predict):
    data = pd.read_csv(csv, sep= sep)
    data = data[cols]
    X = np.array(data.drop([predict],1))
    Y = np.array(data[predict])

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=ratio)
    coeffs = [[] for _ in range(len(cols))]
    acc, error = [], []
    for i in range(len(x_train) // 10 + 1):
        linear = linear_model.LinearRegression()
        linear.fit(x_train[:(i + 1) * 10], y_train[:(i + 1) * 10])
        y_pred = linear.predict(x_test)
        acc.append(linear.score(x_test, y_test))
        error.append(mean_squared_error(y_test, y_pred))
        # print(acc)
        # X1_coeff.append(linear.coef_[0])
        # X2_coeff.append(linear.coef_[1])
        # X3_coeff.append(linear.coef_[2])
        # X4_coeff.append(linear.coef_[3])
        for i in range(len(linear.coef_)):
            coeffs[i].append(linear.coef_[i])
    Y_num = [(x + 1) * 10 for x in range(len(x_train) // 10 + 1)]

    return [coeffs, acc, error, Y_num]
