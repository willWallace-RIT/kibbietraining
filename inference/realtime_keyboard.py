import cv2
import torch
from hand_tracker import HandTracker
from key_classifier import predict_key
from smoothing import SmoothBuffer
from vr_bridge.input_emulator import press_key

cap = cv2.VideoCapture(0)
tracker = HandTracker()
buffer = SmoothBuffer()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = tracker.get_landmarks(frame)

    if len(landmarks) > 0:
        key = predict_key(landmarks)
        key = buffer.update(key)

        if key:
            press_key(key)

    cv2.imshow("VR Keyboard", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
