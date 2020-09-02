# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 16:44
# @Author  : jhys
# @FileName: 直方图正规化1.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    src = cv2.imread("child.jpg", cv2.IMREAD_ANYCOLOR)
    dst = np.zeros_like(src)

    cv2.normalize(src, dst, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)


    #计算灰度直方图
    grayHist = cv2.calcHist([src], [0], None, [256], [0, 256])
    grayHist1 = cv2.calcHist([dst], [0], None, [256], [0, 256])

    #画出直方图
    x_range = range(256)
    plt.plot(x_range, grayHist, 'r', linewidth=1.5, c='black')
    plt.plot(x_range, grayHist1, 'r', linewidth=1.5, c='b')
    #设置坐标轴的范围
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue]) #画图范围
    plt.xlabel("gray Level")
    plt.ylabel("number of pixels")
    plt.show()

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyWindow()

