# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 16:18
# @Author  : jhys
# @FileName: 10.addWeighted.py

import cv2
import numpy as np

# 图像混合

img1 = cv2.imread('../data/ml.png')
img2 = cv2.imread('../data/opencv_logo.png')
h, w, _= img1.shape
img3 = cv2.resize(img2, (w,h), interpolation=cv2.INTER_AREA)

dst = cv2.addWeighted(img1, 0.7, img3, 0.3, 0)  # 第一幅图的权重是 0.7 第二幅图的权重是 0.3
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyWindow()