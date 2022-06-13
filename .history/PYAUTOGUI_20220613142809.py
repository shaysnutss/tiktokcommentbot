#import

import pyautogui
import time

time.sleep(3)
pyautogui.moveTo(3149,728)
pyautogui.click(3149, 728,2,button='left')
time.sleep(3)
pyautogui.moveTo(x=2894, y=952)
pyautogui.click(x=2894, y=952)
time.sleep(2)
pyautogui.write("oof girlie!")
pyautogui.moveTo(x=3159, y=959)
pyautogui.click(x=3159, y=959)

pyautogui.moveTo(x=2966, y=321)
pyautogui.click(x=2966, y=321)

pyautogui.moveTo(x=3002, y=828)
pyautogui.dragTo(3009,292,1,)

print(pyautogui.position())
