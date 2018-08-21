#!/bin/bash
# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# Advanced Scientific Programming in Python summer school
# -----------------------------------------------------------------------------
import numpy as np
from scipy import misc
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

matplotlib.rc('axes',edgecolor='w')

# We load the image to get its dimensions
im = misc.imread("neurons.jpg")

# Read image dimensions as lines (height), cols (width) and depth
h,w,_ = im.shape

# Now we open a new figure with size 2xw, 2xh
dpi = 72.0
W, H= 2*w/dpi, 2*h/dpi
fig = plt.figure(figsize=(W,H), dpi=dpi)

# Main figure
ax1 = plt.axes([0.0, 0.5, 0.5, 0.5])
ax1.imshow(im, origin='upper')
patch = patches.Rectangle((100,170),100,70, facecolor='none', edgecolor='white')
ax1.add_patch(patch)
ax1.text(105, 175, 'A', fontsize=12, va="top", color="white")
patch = patches.Rectangle((200, 20),100,70, facecolor='none', edgecolor='white')
ax1.add_patch(patch)
ax1.text(205,  25, 'B', fontsize=12, va="top", color="white")
patch = patches.Rectangle((270,200),100,70, facecolor='none', edgecolor='white')
ax1.add_patch(patch)
ax1.text(275, 205, 'C', fontsize=12, va="top", color="white")

ax1.set_xticks([])
ax1.set_yticks([])
#ax1.set_axis_off()

# Subplot A
ax2 = plt.axes([0.5, 0.5, 0.5, 0.5])
ax2.imshow(im, interpolation='none')
ax2.set_xlim(100,200)
ax2.set_ylim(240,170)
ax2.set_xticks([])
ax2.set_yticks([])
text = ax2.text(0.025, 0.95, 'A', fontsize=32, va="top", weight="bold",
                color="white", transform=ax2.transAxes)
text.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'),
                       path_effects.Normal()])
#ax2.set_axis_off()

# Subplot B
ax3 = plt.axes([0.0, 0.0, 0.5, 0.5])
ax3.imshow(im, interpolation='none')
ax3.set_xlim(200,300)
ax3.set_ylim( 90, 20)
ax3.set_xticks([])
ax3.set_yticks([])
text = ax3.text(0.025, 0.95, 'B', fontsize=32, va="top", weight="bold",
                color="white", transform=ax3.transAxes)
text.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'),
                       path_effects.Normal()])
#ax3.set_axis_off()

# Subplot C
ax4 = plt.axes([0.5, 0.0, 0.5, 0.5])
ax4.imshow(im, interpolation='none')
ax4.set_xlim(270,370)
ax4.set_ylim(270,200)
ax4.set_xticks([])
ax4.set_yticks([])
text = ax4.text(0.025, 0.95, 'C', fontsize=32, va="top", weight="bold",
                color="white", transform=ax4.transAxes)
text.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'),
                       path_effects.Normal()])
#ax4.set_axis_off()

# Show the figure
plt.show()
