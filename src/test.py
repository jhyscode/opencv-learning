# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 16:48
# @Author  : jhys
# @FileName: test.py

import cv2
import numpy as np
import sys

#img = np.zeros((3,3), dtype=np.uint8)
#img = img.astype('uint8')
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#print(img)

img = cv2.imread("Emperor_penguins.jpg",1)
#cv2.imshow("Penguins",img)

resized_image = cv2.resize(img, (650,500))
cv2.imshow("Penguins", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print(img.shape)