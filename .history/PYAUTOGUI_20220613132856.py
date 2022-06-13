#import

import pyautogui
import time

time.sleep(3)
pyautogui.click(x=3150, y=730)
time.sleep(3)
pyautogui.click(x=2902, y=958)
time.sleep(3)
pyautogui.write("oof girlie!")
print(pyautogui.position())
