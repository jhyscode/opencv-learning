# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 20:58
# @Author  : jhys
# @FileName: 直方图.py

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("airplane.jpg",0)
#


plt.hist(img.ravel(), 256, [0, 256])
plt.show()
