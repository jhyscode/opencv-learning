# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 16:57
# @Author  : jhys
# @FileName: canny.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()