import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.optimize import fmin


def get_data(file_name, sheet):
    data = pd.read_excel(file_name, sheet)
    df = pd.DataFrame(data)
    length = np.array(df.values).shape[0]
    column = []
    for item in range(length):
        column.append(df.values[item][0])
    return np.array(column)


def standard_deviation(data):
    return np.std(data)


def mean(data):
    return np.mean(data)


def main():
    file_name = "data/residential_premises.xlsx"
    sheet = "data"
    data = get_data(file_name, sheet)

    m = mean(data)
    s = standard_deviation(data)

    plt.figure()
    plt.plot(data, np.zeros(len(data)), 'bo', alpha=0.1)
    plt.plot(data, stats.norm.pdf(data, m, s), '.')
    plt.figure()
    # plt.hist(data)
    plt.show()


if __name__ == '__main__':
    main()
