# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 21:09
# @Author  : jhys
# @FileName: 阈值分割3.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg', 0)

# 固定阈值
_, th1 = cv2.threshold(img, 40,  255, cv2.THRESH_BINARY )
_, th2 = cv2.threshold(img, 90,  255, cv2.THRESH_BINARY )
_, th3 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY )
_, th4 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY )
_, th5 = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY )

# 自适应阈值
th6 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY , 11, 4)
th7 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 17, 6)
th8 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 5, 6)

titles = ['Original', 'BINARY_40', 'BINARY_90', 'BINARY_140', 'BINARY_190', 'BINARY_210', 'MEAN_C_11','GAUSSIAN_C_17','GAUSSIAN_C_5']
images = [img, th1, th2, th3, th4, th5, th6, th7, th8]

# 开始画图
plt.figure(figsize = (8,8))

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# 保存并展示图片
plt.savefig('3_out.png')
plt.show()