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
        pos1 = pos[0]+640, pos[1]
        pos2 = pos[0]+1280, pos[1]
        pos3 = pos[0], pos[1]+400
        pos4 = pos[0]+640, pos[1]+400
        pos5 = pos[0]+1280, pos[1]+400
        print(pos)
        from PIL import ImageGrab
        screen = ImageGrab.grab()
        rgb = screen.getpixel(pos)
        rgb1 = screen.getpixel(pos1)
        rgb2 = screen.getpixel(pos2)
        rgb3 = screen.getpixel(pos3)
        rgb4 = screen.getpixel(pos4)
        rgb5 = screen.getpixel(pos5)

        print(rgb)
        print(rgb1)
        print(rgb2)
        print(rgb3)
        print(rgb4)
        print(rgb5)
        time.sleep(0.5)
        
    elif keyboard.is_pressed('F8'):
        pos = 341, 360
        # 341, 360
        pos1 = pos[0]+640, pos[1]
        pos2 = pos[0]+1280, pos[1]
        pos3 = pos[0], pos[1]+400
        pos4 = pos[0]+640, pos[1]+400
        pos5 = pos[0]+1280, pos[1]+400
        print(pos)
        from PIL import ImageGrab
        screen = ImageGrab.grab()
        rgb = screen.getpixel(pos)
        rgb1 = screen.getpixel(pos1)
        rgb2 = screen.getpixel(pos2)
        rgb3 = screen.getpixel(pos3)
        rgb4 = screen.getpixel(pos4)
        rgb5 = screen.getpixel(pos5)

        print(rgb)
        print(rgb1)
        print(rgb2)
        print(rgb3)
        print(rgb4)
        print(rgb5)
        time.sleep(0.5)



