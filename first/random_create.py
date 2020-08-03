# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 21:06
# @Author  : jhys
# @FileName: random_create.py

import cv2
import numpy as np
import os

randomByteArray =  bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
print(grayImage)
print(grayImage[0,0])
cv2.imwrite('RandomGray.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
print(bgrImage)
print(bgrImage[0, 0, 0])
print(bgrImage[0, 0, 1])
print(bgrImage[0, 0, 2])
cv2.imwrite('RandomColor.png', bgrImage)
