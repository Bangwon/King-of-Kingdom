import pyautogui as pag
import random
import time
from PIL import ImageGrab
import schedule
pag.FAILSAFE=False


def left_prisongate(x1, x2, y1, y2):
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴 버튼
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
    # 던전 버튼
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(182, 287), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
    # 정예 던전
    time.sleep(random.uniform(2.5, 3.5))
    pag.moveTo(890, 380)
    pag.drag(-500, 0, 1)
    # 드래그
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(650, 905), random.uniform(380, 530), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 1단계
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(751, 929), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
    # 이동
    time.sleep(random.uniform(12.5, 13.5))
    pag.click(random.uniform(890, 910), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
    # 자동사냥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(570, 600), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
    # 순간이동
    time.sleep(random.uniform(4.5, 5.5))
    checkpoint=(25,50)
    skill=(625, 765)
    death=(545, 893)
    color1=(0,0,0)
    color2=(255,255,255)
    color3=(230,0,0)
    while True:
        screen = ImageGrab.grab()
        rgb1 = screen.getpixel(checkpoint)
        rgb2 = screen.getpixel(skill)
        rgb3 = screen.getpixel(death)
        if rgb1 == color1:
            time.sleep(random.uniform(40.11, 41.15))
            break
        
        elif rgb2 == color2:
            pag.click(625, 765, 3, 1)

        elif rgb3 == color3:
            print(time.ctime())
            time.sleep(random.uniform(7.5, 8.5))
            pag.click(random.uniform(520, 635), random.uniform(930, 950), 1, random.uniform(0.3, 0.6))
            # 마을에서 부활 520, 930 / 635, 950
            time.sleep(random.uniform(15.11, 16.22))
            pag.click(random.uniform(760, 785), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
            # 소모품 상인
            time.sleep(random.uniform(24.11, 25.22))
            pag.click(random.uniform(90, 280), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
            # 소형 HP 회복 물약
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(550, 610), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
            # 최대 버튼
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(500, 600), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
            # 물약 구매
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
            # 장비창 나가기
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
            # 메뉴 버튼
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
            # 던전 버튼
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(182, 287), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
            # 정예 던전
            time.sleep(random.uniform(2.5, 3.5))
            pag.moveTo(890, 380)
            pag.drag(-500, 0, 1)
            # 드래그
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(650, 905), random.uniform(380, 530), 1, random.uniform(0.3, 0.6))
            # 지하 감옥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
            # 1단계
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(751, 929), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
            # 이동
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(890, 910), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
            # 자동사냥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(570, 600), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
            # 순간이동
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(917, 930), random.uniform(170, 185), 1, random.uniform(0.3, 0.6))
            # 파티 917, 170 / 930, 185
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(880, 900), random.uniform(260, 270), 1, random.uniform(0.3, 0.6))
            # 파티장에게 4명 파티 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270
            
        else :
            time.sleep(10)
            print(time.ctime())

def right_prisongate(x1, x2, y1, y2):
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴 버튼
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(727+960, 751+960), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
    # 던전 버튼
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(182+960, 287+960), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
    # 정예 던전
    time.sleep(random.uniform(2.5, 3.5))
    pag.moveTo(890+960, 380+960)
    pag.drag(-500, 0, 1)
    # 드래그
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(650+960, 905+960), random.uniform(380, 530), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 1단계
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(751+960, 929+960), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
    # 이동
    time.sleep(random.uniform(12.5, 13.5))
    pag.click(random.uniform(890+960, 910+960), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
    # 자동사냥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(570+960, 600+960), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
    # 순간이동
    time.sleep(random.uniform(4.5, 5.5))
    checkpoint=(25,50)
    skill=(625, 765)
    death=(545, 893)
    color1=(0,0,0)
    color2=(255,255,255)
    color3=(230,0,0)
    while True:
        screen = ImageGrab.grab()
        rgb1 = screen.getpixel(checkpoint)
        rgb2 = screen.getpixel(skill)
        rgb3 = screen.getpixel(death)
        if rgb1 == color1:
            time.sleep(random.uniform(40.11, 41.15))
            break
        
        elif rgb2 == color2:
            pag.click(625, 765, 3, 1)

        elif rgb3 == color3:
            print(time.ctime())
            time.sleep(random.uniform(7.5, 8.5))
            pag.click(random.uniform(520+960, 635+960), random.uniform(930, 950), 1, random.uniform(0.3, 0.6))
            # 마을에서 부활 520, 930 / 635, 950
            time.sleep(random.uniform(15.11, 16.22))
            pag.click(random.uniform(760+960, 785+960), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
            # 소모품 상인
            time.sleep(random.uniform(24.11, 25.22))
            pag.click(random.uniform(90+960, 280+960), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
            # 소형 HP 회복 물약
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(550+960, 610+960), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
            # 최대 버튼
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(500+960, 600+960), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
            # 물약 구매
            time.sleep(random.uniform(2, 3.4))
            pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
            # 장비창 나가기
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
            # 메뉴 버튼
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(727+960, 751+960), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
            # 던전 버튼
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(182+960, 287+960), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
            # 정예 던전
            time.sleep(random.uniform(2.5, 3.5))
            pag.moveTo(890+960, 380)
            pag.drag(-500, 0, 1)
            # 드래그
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(650+960, 905+960), random.uniform(380, 530), 1, random.uniform(0.3, 0.6))
            # 지하 감옥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
            # 1단계
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(751+960, 929+960), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
            # 이동
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(890+960, 910+960), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
            # 자동사냥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(570+960, 600+960), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
            # 순간이동
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(917+960, 930+960), random.uniform(170, 185), 1, random.uniform(0.3, 0.6))
            # 파티 917, 170 / 930, 185
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(880+960, 900+960), random.uniform(260, 270), 1, random.uniform(0.3, 0.6))
            # 파티장에게 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270
            
        else :
            time.sleep(10)
            print(time.ctime())
