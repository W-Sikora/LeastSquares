import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import inv


def get_data(file_name, sheet):
    data = pd.read_excel(file_name, sheet)
    df = pd.DataFrame(data)
    length = np.array(df.values).shape[0]
    column_0, column_1, column_2 = ([] for i in range(3))
    for item in range(length):
        column_0.append(1)
        column_1.append(df.values[item][0])
        column_2.append(df.values[item][1])
    return np.array([column_0, column_1]), np.array(column_2)


def least_square_fit(input_matrix, output_matrix):
    return np.dot(inv(np.dot(input_matrix, input_matrix.T)), np.dot(input_matrix, output_matrix.T))


def linear_equation(arguments, coefficient_A, coefficient_B):
    return coefficient_A * arguments + coefficient_B


def choice(file_name, sheet, number):
    data = pd.read_excel(file_name, sheet)
    df = pd.DataFrame(data)
    length = np.array(df.values).shape[0]

    array = np.zeros(length)

    for i in range(0, length, 1):
        array[i] = i

    array_choice = np.array(np.random.choice(array, number - 1, replace=False))

    column_0, column_1, column_2 = ([] for i in range(3))
    for i in range(len(array_choice)):
        column_0.append(1)
        column_1.append(df.values[int(array_choice[i])][0])
        column_2.append(df.values[int(array_choice[i])][1])
    return np.array([column_0, column_1]), np.array(column_2)


def main():
    plt.figure(figsize=(12, 7))
    file_name = "data/residential_premises.xlsx"
    sheet = "data"

    data = get_data(file_name, sheet)
    U1 = data[0]
    Y1 = data[1]
    coefficients_of_linear_equation1 = least_square_fit(U1, Y1)
    print("Result:\n\tCoefficient A =", coefficients_of_linear_equation1[1],
          "coefficient B =", coefficients_of_linear_equation1[0])
    plt.plot(U1[1], Y1, 'o', color="royalblue", alpha=0.35, label="data", markersize=4.5)
    plt.plot(U1[1],
             linear_equation(U1[1], coefficients_of_linear_equation1[1], coefficients_of_linear_equation1[0]),
             color="black", alpha=0.8, linewidth=2.2, label="line of best fit")
    plt.xlabel("\nLiving space area [m2]", fontsize=14)
    plt.ylabel("Price [PLN]\n", fontsize=14)
    plt.legend(loc='lower right', fontsize=13)
    plt.show()


if __name__ == '__main__':
    main()
