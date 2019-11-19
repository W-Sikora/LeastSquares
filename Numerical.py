import numpy as np
import pandas as pd
from scipy import fmin


def get_data(file_name, sheet):
    data = pd.read_excel(file_name, sheet)
    df = pd.DataFrame(data)
    length = np.array(df.values).shape[0]
    column_0, column_1 = ([] for i in range(2))
    for item in range(length):
        column_0.append(df.values[item][0])
        column_1.append(df.values[item][1])
    return np.array([column_0]), np.array([column_1])


# def Q(w, u, y):
#     a = w[0]
#     b = w[1]
#     return (y - (a * u + b)) ** 2
#
#
# data = get_data("data/residential_premises.xlsx", "data")
# u = data[0]
# y = data[1]
# w_0 = np.random.rand(2, 1099)
# w_min = fmin(Q(w_0, u, y), w_0)
# print(w_min)