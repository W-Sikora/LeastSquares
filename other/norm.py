import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def probability_density_function_of_normal_distribution(mi, sigma, x):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mi) ** 2 / 2 * sigma ** 2)


def norm(mi, sigma):
    z = np.linspace(mi - 3 * sigma, mi + 3 * sigma, 1100)
    plt.plot(z, stats.norm.pdf(z, mi, sigma))


plt.figure()
norm(0, 1)
norm(0, 3)
norm(0, 5)
norm(0, 10)
plt.show()

plt.figure()
norm(-1, 3)
norm(0, 3)
norm(1, 3)
norm(5, 3)
plt.show()
