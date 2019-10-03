# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:41:05 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0)
row, col = img.shape 
output = np.array(np.zeros((row,col), np.uint8))

cv.imshow("Original Image",img)

for i in range (row):
    for j in range (col):
        if(img[i][j] > 50 and img[i][j] < 150):
            img[i][j] = 255
        else:
            img[i][j] = img[i][j]

cv.imshow("Gray Sliced",img)

cv.waitKey(0)
cv.destroyAllWindows()
