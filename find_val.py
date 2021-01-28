from pynput.mouse import Controller
import pyautogui

mouse = Controller()
currentp = mouse.position
print(currentp)
im = pyautogui.screenshot()
pix = im.getpixel(currentp)
print(pix)
