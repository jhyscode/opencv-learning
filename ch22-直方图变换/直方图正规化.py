# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 11:39
# @Author  : jhys
# @FileName: 直方图正规化.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def hist_normalization(img, a=0, b=255):
    c = img.min()
    d = img.max()

    out = img.copy()
    # normalization
    out = (b - a) / (d - c) * (out - c) + a
    out[out < a] = a
    out[out > b] = b

    out = out.astype(np.uint8)
    return out


# Read image
img  = cv2.imread("imori_dark.jpg").astype(np.float)
H, W, C = img.shape

# histogram normalization
out = hist_normalization(img)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("out_his.png")
plt.show()

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)