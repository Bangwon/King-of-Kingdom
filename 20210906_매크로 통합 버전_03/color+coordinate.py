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
        
