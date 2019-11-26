from Method_of_least_squares import*
import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.figure(figsize=(12, 7))
    file_name = "data/residential_premises.xlsx"
    sheet = "data"
    try:
        number = int(input("Please enter a number: "))

        data = get_data(file_name, sheet)
        U1 = data[0]
        Y1 = data[1]
        coefficients_of_linear_equation1 = least_squares_fit(U1, Y1)
        print("Result:\n\tCoefficient A =", coefficients_of_linear_equation1[1],
              "coefficient B =", coefficients_of_linear_equation1[0])
        plt.plot(U1[1], Y1, 'o', color="royalblue", alpha=0.35, label="data", markersize=4.5)
        plt.plot(U1[1],
                 linear_equation(U1[1], coefficients_of_linear_equation1[1], coefficients_of_linear_equation1[0]),
                 color="royalblue", linewidth=2.2, label="line of best fit")

        some_data = choice(file_name, sheet, number)
        U2 = some_data[0]
        Y2 = some_data[1]
        coefficients_of_linear_equation2 = least_squares_fit(U2, Y2)
        print("Result:\n\tCoefficient A =", coefficients_of_linear_equation2[1],
              "coefficient B =", coefficients_of_linear_equation2[0])
        plt.plot(U2[1], Y2, 'o', color="black", alpha=0.35, label="data", markersize=4.5)
        plt.plot(U2[1],
                 linear_equation(U2[1], coefficients_of_linear_equation2[1], coefficients_of_linear_equation2[0]),
                 color="black", linewidth=1.5, alpha=0.7, label="line of best fit")

        plt.xlabel("\nliving space area", fontsize=14)
        plt.ylabel("price\n", fontsize=14)
        plt.legend(loc='lower right', fontsize=13)
        plt.savefig("chart.jpg", dpi=300)
        plt.show()
    except ValueError:
        print("invalid value")


if __name__ == '__main__':
    main()