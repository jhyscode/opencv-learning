# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:56
# @Author  : jhys
# @FileName: video_read1.py

import numpy as np
import cv2

cap = cv2.VideoCapture('traffic.flv')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()