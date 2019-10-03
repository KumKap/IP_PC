# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:15:27 2019

@author: KumKap
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",1) # 0 for bw and 1 for color

impulse = np.array(([0,0,0],[0,1,0],[0,0,0]), np.float32) #identity

sobely = np.array(([-1,-2,-1],[0,0,0],[1,2,1]), np.float32) #edge detection1
sobelx = np.array(([-1,0,1],[-2,0,2],[-1,0,1]), np.float32) #edge detection1
previtty = np.array(([-1,-1,-1],[0,0,0],[1,1,1]), np.float32) #edge detection2
previttx = np.array(([-1,0,1],[-1,0,1],[-1,0,1]), np.float32) #edge detection2

largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
sharpen = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), np.float32) #sharpen
boxblur = np.array(np.ones((3,3), np.float32))/9 #box blur

output1 = cv.filter2D(img, -1, impulse)
output2 = cv.filter2D(img, -1, sobely)
output3 = cv.filter2D(img, -1, sobelx)
output4 = cv.filter2D(img, -1, previtty)
output5 = cv.filter2D(img, -1, previttx)
output6 = cv.filter2D(img, -1, largeBlur)
output7 = cv.filter2D(img, -1, sharpen)
output8 = cv.filter2D(img, -1, boxblur) 

cv.imshow("Original Image",img)
cv.imshow("Identity",output1)
cv.imshow("Sobel-y",output2)
cv.imshow("Sobel-x",output3)
cv.imshow("Previtt-y",output4)
cv.imshow("Previtt-x",output5)
cv.imshow("Large Blur",output6)
cv.imshow("Sharpen",output7)
cv.imshow("Box Blur",output8)

cv.waitKey(0)
cv.destroyAllWindows()

