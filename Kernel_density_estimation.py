import numpy as np
import matplotlib.pyplot as plt
from Maximum_likelihood_estimation import get_data


def kernel(u):
    return 1 / (np.sqrt(2 * np.pi)) * np.exp(-u ** 2 / 2)


def main(h):
    s = 0
    for j in range(len(data)):
        s += kernel((u - data[j]) / h)
    return s


data = get_data('data/residential_premises.xlsx', 'data')
margin = 7
u = np.linspace(min(data) - margin, max(data) + margin, 10000)
# window width
h = np.array([0.4, 1, 1.6])

plt.figure(figsize=(12, 7))
plt.plot(data, np.zeros(len(data)), 'o', color='royalblue', alpha=0.15, label='data (living space area [m2])')
for i in range(len(h)):
    f = 1 / (len(data) * h[i]) * main(h[i])
    plt.plot(u, f, label=h[i])
    plt.legend()
plt.show()
