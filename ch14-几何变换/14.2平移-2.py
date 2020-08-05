# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:48
# @Author  : jhys
# @FileName: 14.2平移-2.py

import cv2
import numpy as np

img = cv2.imread("../data/messi5.jpg", 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
