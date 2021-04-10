# Color Palette

# HSV (HSB) Color Space
HSV = H(Hue) + S(Saturation) + V(Valuness)  
HSB = H(Hue) + S(Saturation) + B(Brightness)
* HSV and HSB is Same Color Space.  

# RGB to HSV / HSV to RGB
Converting RGB to HSV using Python needs "colorsys" library(Python provides us).  
This implmetation is following.  

```
import colorsys
colorsys.rgb_to_hsv(0.2, 0.4, 0.4) # out : (0.5, 0.5, 0.4)
colorsys.hsv_to_rgb(0.5, 0.5, 0.4) # out : (0.2, 0.4, 0.4)
```

* In Python, color space(RGB,HSV,etc) is defined in the range (0,1).  
* In General, HSV consits of H(0,360°),S(0,100%),V(0,100%).  

#
