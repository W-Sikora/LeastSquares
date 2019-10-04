import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import inv

def get_data(file_name, sheet):
    data = pd.read_excel(file_name, sheet)
    df = pd.DataFrame(data)
    length = np.array(df.values).shape[0]
    column_0 , column_1, column_2 = ([] for i in range(3))
    for item in range(length):
        column_0.append(1)
        column_1.append(df.values[item][0])
        column_2.append(df.values[item][1])
    return np.array([column_0, column_1]), np.array(column_2)

def least_square_fit(input_matrix, output_matrix):
    return np.dot(inv(np.dot(input_matrix, input_matrix.T)), np.dot(input_matrix, output_matrix.T))

def linear_equation(arguments ,coefficient_A, coefficient_B):
    return coefficient_A * arguments + coefficient_B

def main():
    data = get_data("residential_premises.xlsx", "data")
    U = data[0]
    Y = data[1]
    coefficients_of_linear_equation = least_square_fit(U, Y)
    print("Result:\n\tCoefficient A =", coefficients_of_linear_equation[1],
          "coefficient B =", coefficients_of_linear_equation[0])
    plt.figure(figsize=(12, 7))
    plt.plot(U[1], Y, 'o', color="black", alpha=0.35, label="data", markersize=4.5)
    plt.plot(U[1], linear_equation(U[1], coefficients_of_linear_equation[1], coefficients_of_linear_equation[0]),
             color="royalblue", linewidth=2.2, label="line of best fit")
    plt.xlabel("\nliving space area", fontsize=14)
    plt.ylabel("price\n", fontsize=14)
    plt.legend(loc='lower right', fontsize=13)
    plt.savefig("chart.jpg", dpi=300)
    plt.show()

if __name__ == '__main__':
    main()