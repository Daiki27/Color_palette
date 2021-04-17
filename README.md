# Color Palette | HSV
This program makes 12 colors that are identical in tone and outputs them in the form of an image.  
* input : s,v  
* output : rgb image (see "Example Tone Equal Colors")  

```
python3 colorPalette.py
```


## HSV (HSB) Color Space
HSV = H(Hue) + S(Saturation) + V(Valuness)  
HSB = H(Hue) + S(Saturation) + B(Brightness)
* HSV and HSB is Same Color Space.  

## RGB to HSV / HSV to RGB
Converting RGB to HSV using Python needs "colorsys" library(Python provides us).  
This implmetation is following.  

```
import colorsys
colorsys.rgb_to_hsv(0.2, 0.4, 0.4) # out : (0.5, 0.5, 0.4)
colorsys.hsv_to_rgb(0.5, 0.5, 0.4) # out : (0.2, 0.4, 0.4)
```

* In Python, color space(RGB,HSV,etc) is defined in the range (0,1).  
* In General, HSV consits of H(0,360°),S(0,100%),V(0,100%).  

## HSV and Tone Region
It is said that using colors that match in tone will create a sense of unity in the design. So, I define the color tone areas(T1 ~ T16) as shown in the following figure. Then, I use the value at the center of each region as the representative value, and the following figure shows the visualization of these values.  
<img width="960" alt="HSV1" src="https://user-images.githubusercontent.com/27540739/114301744-12589580-9b01-11eb-90ad-993385fcfdaf.png">


## Example Tone Equal Colors
The following figure shows the results when the hue is changed by 30 degrees in a certain tone areas(T1 ~ T16). Once the tone is decided, a unified color scheme can be achieved by designing with these colors.The top left corner is 0 degrees, and each time you move next to it, the hue increases by 30 degrees.

<img width="1252" alt="スクリーンショット 2021-04-11 20 24 07" src="https://user-images.githubusercontent.com/27540739/114302421-e4c11b80-9b03-11eb-99d2-6dd2a43e364d.png">

## Supplement
PCSS defines tone like [this](http://www.sikiken.co.jp/pccs/pccs04.html)  

## Ref
RGB to HSV Mathematics [site](http://hooktail.org/computer/index.php?RGB%A4%AB%A4%E9HSV%A4%D8%A4%CE%CA%D1%B4%B9%A4%C8%C9%FC%B8%B5)
