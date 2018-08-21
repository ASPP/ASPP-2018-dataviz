# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# Advanced Scientific Programming in Python summer school
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

np.random.seed(123)

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# Clean data
X = np.linspace(15, 21, 100)
Y = gaussian(X, 0.65, 17.6, 1.)

# Noisy dat
Xn = np.random.uniform(16, 20, 25)
Yn = gaussian(Xn, 0.65, 17.6, 1.) + 0.01 * np.random.normal(size=len(Xn))


plt.figure(figsize=(6,6))
plt.plot(X, Y, c='k', label="calculated")
plt.scatter(Xn, Yn, s=250, marker="+", color="k", label="measured")
plt.xlim(15,21)
plt.ylim(0,1)
plt.grid(linestyle="-")
plt.xticks(np.linspace(15,21,7))
plt.yticks(np.linspace(0,1,11))
plt.legend()

plt.ylabel("Output power [W]")
plt.xlabel("Frequency [GHz]")

plt.tick_params(which='major', width=1.5)
plt.tick_params(which='minor', length=10)
plt.tick_params(which='major', length=20)
plt.axes().xaxis.set_minor_locator(MultipleLocator(0.10))
plt.axes().yaxis.set_minor_locator(MultipleLocator(0.01))


plt.savefig("exercise-1.png")

plt.show()
