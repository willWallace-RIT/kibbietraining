import pyautogui

def press_key(key):
    if key:
        pyautogui.press(key.lower())
