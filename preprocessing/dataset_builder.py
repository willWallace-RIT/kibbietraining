import numpy as np
import json

def build_dataset(raw_landmarks, labels):
    X = []
    y = []

    for lm, label in zip(raw_landmarks, labels):
        X.append(np.array(lm).flatten())
        y.append(label)

    return np.array(X), np.array(y)
