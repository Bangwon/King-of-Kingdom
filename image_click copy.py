import pyautogui as pag
import time
import random

def autoexit1(x, y):
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+x, 213+y)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제


p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\braveportion.png", confidence=0.79)
p_list = list(p_list)
p_cneter = pag.center(p_list[0])
f1 = [478, 122]
f2 = [618, 327]



if len(p_list) == 0:
    print("이미지없음")
else :
    for p in p_list:
        ctr = pag.center(p)
        if ctr[0] >= f1[0] and ctr[0] <= f2[0] and ctr[1] >= f1[1] and ctr[1] < f2[1]:
            print(pag.center(p))
            pag.click(p, None, 1, 0.5)



