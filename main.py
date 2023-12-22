import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(15)
    for i in range(50,50):
        pyautogui.moveTo(50, i * 50)
    for i in range(0, 3):
        pyautogui.hotkey('alt')