import pyautogui as pag
import keyboard
import time
import random



def left_guilddonate():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.1, 0.5))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(670, 689), random.uniform(401, 426), 1, random.uniform(0.1, 0.5))
    # 길드 670, 401 / 689, 426
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(161, 278), random.uniform(97, 122), 2, random.uniform(1, 1.5))
    # 길드 정보 161, 97 / 278, 122
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(270, 374), random.uniform(867, 879), 6, random.uniform(1, 1.5))
    # 일반 기부하기 270, 867 / 374, 879
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.1, 0.5))
    # 나가기 914, 45 / 939, 63
    time.sleep(random.uniform(4.5, 5.5))

def right_guilddonate():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.1, 0.5))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(670+960, 689+960), random.uniform(401, 426), 1, random.uniform(0.1, 0.5))
    # 길드 670, 401 / 689, 426
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(161+960, 278+960), random.uniform(97, 122), 2, random.uniform(1, 1.5))
    # 길드 정보 161, 97 / 278, 122
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(270+960, 374+960), random.uniform(867, 879), 6, random.uniform(1, 1.5))
    # 일반 기부하기 270, 867 / 374, 879
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.1, 0.5))
    # 나가기 914, 45 / 939, 63
    time.sleep(random.uniform(4.5, 5.5))
