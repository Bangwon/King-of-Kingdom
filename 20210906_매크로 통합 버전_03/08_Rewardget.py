import pyautogui as pag
import keyboard
import time
import random

# 업적 버튼 905, 220 / 930, 250
# 모두받기 810, 1000 / 940, 1020

def left_rewardget():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.1, 0.5))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(905, 930), random.uniform(220, 250), 1, random.uniform(0.1, 0.5))
    # 업적 버튼 905, 220 / 930, 250
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(810, 940), random.uniform(1000, 1020), 2, random.uniform(1, 1.5))
    # 모두받기 810, 1000 / 940, 1020
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.1, 0.5))
    # 나가기 914, 45 / 939, 63
    time.sleep(random.uniform(3.55, 4.12))

def right_rewardget():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.1, 0.5))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(905+960, 930+960), random.uniform(220, 250), 1, random.uniform(0.1, 0.5))
    # 업적 버튼 905, 220 / 930, 250
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(810+960, 940+960), random.uniform(1000, 1020), 2, random.uniform(1, 1.5))
    # 모두받기 810, 1000 / 940, 1020
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.1, 0.5))
    # 나가기 914, 45 / 939, 63
    time.sleep(random.uniform(3.55, 4.12))
