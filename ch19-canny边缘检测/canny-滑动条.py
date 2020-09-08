# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 17:03
# @Author  : jhys
# @FileName: canny-滑动条.py

import numpy as np
import cv2

def nothing(x):
    pass

img=cv2.imread('test.jpg',0)

cv2.namedWindow('res')
cv2.createTrackbar('min','res',0,25,nothing)
cv2.createTrackbar('max','res',0,25,nothing)
while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    maxVal=cv2.getTrackbarPos('max','res')
    minVal=cv2.getTrackbarPos('min','res')
    canny=cv2.Canny(img,10*minVal,10*maxVal)
    cv2.imshow('res',canny)
cv2.destroyAllWindows()