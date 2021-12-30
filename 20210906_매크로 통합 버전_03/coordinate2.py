import pyautogui as pag
import keyboard
import time

while True:
    mousePositionX, mousePositionY = pag.position()
    print(mousePositionX,",",mousePositionY)
    time.sleep(1)
    if keyboard.is_pressed('F4'): # F4 누르면
        break # while문 탈출