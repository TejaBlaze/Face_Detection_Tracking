import cv2
import numpy as np
import sys
src = raw_input("Image name: ")
fn = 'Input_images/'+src
imgIn = cv2.imread(fn)#, cv2.IMREAD_GRAYSCALE)
kernel = np.zeros( (9,9), np.float32)
kernel[4,4] = 2.0   #Identity, times two! 
#Create a box filter:
boxFilter = np.ones( (9,9), np.float32) / 81.0
#Subtract the two:
kernel = kernel - boxFilter
#Note that we are subject to overflow and underflow here...but I believe that
# filter2D clips top and bottom ranges on the output, plus you'd need a
# very bright or very dark pixel surrounded by the opposite type.
custom = cv2.filter2D(imgIn, -1, kernel)
cv2.imwrite('Sharpened_images/'+src, custom)