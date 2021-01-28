from pynput.mouse import Button, Controller
import pyautogui
import time


# initialize mouse
mouse = Controller()

# set default values of variables
# tested on Win10, 1920x1280, default taskbar size and position
# position of the close botton of the brave for windows notification
brave_close_x = 1725
brave_close_y = 995
# postion of an orange pixel of the brave icon in the notification area
brave_pix_x = 1561
brave_pix_y_1 = 931
brave_pix_y_2 = 911
# how often the script is run in seconds
sleep_timer = 5
# pixel value to compare in RGB, default (255, 85, 0) is orange
pixel_compare_val = (255, 85, 0)


def check_pixel_val():
    try:
        pix_val = pyautogui.pixel(brave_pix_x, brave_pix_y_1)
        pix_val_2 = pyautogui.pixel(brave_pix_x, brave_pix_y_2)
        print(pix_val + pix_val_2)
    except:
        print("Cannot get pixel for the moment")
        pix_val = (0, 0, 0)
        pix_val_2 = (0, 0, 0)
    # if pix_val == pixel_compare_val:
    if pix_val == pixel_compare_val or pix_val_2 == pixel_compare_val:
        return True
    else:
        return False


def close_brave_notify():
    currentp = mouse.position
    mouse.position = (brave_close_x, brave_close_y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = currentp


while True:
    if check_pixel_val() is True:
        close_brave_notify()
    # print(check_pixel_val())
    time.sleep(sleep_timer)
