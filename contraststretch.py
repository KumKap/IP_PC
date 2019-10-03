# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 02:35:15 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
  
img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0) 
row, col = img.shape 
img_temp = img.astype('float32')

output = np.array(np.zeros((row,col), np.uint8))
LT = int(input("Enter lower threshold value: "))
UT = int(input("Enter higher threshold value: "))

for i in range (row):
    for j in range (col):
        if(img[i][j] <= LT):
            output[i][j] = img[i][j] // 2
        elif(img[i][j] <= UT):
            output[i][j] = 2 * (img[i][j] -LT) + (LT // 2)
        else:
            output[i][j] = (img[i][j] - UT) // 2  + (LT // 2) + (2 *(UT - LT))
        
cv.imshow("Original Image",img)
cv.imshow("Contrast Stretching",output)

cv.waitKey(0)
cv.destroyAllWindows()        
