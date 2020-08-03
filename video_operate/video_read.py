# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:20
# @Author  : jhys
# @FileName: video_read.py

import cv2

cap = cv2.VideoCapture('./traffic.flv')

while True:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break