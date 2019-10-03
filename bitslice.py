# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:40:37 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def decimalToBinary(n): 
    temp = bin(n).replace("0b","")
    rem = len(temp) % 8 
    if(rem != 0):
        append = "0"* (8-rem)
        temp = append + temp
    return(temp)    
  
img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0) 
row, col = img.shape 

cv.imshow("Original Image",img)

output = np.array(np.zeros((row,col), np.float32))
r = 2 #int(input("Enter value: ")) 

for i in range (row):
    for j in range (col):
        c = decimalToBinary(img[i][j])
        d = c[r]
        output[i][j] = int(d)
        if(output[i][j] == 1):
            output[i][j] = 255
output = output.astype('uint8')

cv.imshow("Binary Slice",output)

cv.waitKey(0)
cv.destroyAllWindows()        
