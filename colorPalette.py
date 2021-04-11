import colorsys
import cv2
import numpy as np

# set hue, saturation and valuness here.
h, s, v = 0, 87.5, 87.5

# output image date
img = np.full((600, 800, 3), 128, dtype=np.uint8)

# cordinate for making color rectangule.
sX = 0
sY = 0
eX = 200
eY = 200

# make palette 3columns * 4rows
for i in range(3):
    for j in range(4):
        # Matching the HSV value range for OpenCV value range.
        # General : H(0,360), S(0,100), V(0,100)
        h_ = h/360
        s_ = s/100
        v_ = v/100
        # conver hsv to rgb using OpenCV library method.
        r,g,b = colorsys.hsv_to_rgb(h_, s_, v_)
        # Matching the RGB value range for OpenCV Recatngule method.
        b = b*255
        g = g*255
        r = r*255
        # make rectangule of each hsv value.
        cv2.rectangle(img, (sX, sY), (eX, eY), (b, g, r), thickness=-1)
        # Move the coordinates.
        sX = sX + 200
        eX = eX + 200
        #  Increase the hue by 30 degrees.
        h = h + 360/12
    # Reset X coordinates.
    sX = 0
    # Move Y coordinates.
    sY = sY + 200
    eY = eY + 200
    
# write result image
cv2.imwrite("result-S"+str(s)+"V"+str(v)+".png", img)
