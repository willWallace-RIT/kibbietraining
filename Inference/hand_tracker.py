import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7
        )

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        points = []
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                for lm in hand.landmark:
                    points.append((lm.x, lm.y))
        return points
