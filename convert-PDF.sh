#!/bin/bash

convert -density 150 $1 -bordercolor black -border 1 -scale 25% ${1%.pdf}_%03d.png
montage -tile 3x -geometry +5+5 ${1%.pdf}_*.png ${1%pdf}png
rm -f ${1/.pdf/}_*.png
