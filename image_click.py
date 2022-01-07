import pyautogui as pag
import time

p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\V.PNG")
p_list = list(p_list)
p_cneter = pag.center(p_list[0])
pag.click('V.png')


if len(p_list) == 0:
    print("이미지없음")
else :
    for p in p_list:
        ctr = pag.center(p)
        if ctr[0] >= f1[0] and ctr[0] <= f2[0] and ctr[1] >= f1[1] and ctr[1] < f2[1]:
            print(pag.center(p))


while True:
    if len(p_list) == 0:
        pag.moveTo(496+1280, 246+400)
        pag.drag(0, -100, 1)
        time.sleep(2)
    elif :
        while True:
            if len(p_list) == 0:
                break
            for p in p_list:
                pag.click(pag.center(p), None, 2, 0.5)
                time.sleep(3)
                pag.click(random.uniform(299, 337), random.uniform(371, 379), 2, random.uniform(0.5, 1))
                time.sleep(3)
    break



