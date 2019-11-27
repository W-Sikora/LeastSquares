import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def probability_density(mi, sigma, x):
    return (1 / (np.sqrt(2 * np.pi * sigma ** 2))) * np.exp(-(x - mi) ** 2 / 2 * sigma ** 2)


mi = 0
sigma = 3
lin = np.linspace(-5 * sigma, 5 * sigma, 10000)
plt.plot(lin, probability_density(mi, sigma, lin))
plt.show()


def norm(mi, sigma):
    z = np.linspace(mi - 3 * sigma, mi + 3 * sigma, 1100)
    plt.plot(z, stats.norm.pdf(z, mi, sigma))

# plt.figure()
# norm(0, 1)
# norm(0, 3)
# norm(0, 5)
# norm(0, 10)
# plt.show()
#
# plt.figure()
# norm(-1, 3)
# norm(0, 3)
# norm(1, 3)
# norm(5, 3)
# plt.show()
