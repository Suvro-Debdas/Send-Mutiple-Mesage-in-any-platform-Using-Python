import pyautogui
import time
time.sleep(5)
count=0
while count <= 10000:
    pyautogui.typewrite("Enjoy Brother" + str(count))
    pyautogui.press("enter")
    count = count + 1