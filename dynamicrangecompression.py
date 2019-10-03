# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:15:09 2019

@author: KumKap
"""
import cv2 as cv
import numpy as np
import math 

from matplotlib import pyplot as plt

aa = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0)
a = aa.astype('float32')

row, col = aa.shape 

c = np.array(np.zeros((row,col), np.float32))
  
for i in range (row):
    for j in range (col):
        c[i][j] = a[i][j] * ((-1)**(i+j)) 

f = np.fft.fft2(c)
ft = np.fft.fftshift(f)
d = np.abs(f)
d_log = (np.log(d+1)/(np.log(1+np.max(d))))*255
d_log = np.array(d_log,dtype=np.uint8)

cv.imshow('Dynamic range compression b',d_log )

cv.imshow('Dynamic range compression a',d.astype('uint8') )

cv.waitKey(0)
cv.destroyAllWindows()