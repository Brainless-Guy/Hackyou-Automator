import pyautogui
from pynput import keyboard
import time,os
import random
from colorama import Fore,Back
script_dir = os.path.dirname(os.path.abspath(__file__))
def auto(bool,x_=None,y_=None):
    time.sleep(5)                      # 5 seconds wait to change the window!
    with open(f"{script_dir}\\assets\\hacks.txt","r") as ids:
        ids = ids.readlines()
        for pid in ids:
            pid = pid.strip()
            if pid != "":
                text = f"/hack "
                pyautogui.write(text)
                time.sleep(0.5)
                pyautogui.write(pid)
                time.sleep(0.5)
                pyautogui.press("enter")
                time.sleep(62)
            else:
                if bool == True:
                    listofChoices = ["virus","exploit","firewall"]
                    time.sleep(0.5)
                    pyautogui.write(f"/{random.choice(listofChoices)}")
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    time.sleep(3)
                    pyautogui.doubleClick(x_,y_)
                    time.sleep(3)

setup = input(Back.LIGHTCYAN_EX +Fore.BLACK+"Do you want to setup Auto-Upgrade ? (Y/N) : ")
if setup.capitalize() == 'Y':
    print(Back.RED+Fore.BLACK+"Please Enter Shift on the Upgrade Button to Record the position of Mouse!!")
    def record():
        record = pyautogui.position()
        position = tuple(record)
        x_coord = position[0]
        y_coord = position[1]
        return (x_coord,y_coord)
    def on_press(key):
            k = "{0}".format(key)           
    def on_release(key):
        if key == keyboard.Key.shift:
            global position
            position = record()
            print(position)
            return False 
    
    with keyboard.Listener(
        on_press=on_press,

        on_release=on_release) as listener:
        listener.join()
    time.sleep(2)
    auto(True,position[0],position[1])
else:
    time.sleep(1)
    auto(False)

