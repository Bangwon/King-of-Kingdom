import pyautogui as pag
import keyboard
import time

while True:
    if keyboard.is_pressed('F4'): # F4 누르면
        pos = pag.position()
        print(pos)
        from PIL import ImageGrab
        screen = ImageGrab.grab()
        rgb = screen.getpixel(pos)
        print(rgb)
        time.sleep(0.5)
    if keyboard.is_pressed('F6'):
        break
        
    elif keyboard.is_pressed('F7'):
        pos = pag.position()
        pos1 = 337+640, 362+400
        pos2 = 337+1280, 362
        pos3 = 337+1280, 362+400
        print(pos)
        from PIL import ImageGrab
        screen = ImageGrab.grab()
        rgb = screen.getpixel(pos)
        rgb1 = screen.getpixel(pos1)
        rgb2 = screen.getpixel(pos2)
        rgb3 = screen.getpixel(pos3)

        print(rgb)
        print(rgb1)
        print(rgb2)
        print(rgb3)
        time.sleep(0.5)


