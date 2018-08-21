# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization crash course 
# Advanced Scientific Python Programming summer school
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt

dpi = 300
fig = plt.figure(figsize = (3.15,3.15))

plt.subplot(111)
plt.savefig("exercise-4.png", dpi=dpi)
plt.show()

