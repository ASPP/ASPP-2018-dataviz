# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# Advanced Scientific Programming in Python summer school
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

np.random.seed(123)

# Clean data
X = np.linspace(15, 21, 100)
Y = gaussian(X, 0.65, 17.6, 1.)

# Noisy dat
Xn = np.random.uniform(16, 20, 25)
Yn = gaussian(Xn, 0.65, 17.6, 1.) + 0.01 * np.random.normal(size=len(Xn))

plt.figure(figsize=(8,6), facecolor="w")
ax = plt.subplot(121)
plt.plot(X, 1000*Y, color='orange', linewidth=1.5, zorder=-10,
         clip_on=False)
plt.scatter(Xn, 1000*Yn, s=50, marker=".", color="black")


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes', -0.1))
ax.spines['bottom'].set_color('0.5')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('axes', -0.5))
ax.spines['left'].set_color('0.5')

plt.xlim(16,20)
plt.ylim(0,650)

plt.xticks([16,17.6,20],["16", "17.6 GHz", "20"])
plt.yticks([0, 325, 650], ["0", "", "650 mW"])

plt.tick_params(which='major', width=1.5, color="0.5")

ax.text(-0.5, 1.02, 'Output power',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes, color='0.5', fontsize=12)
ax.text(18, 630, 'Measured',        
        transform=ax.transData, color='black', fontsize=12)
ax.text(18.5, 500, 'Calculated',
        transform=ax.transData, color='orange', fontsize=12)

plt.tight_layout(pad=2.0)

[t.set_color('0.5') for t in ax.xaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.xaxis.get_ticklabels()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklabels()]

plt.savefig("exercise-1-sol.png")
plt.show()
