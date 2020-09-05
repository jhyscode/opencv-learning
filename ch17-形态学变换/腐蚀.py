# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 21:09
# @Author  : jhys
# @FileName: 腐蚀.py

import cv2
import numpy as np

img = cv2.imread('j.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('j',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()