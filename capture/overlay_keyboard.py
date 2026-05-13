import cv2
import numpy as np

KEYS = list("QWERTYUIOPASDFGHJKLZXCVBNM")

def draw_keyboard(frame):
    h, w, _ = frame.shape
    key_w = w // 10
    key_h = h // 5

    for i, key in enumerate(KEYS):
        x = (i % 10) * key_w
        y = (i // 10) * key_h

        cv2.rectangle(frame, (x, y), (x+key_w, y+key_h), (0,255,0), 2)
        cv2.putText(frame, key, (x+10, y+30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = draw_keyboard(frame)
    cv2.imshow("Green Keyboard Overlay", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
