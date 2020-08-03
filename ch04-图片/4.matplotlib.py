# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:43
# @Author  : jhys
# @FileName: 4.matplotlib.py

import numpy as np
import cv2
import  matplotlib.pyplot as plt

img = cv2.imread("../data/messi5.jpg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.xticks([]), plt.yticks([])
plt.show()