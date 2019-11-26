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


data = get_data('data/residential_premises.xlsx', 'data')


def f(w):
    u = w[0]
    s = w[1]
    N = len(data)
    x, x_pow = 0, 0
    for i in range(N):
        x_pow += data[i] ** 2
        x += data[i]
    return -(N * np.log(s * np.sqrt(2 * np.pi)) + 1 / (2 * s ** 2) * (x_pow - 2 * u * x + N * u ** 2))


def neg_f(w):
    return - f(w)


def main():
    initial_values = 100 * np.random.rand(2)
    optimal_coefficients = fmin(neg_f, initial_values)
    print('Result:\n\texpected value =', optimal_coefficients[0], '\n\tstandard deviation =', optimal_coefficients[1])
    plt.figure(figsize=(12, 9))
    plt.plot(data, np.zeros(len(data)), 'ob', alpha=0.1, label='data (living space area [m2])')
    plt.plot(data, stats.norm.pdf(data, optimal_coefficients[0], optimal_coefficients[1]), '.k',
             label='normal distribution of data')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
