import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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


def probability_density(mi, sigma, x):
    return 1 / np.sqrt(2 * np.pi * sigma ** 2) * np.exp(-1 / (2 * sigma ** 2) * (x - mi) ** 2)


data = get_data('data/residential_premises.xlsx', 'data')


def f(w):
    u = w[0]
    s = w[1]
    n = len(data)
    x, x_pow = 0, 0
    for i in range(n):
        x_pow += data[i] ** 2
        x += data[i]
    return -(n * np.log(s * np.sqrt(2 * np.pi)) + 1 / (2 * s ** 2) * (x_pow - 2 * u * x + n * u ** 2))


def neg_f(w):
    return - f(w)


def main():
    # analytical method
    mi = mean(data)
    sigma = standard_deviation(data)
    print('\nanalytical method result:\n\texpected value =', mi, '\n\tstandard deviation =', sigma,
          "\n---------------------------------------------------------")

    # numerical method
    initial_values = 100 * np.random.rand(2)
    optimal_coefficients = fmin(neg_f, initial_values)
    print('\nnumerical method result:\n\texpected value =', optimal_coefficients[0],
          '\n\tstandard deviation =', optimal_coefficients[1])

    # charts
    arguments = np.linspace(min(data), max(data), 1100)
    plt.figure(figsize=(12, 8))
    plt.plot(data, np.zeros(len(data)), 'o', color='royalblue', alpha=0.15, label='data (living space area [m2])')
    plt.plot(arguments, probability_density(optimal_coefficients[0], optimal_coefficients[1], arguments),
             label='normal distribution for data', color='black')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
