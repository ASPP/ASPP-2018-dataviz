
### Computing column size

  * DPI = Dots Per Inch
  * 1 inch = 2.54cm
  * Double-column article on A4 paper (21cm x 29.4cm)
  * Margin is 2cm, column separation is 1cm
  * One column is ≈(21 - 2x2 - 1)/2 ≈ 8cm
  * Figures should be rendered at 300dpi  
    → 8/2.54*300 ≈ 954 pixels ≈ 1000 pixels wide
 

### Vector or bitmap

* If figure has been saved in bitmap format (e.g. PNG), you should ensure it has
  sufficient resolution
* If figure has been saved in vector format (e.g. PDF), you don't care about
  resolution
  
Vector or bitmap ? If you have only a few elements on your figure, vector might
be a good idea. If you have many small elements, bitmap might be a better
option (smaller file size, faster rendering).
