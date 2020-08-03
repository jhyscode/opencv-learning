# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 21:01
# @Author  : jhys
# @FileName: img_roi.py

import cv2
import numpy as np

img = cv2.imread("../data/messi5.jpg")

img[:,:,1] = 0
cv2.imshow("test",img)
cv2.waitKey(0)
cv2.destroyWindow()