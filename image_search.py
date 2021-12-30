import pyautogui as pag
import time

p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\V.PNG")
p_list = list(p_list)
p_cneter = pag.center(p_list[0])
pag.click('V.png')
print(p_list)
