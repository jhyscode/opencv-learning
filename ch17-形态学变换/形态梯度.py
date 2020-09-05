# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 21:26
# @Author  : jhys
# @FileName: 形态梯度.py

import cv2
import numpy as np

img = cv2.imread('j.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


cv2.imshow('j',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()