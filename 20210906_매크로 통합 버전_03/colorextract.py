import pyautogui as pag
import keyboard
import time

while True:
    pos = pag.position()
    from PIL import ImageGrab
    screen = ImageGrab.grab()
    rgb = screen.getpixel(pos)
    print(rgb)
    time.sleep(1)
    if keyboard.is_pressed('F4'): # F4 누르면
        break # while문 탈출