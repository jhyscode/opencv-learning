# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 20:58
# @Author  : jhys
# @FileName: 阈值分割2.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cell.jpg', 0)

# 应用5种不同的阈值方法
_, th1 = cv2.threshold(img, 40,  255, cv2.THRESH_BINARY_INV)
_, th2 = cv2.threshold(img, 90,  255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY_INV)
_, th4 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY_INV)
_, th5 = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)

titles = ['Original', 'BINARY_40', 'BINARY_90', 'BINARY_140', 'BINARY_190', 'BINARY_210']
images = [img, th1, th2, th3, th4, th5]

plt.figure(figsize=(8, 4))

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.savefig("2_out.png")
plt.show()
