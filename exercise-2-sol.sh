#!/bin/bash
# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# Advanced Scientific Python Programming summer school
# -----------------------------------------------------------------------------

# Draw 3 rectangles on the image 
convert neurons.jpg \
    -fill none -stroke white -strokewidth 2 -draw "rectangle 100,170,200,240" \
    -fill none -stroke white -strokewidth 2 -draw "rectangle 200, 20,300, 90" \
    -fill none -stroke white -strokewidth 2 -draw "rectangle 270,200,370,270" \
    neurons_abc.jpg

# Crop, resize and label first subimage (100x70+100+170)
convert neurons.jpg \
    -crop 100x70+100+170 -resize 500x350 \
    -background none -fill white -stroke black -strokewidth 1 \
    -font Helvetica-bold -pointsize 32 label:'(a)' -gravity northwest \
    -geometry +10+12 -composite neurons_a.jpg

# Crop, resize and label second subimage (100x70+200+20)
convert neurons.jpg \
    -crop 100x70+200+20 -resize 500x350 \
    -background none -fill white -stroke black -strokewidth 1 \
    -font Helvetica-bold -pointsize 32 label:'(b)' -gravity northwest \
    -geometry +10+12 -composite neurons_b.jpg

# Crop, resize and label third subimage (100x70+270+200)
convert neurons.jpg \
    -crop 100x70+270+200 -resize 500x350 \
    -background none -fill white -stroke black -strokewidth 1 \
    -font Helvetica-bold -pointsize 32 label:'(c)' -gravity northwest \
    -geometry +10+12 -composite neurons_c.jpg

# Final composition
montage neurons_abc.jpg neurons_a.jpg neurons_b.jpg neurons_c.jpg \
    -tile 2x2 -geometry +3+3 final.jpg

# Cleanup tmp files
rm neurons_abc.jpg
rm neurons_a.jpg
rm neurons_b.jpg
rm neurons_c.jpg
