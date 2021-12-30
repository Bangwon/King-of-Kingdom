import pyautogui as pag
import random
import time

def afterLogin():

    pag.click(random.uniform(557, 1244), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 선택

    pag.hotkey('winleft', 'left')
    time.sleep(random.uniform(1.0, 1.5))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 왼쪽 보내기

    pag.click(random.uniform(101, 776), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 재선택

    pag.click(random.uniform(961, 1292), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 선택

    pag.hotkey('winleft', 'right')
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 오른쪽 보내기

    pag.click(random.uniform(1072, 1700), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 재선택

    pag.click(random.uniform(150, 786), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 접속 1 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 접속 1 (우)

    pag.click(random.uniform(150, 786), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 접속 2 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 접속 2 (우)

    pag.click(random.uniform(777, 896), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 게임하기 (좌)
    pag.click(random.uniform(777+960, 896+960), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20, 30))
    # 게임하기 (우)

    pag.click(random.uniform(430, 519), random.uniform(635, 649), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 방치모드확인하기 (좌)
    pag.click(random.uniform(430+960, 519+960), random.uniform(635, 649), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20, 30))
    # 방치모드확인하기 (우)
    ##############로그인 후 접속#############

time.sleep(5)
afterLogin()