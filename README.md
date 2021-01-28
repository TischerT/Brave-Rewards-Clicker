# Brave Rewards Clicker
Checks for Brave Browser Rewards Ad notifications on Windows and closes them

## Idea and concept
Brave rewards lets you see a small number of Ads in the form of (Windows) notifications. They remain on the desktop for about 30 seconds or until you manually press the close button. Any Windows notification setting seem not to have any effect on them (even setting the notifications to 1 sec via the windows registry leaves them for 30 secs).
This small python script can be set up to run in the background and checks for the Brave browser notification to show up. It subsequently closes it.

## Requirements
Written in Python 3.9 using to following modules:
* pynput
* pyautogui
* time

## Setup
1. *find your own values* with the use of find_values.py
1. Wait for the Brave rewards notification to show up and move the mouse on top of the orange part of the Brave icon
1. Run the script
1. Replace the values for *brave_close_x and y* as well as *brave_pix_x and y* and *pixel_compare_value*
1. *sleep_timer* defines the pause between each execution of the script
1. Use the Windows Task Scheduler to run the script on Log-on, [see here for example](https://community.esri.com/t5/python-documents/schedule-a-python-script-using-windows-task-scheduler/ta-p/915861), you can use **pyw.exe** to run the script without a cmd window


## Known limitations
* If you have an orange desktop background with the exact same color as the Brave icon, the script will detect this constantly.
* Could not test the script in Linux.
