import pyautogui as pag
import keyboard
import time

# while True:
#     if keyboard.is_pressed('F4'):
#         t1 = pag.position()
#         print(t1)
#         time.sleep(0.5)
#         break
# while True:
#     if keyboard.is_pressed('F4'):
#         t2 = pag.position()
#         print(t2)
#         time.sleep(0.5)
#         break
# while True:
#     if keyboard.is_pressed('F4'):
#         f1 = pag.position()
#         print(f1)
#         time.sleep(0.5)
#         break
# while True:
#     if keyboard.is_pressed('F4'):
#         f2 = pag.position()
#         print(f2)
#         time.sleep(0.5)
#         break

# region1 = (t1[0], t2[1], t2[0]-t1[0], t2[1]-t1[1])

# pag.screenshot('C:\\Users\\ODIN\\ODIN\\LineageW\\find.png', region = region1)

p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\summon.png", confidence=0.99)
p_list = list(p_list)
p=pag.center(p_list[0])
# len=len(p_list)
print(p)
# print(len)
pag.click(p[0], p[1], 2, 1)

# if p[0] > f1[0] and p[1] > f1[1] and p[0] < f2[0] and p[1] <f2[1]:
#     print(p)
