import pyautogui as pag
import time

p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\V.PNG")
p_list = list(p_list)
pag.click('V.png')
print(p_list)
