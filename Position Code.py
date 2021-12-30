import pyautogui as pag
import time
import keyboard
from PIL import ImageGrab

while True:
    pos = pag.position()
    print(pos)
    screen = ImageGrab.grab()
    rgb = screen.getpixel(pos)
    print(rgb)
    time.sleep(3) 
    if keyboard.is_pressed('F4'): # F4 누르면
        break # while문 탈출


checkpoint = (840, 846)
# cp2 = (686, 127)
# cp3 = (689, 130)
# color = (255, 235, 161)

# while True:
#   rgb = ImageGrab.grab().getpixel(checkpoint)
# #   rgb1 = ImageGrab.grab().getpixel(cp2)
# #   rgb2 = ImageGrab.grab().getpixel(cp3)
#   print(rgb)
# #   print(rgb1)
# #   print(rgb2)
#   time.sleep(3)
