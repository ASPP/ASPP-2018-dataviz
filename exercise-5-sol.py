# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# Advanced Scientific Python Programming summer school
# Inspired by http://merqur.io/2015/10/02/drawing-a-brain-with-bokeh
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

n = 75
radius = 1
T = np.linspace(0,2*np.pi,n,endpoint=False)
P = radius * np.vstack((np.cos(T),np.sin(T))).T
C = np.abs(np.random.uniform(0, 1, size=(n,n)))

# Limit in connection strenght for displaying the link
c_min = 0.99

# Line width of the weakest and strongest connections
lw_min, lw_max = 0.5, 8.0

# Colormap to use
cmap = plt.cm.viridis

# Handy function to draw a cubic Bézier
def bezier(p0, p1, p2, p3, color='k', linewidth=1.0):
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(np.array([p0,p1,p2,p3]), codes)
    return patches.PathPatch(path, fc='none',
                             color=color, linewidth=linewidth)


# New figure with aspect = 1
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, aspect=1)

# Get connections stronget than c_min
I, J = np.where(C > c_min)

# Normalized them
vmin, vmax = C[I,J].min(), C[I,J].max()
LW = lw_min + ((C-vmin)/(vmax-vmin))**2 *(lw_max-lw_min)

# Draw connections
for i,j in zip(I,J):
    color = cmap(T[i]/(2*np.pi))
    linewidth = LW[i,j]
    # Make connection more visible
    # patch = bezier(P[i], P[i]/2, P[j]/2, P[j], color='w', linewidth=linewidth+2)
    # ax.add_patch(patch)
    patch = bezier(P[i], P[i]/2, P[j]/2, P[j], color=color, linewidth=linewidth)
    ax.add_patch(patch)

# Draw points
plt.scatter(P[:,0],P[:,1], s=100, color=T, linewidth=1.5,
            edgecolor='white', cmap=cmap, zorder=10)

# Draw labels
for i,angle in enumerate(T):
    x, y = 1.05*np.cos(angle), 1.05*np.sin(angle)
    text = "  area %03d" % i
    plt.text(x, y, text, size=12, ha="left",va="center",
             rotation = 180*angle/np.pi, rotation_mode="anchor")

plt.xlim(-1.35,+1.35)
plt.ylim(-1.35,+1.35)
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("exercise-5-sol.png")
plt.show()
