# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 21:13
# @Author  : jhys
# @FileName: channel_split.py

import numpy as np
import cv2

image = cv2.imread("../data/lena.jpeg")
B,G,R = cv2.split(image)                     #分离出图片的B，R，G颜色通道

cv2.imshow("RED",R)                            #显示三通道的值都为R值时d图片
cv2.imshow("GREEN",G)                        #显示三通道的值都为G值时d图片
cv2.imshow("BLUE",B)                          #显示三通道的值都为B值时d图片
cv2.waitKey(0)                             #不让程序突然结束
