import pyautogui as pag
import time
import random

def left_partygate():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.1, 0.5))
    # 메뉴
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
    # 던전 버튼
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(38, 144), random.uniform(99, 116), 1, random.uniform(0.3, 0.6))
    # 파티 던전 38, 99 / 144, 116
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 던전 선택
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(x3, x4), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
    # 단계 선택
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(751, 929), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
    # 이동
    time.sleep(random.uniform(12.5, 13.5))
    pag.click(random.uniform(890, 910), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
    # 자동사냥
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(570, 600), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
    # 순간이동
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
