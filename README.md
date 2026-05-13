# VR Keyboard Vision System

A vision-based input system that replaces physical keyboard typing with hand tracking and spatial intent inference.

The dataset is created using a physical green keyboard. The keyboard is used only during capture to define spatial layout, then it is fully removed from all training frames. The remaining data is downsampled to eliminate any residual visual artifacts from segmentation or editing.

The model learns spatial relationships between hand position and keyboard coordinates, not keyboard appearance.

---

## System Description

The system converts camera input into keyboard events using the following process:

1. A physical green keyboard is recorded during interaction
2. The keyboard is segmented using color thresholding
3. The keyboard region is removed from each frame
4. The resulting frames are downsampled to reduce artifact retention
5. Hand landmarks are extracted from the processed frames
6. A model is trained on spatial hand-to-key mappings
7. Real-time inference converts hand motion into key events

---

## Dataset Method

The dataset is generated from real recordings of a green keyboard environment.

The purpose of the keyboard is strictly structural. It defines:

- key positions
- spatial layout
- labeling reference

It is not used as a visual feature.

After segmentation:

- keyboard pixels are removed entirely
- replaced with neutral or blank background
- frames are reduced in resolution

The final dataset contains only hand motion and spatial structure.

---

## Artifact Suppression Strategy

To prevent the model from learning unintended visual signals, the dataset is processed with the following constraints:

- keyboard is fully removed before training
- segmentation boundaries are not preserved
- images are downsampled after removal
- no high-frequency visual information is retained

This ensures the model does not learn:
- keyboard edges
- key labels
- lighting artifacts
- segmentation traces

The model only receives coarse spatial information.

---

## Project Structure

vr-keyboard-vision/

capture/
record_session.py
overlay_keyboard.py

preprocessing/
segment_keyboard.py
remove_keyboard.py
downsample.py
build_dataset.py

model/
model.py
train.py
dataset.py
evaluate.py

inference/
realtime.py
hand_tracker.py
predictor.py
smoothing.py

vr_bridge/
input_emulator.py
hid_interface.py

utils/
camera.py
geometry.py
timing.py

data/
raw/
masked/
downsampled/
labels/

config.py
requirements.txt
README.md

---

## Requirements

opencv-python
mediapipe
numpy
torch
torchvision
scikit-learn
pyautogui
pynput
matplotlib
tqdm

---

## Data Collection

Run:

python capture/record_session.py

This captures:
- video frames
- hand motion
- keyboard interaction labels

---

## Preprocessing

Segment keyboard:

python preprocessing/segment_keyboard.py

Remove keyboard:

python preprocessing/remove_keyboard.py

Downsample frames:

python preprocessing/downsample.py

Build dataset:

python preprocessing/build_dataset.py

---

## Training

Run:

python model/train.py

Output:
model/weights.pth

The model learns a mapping from hand geometry to keyboard space.

---

## Inference

Run:

python inference/realtime.py

The system performs:

- hand tracking
- landmark extraction
- spatial inference
- temporal smoothing
- keyboard event output

---

## Input Emulation

Keyboard events are emitted using:

- pyautogui
- pynput
- future virtual HID interface support

---

## Design Constraints

The system is designed so that:

- the keyboard is not part of the learned input
- only spatial relationships are preserved
- all visual artifacts are removed before training
- resolution reduction prevents reconstruction of removed elements

---

## Limitations

- requires stable lighting conditions
- requires calibration per environment
- dependent on camera quality
- not yet optimized for VR-native rendering

---

## Future Work

- VR floating keyboard using OpenXR
- transformer-based spatial intent model
- heatmap-based key prediction
- OS-level virtual keyboard driver
- embedded fallback input devices

---

## Goal

To create a software-defined keyboard system where a physical keyboard is only used for dataset generation and never appears in the learned representation.

The system is intended to operate in desktop, VR, and AR environments as a universal input layer.
