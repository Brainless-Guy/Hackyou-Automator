from pynput import keyboard
import time , random , pytesseract , pyautogui,os
from setup import scrape_numbers
from PIL import ImageGrab
# Set Tesseract-OCR path
import platform
script_dir= os.path.dirname(os.path.abspath(__file__))
os_name = platform.system()

if os_name == 'Darwin':
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
elif os_name == 'Linux':                                                              #DEFAULT , You can change it!
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
elif os_name == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
else:
    print("Tesseract is Not supported or Its Not INSTALLED!")
setup = input("Do you want to setup Auto-Upgrade ? (Y/N) : ")
if setup.capitalize() == 'Y':
    print("Please Enter Shift on the Upgrade Button to Record the position of Mouse!!")
    def record3():
        record = pyautogui.position()
        position_3 = tuple(record)
        x_coord = position_3[0]
        y_coord = position_3[1]
        return (x_coord,y_coord)
    def on_press3(key):
            k = "{0}".format(key)           
    def on_release3(key):
        if key == keyboard.Key.shift:
            global position_3
            position_3 = record3()
            print(position_3)
            return False 
    
    with keyboard.Listener(
        on_press=on_press3,

        on_release=on_release3) as listener3:
        listener3.join()
    x_ = position_3[0]
    y_ = position_3[1]
    time.sleep(2)




print("Do a /scan and , Please Put your Cursor below-Right of the scan and Press SHIFT!!")
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
print(" Please Put your Cursor Top-Left of the scan Result and Press SHIFT!!")
x1 = position[0]
y1 =position[1]
def record2():
    record = pyautogui.position()
    position = tuple(record)
    x_coord = position[0]
    y_coord = position[1]
    return (x_coord,y_coord)
def on_press2(key):
        k = "{0}".format(key)           
def on_release2(key):
    if key == keyboard.Key.shift:
        global position2
        position2 = record2()
        print(position2)
        return False 
with keyboard.Listener(
    on_press=on_press2,
    on_release=on_release2) as listener:
    listener.join()

x2 = position2[0]
y2= position2[1]


time.sleep(5)
def capture_and_extract_text(x1, y1, x2, y2):
    left, top, right, bottom = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    bbox = (left, top, right, bottom)
    screenshot = ImageGrab.grab(bbox)
    text = pytesseract.image_to_string(screenshot)
    return text

def auto_hack(ids, x=None, y=None):
    for pid in ids:
        if pid:
            # print(pid)
            pyautogui.write(f"/hack ")
            time.sleep(0.5)
            pyautogui.write(pid)
            time.sleep(1)
            pyautogui.press("enter")

            time.sleep(62)
        else:
            choices = ["virus", "exploit", "firewall"]
            pyautogui.write(f"/{random.choice(choices)}")
            pyautogui.press("enter")
            pyautogui.doubleClick(x, y)
            time.sleep(3)

upgrade_Counter = 1
if __name__ == "__main__":
    while True:
            if upgrade_Counter % 5 != 0:
                time.sleep(2)
                upgrade_Counter += 1
                extracted_text = capture_and_extract_text(x1, y1, x2, y2)
                ids = scrape_numbers(extracted_text)
                auto_hack(ids)
                time.sleep(7)
                pyautogui.write("/scan")
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("enter")
                time.sleep(2)
                #
            else:
                upgrade_Counter += 1
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
                
                
