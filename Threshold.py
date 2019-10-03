# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:06:20 2019

@author: KumKap
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0) 
row, col = img.shape 
output = np.array(np.zeros((row,col), np.uint8))

thresh = int(input("Enter Threshold value: "))
cv.imshow("Original Image",img)

for i in range (row):
    for j in range (col):
        if(img[i][j] < thresh):
            img[i][j] = 0 
        else:
            img[i][j] = 255

cv.imshow("Threshold Image",img)

cv.waitKey(0)
cv.destroyAllWindows()