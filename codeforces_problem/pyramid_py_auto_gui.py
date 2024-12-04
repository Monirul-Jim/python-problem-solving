

import pyautogui
import time
num = 6
time.sleep(2)

for row in range(num):
    for col in range(row + 1):
        pyautogui.typewrite('#', interval=0.1)

    pyautogui.press('enter')
