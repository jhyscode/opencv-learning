# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 21:11
# @Author  : jhys
# @FileName: 阈值分割5.py

# 导入库
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cell.jpg', 0)

# 自适应阈值
th1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV , 3, 0)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV , 33, 0)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV , 53, 0)
th4 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV , 73, 0)
th5 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 3, 0)
th6 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 33, 0)
th7 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 53, 0)
th8 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 73, 0)

titles = ['Original', 'MEAN_3', 'MEAN_33','MEAN_53','MEAN_73','GAUSSIAN_3','GAUSSIAN_33','GAUSSIAN_53','GAUSSIAN_73']
images = [img, th1, th2, th3, th4, th5, th6, th7, th8]

# 开始画图
plt.figure(figsize = (8,8))

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# 保存并展示图片
plt.savefig('4_out.png')
plt.show()