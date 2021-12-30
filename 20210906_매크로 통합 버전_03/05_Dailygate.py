import datetime
import pyautogui as pag
import time
import keyboard
import random
from PIL import ImageGrab

pag.FAILSAFE = False


def left_dailygate(x1, x2, y1, y2, x3, x4, y3, y4):
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴 버튼
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
    # 던전 버튼
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(182, 287), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
    # 정예 던전
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
    time.sleep(random.uniform(14.5, 15.5))
def right_dailygate(x1, x2, y1, y2, x3, x4, y3, y4):
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴 버튼
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(727+960, 751+960), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
    # 던전 버튼
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(182+960, 287+960), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
    # 정예 던전
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 여름의 섬
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(x3+960, x4+960), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
    # 1단계
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(751+960, 929+960), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
    # 이동
    time.sleep(random.uniform(12.5, 13.5))
    pag.click(random.uniform(890+960, 910+960), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
    # 자동사냥
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(570+960, 600+960), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
    # 순간이동
    time.sleep(random.uniform(14.5, 15.5))
def left_buy_potion(x1, x2, y1, y2):
    time.sleep(random.uniform(3.11, 4.22))
    pag.click(random.uniform(760, 785), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
    # 소모품 상인
    time.sleep(random.uniform(15.11, 16.22))
    pag.click(random.uniform(30, 280), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
    # 소형 HP 회복 물약
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(550, 610), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
    # 최대 버튼
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(500, 600), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
    # 물약 구매
    time.sleep(random.uniform(1.11, 2.22))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 미드 순간 이동 주문서 30, 280, 535, 575
    # 요툰 순간 이동 주문서 21, 280, 609, 655
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(550, 610), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
    # 최대 버튼
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(500, 600), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
    # 물약 구매
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
    # 장비창 나가기
    time.sleep(random.uniform(4.5, 5.5))
def right_buy_potion(x1, x2, y1, y2):
    time.sleep(random.uniform(3.11, 4.22))
    pag.click(random.uniform(760+960, 785+960), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
    # 소모품 상인
    time.sleep(random.uniform(15.11, 16.22))
    pag.click(random.uniform(30+960, 280+960), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
    # 소형 HP 회복 물약
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(550+960, 610+960), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
    # 최대 버튼
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(500+960, 600+960), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
    # 물약 구매
    time.sleep(random.uniform(1.11, 2.22))
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 미드 순간 이동 주문서 30, 280, 535, 575
    # 요툰 순간 이동 주문서 30, 280, 609, 655
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(550+960, 610+960), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
    # 최대 버튼
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(500+960, 600+960), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
    # 구매
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
    # 장비창 나가기
    time.sleep(random.uniform(4.5, 5.5))
# 미드 순간 이동 주문서 30, 280, 535, 575
# 요툰 순간 이동 주문서 21, 280, 609, 655
def left_prisongate(x1, x2, y1, y2, x3, x4, y3, y4):
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
    pag.drag(-700, 0, 1)
    # 드래그
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x3, x4), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
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
            pag.drag(-700, 0, 1)
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
            # 파티장에게 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270
            
        else :
            time.sleep(1)
            print(time.ctime())

def left_prison_gateend(x1, x2, y1, y2, x3, x4, y3, y4):
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
            pag.drag(-700, 0, 1)
            # 드래그
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
            # 지하 감옥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x3, x4), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
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
            # 파티장에게 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270
            
        else :
            time.sleep(1)
            print(time.ctime())

def right_prisongate(x1, x2, y1, y2, x3, x4, y3, y4):
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
    pag.drag(-700, 0, 1)
    # 드래그
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(x3+960, x4+960), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
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
    hp=(840, 846)
    color1=(0,0,0)
    color2=(255,255,255)
    color3=(173,0,0)
    while True:
        screen = ImageGrab.grab()
        rgb1 = screen.getpixel(checkpoint)
        rgb2 = screen.getpixel(skill)
        rgb3 = screen.getpixel(hp)
        if rgb1 == color1:
            time.sleep(random.uniform(40.11, 41.15))
            break
        
        elif rgb2 == color2:
            pag.click(625, 765, 3, 1)

        elif rgb3 == color3:
            print(rgb3)
            print(time.ctime())
            time.sleep(1)
            
        else :
            time.sleep(1)
            print(time.ctime())
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(20+960, 30+960), random.uniform(260, 270), 1, random.uniform(0.3, 0.6))
            # 던전 나가기 20, 260 / 30, 270
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(490+960, 605+960), random.uniform(600, 620), 1, random.uniform(0.3, 0.6))
            # 나가기 490, 600 / 605, 620       
            time.sleep(random.uniform(15.11, 16.22))
            pag.click(random.uniform(760+960, 785+960), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
            # 소모품 상인
            time.sleep(random.uniform(4.11, 5.22))
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
            pag.moveTo(890+960, 380+960)
            pag.drag(-700, 0, 1)
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
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(917+960, 930+960), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
            # 파티 917, 170 / 930, 185
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(880+960, 900+960), random.uniform(295, 310), 1, random.uniform(0.3, 0.6))
            # 파티장에게 이동 800, 295 / 900, 310

def left_gateend(x1, x2, y1, y2, x3, x4, y3, y4):
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
            print(time.ctime())
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
            time.sleep(random.uniform(14.11, 15.22))
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
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
            # 메뉴 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
            # 던전 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(182, 287), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
            # 정예 던전
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

        else :
            time.sleep(1)
            print(time.ctime())

def right_gateend(x1, x2, y1, y2, x3, x4, y3, y4):
    checkpoint=(25+960,50)
    skill=(625+960, 765)
    death=(545+960, 893)
    color1=(0,0,0)
    color2=(255,255,255)
    color3=(230,0,0)
    while True:
        screen = ImageGrab.grab()
        rgb1 = screen.getpixel(checkpoint)
        rgb2 = screen.getpixel(skill)
        rgb3 = screen.getpixel(death)
        if rgb1 == color1:
            print(time.ctime())
            time.sleep(random.uniform(40.11, 41.15))
            break
        
        elif rgb2 == color2:
            pag.click(625+960, 765, 3, 1)
                    
        elif rgb3 == color3:
            print(time.ctime())
            time.sleep(random.uniform(7.5, 8.5))
            pag.click(random.uniform(520+960, 635+960), random.uniform(930, 950), 1, random.uniform(0.3, 0.6))
            # 마을에서 부활 520, 930 / 635, 950
            time.sleep(random.uniform(15.11, 16.22))
            pag.click(random.uniform(760+960, 785+960), random.uniform(895,920), 1, random.uniform(0.3, 0.6))
            # 소모품 상인
            time.sleep(random.uniform(14.11, 15.22))
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
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
            # 메뉴 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(727+960, 751+960), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
            # 던전 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(182+960, 287+960), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
            # 정예 던전
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
            # 던전 선택
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(x3+960, x4+960), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
            # 단계 선택
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(751+960, 929+960), random.uniform(971, 1007), 1, random.uniform(0.3, 0.6))
            # 이동
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(890+960, 910+960), random.uniform(880, 900), 1, random.uniform(0.3, 0.6))
            # 자동사냥
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(570+960, 600+960), random.uniform(965, 1000), 1, random.uniform(0.3, 0.6))
            # 순간이동
            time.sleep(random.uniform(4.5, 5.5))

        else :
            time.sleep(1)
            print(time.ctime())

def gateend(x1, x2, y1, y2, x3, x4, y3, y4):
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
            print(time.ctime())
            time.sleep(random.uniform(4.11, 5.15))
            rightcp=(25+960,50)
            color1=(0,0,0)
            while True:
                screen = ImageGrab.grab()
                rgb4 = screen.getpixel(rightcp)
                if rgb4 == color1:
                    print(time.ctime())
                    time.sleep(random.uniform(40.11, 41.15))
                    break
                else :
                    time.sleep(1)
                    print(time.ctime())
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
            time.sleep(random.uniform(14.11, 15.22))
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
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
            # 메뉴 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(727, 751), random.uniform(403, 431), 1, random.uniform(0.3, 0.6))
            # 던전 버튼
            time.sleep(random.uniform(4.5, 5.5))
            pag.click(random.uniform(182, 287), random.uniform(99, 117), 1, random.uniform(0.3, 0.6))
            # 정예 던전
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

        else :
            time.sleep(1)
            print(time.ctime())

def prison_gateend(x1, x2, y1, y2, x3, x4, y3, y4):
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
            print(time.ctime())
            time.sleep(random.uniform(4.11, 5.15))
            rightcp=(25+960,50)
            color1=(0,0,0)
            while True:
                screen = ImageGrab.grab()
                rgb4 = screen.getpixel(rightcp)
                if rgb4 == color1:
                    print(time.ctime())
                    time.sleep(random.uniform(40.11, 41.15))
                    break
                else :
                    time.sleep(1)
                    print(time.ctime())
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
            pag.drag(-700, 0, 1)
            # 드래그
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
            # 지하 감옥
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(x3, x4), random.uniform(y3, y4), 1, random.uniform(0.3, 0.6))
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
            # 파티장에게 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270

        else :
            time.sleep(1)
            print(time.ctime())

def left_returntotown():
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(19, 33), random.uniform(255, 267), 1, random.uniform(0.1, 0.3))
    # 귀환 19, 255 / 33, 267
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(490, 600), random.uniform(600, 615), 1, random.uniform(0.1, 0.3))
    # 귀환 확인 490, 600 / 600, 615
    time.sleep(random.uniform(10.5, 14.7))
def right_returntotown():
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(19+960, 33+960), random.uniform(255, 267), 1, random.uniform(0.1, 0.3))
    # 귀환 19, 255 / 33, 267
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(490+960, 600+960), random.uniform(600, 615), 1, random.uniform(0.1, 0.3))
    # 귀환 확인 490, 600 / 600, 615
    time.sleep(random.uniform(10.5, 14.7))

def left_itemunequip():
    time.sleep(random.uniform(4.55, 5.65))
    pag.click(random.uniform(852, 872), random.uniform(46, 64), 1, random.uniform(0.1, 0.3))
    # 장비창 열기
    time.sleep(random.uniform(1, 2))
    pag.click(random.uniform(26, 65), random.uniform(330, 360), 2, random.uniform(0.1, 0.3))
    # 무기 해제 
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26, 65), random.uniform(400, 430), 2, random.uniform(0.1, 0.3))
    # 투구 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26, 65), random.uniform(470, 500), 2, random.uniform(0.1, 0.3))
    # 갑옷 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26, 65), random.uniform(540, 570), 2, random.uniform(0.1, 0.3))
    # 장갑 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26, 65), random.uniform(610, 640), 2, random.uniform(0.1, 0.3))
    # 신발 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26, 65), random.uniform(680, 710), 2, random.uniform(0.1, 0.3))
    # 망토 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(330, 360), 2, random.uniform(0.1, 0.3))
    # 목걸이 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(400, 430), 2, random.uniform(0.1, 0.3))
    # 귀걸이 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(470, 500), 2, random.uniform(0.1, 0.3))
    # 팔찌 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(540, 570), 2, random.uniform(0.1, 0.3))
    # 반지 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(610, 640), 2, random.uniform(0.1, 0.3))
    # 벨트 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530, 560), random.uniform(680, 700), 2, random.uniform(0.1, 0.3))
    # 호른 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(455, 490), random.uniform(670, 700), 2, random.uniform(0.1, 0.3))
    # 문장 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(455, 490), random.uniform(600, 630), 2, random.uniform(0.1, 0.3))
    # 완장 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 장비창 나가기
    time.sleep(random.uniform(3.1, 4.99))
    pag.click(random.uniform(660, 690), random.uniform(965, 990), 1, random.uniform(0.3, 0.6))
    # 창고 가기
    time.sleep(random.uniform(15.11, 16.99))
    pag.click(random.uniform(600, 650), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670, 720), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740, 790), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810, 860), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880, 930), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600, 650), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670, 720), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740, 790), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810, 860), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880, 930), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600, 650), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670, 720), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740, 790), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810, 860), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880, 930), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600, 650), random.uniform(350, 390), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670, 720), random.uniform(350, 390), 1, random.uniform(0.3, 0.6))
    # 아이템 창고 보관
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(840, 930), random.uniform(995, 1015), 1, random.uniform(0.3, 0.6))
    # 보관 버튼
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
    # 창고 나가기
    time.sleep(random.uniform(4.5, 5.5))
def right_itemunequip():
    time.sleep(random.uniform(4.55, 5.65))
    pag.click(random.uniform(852+960, 872+960), random.uniform(46, 64), 1, random.uniform(0.1, 0.3))
    # 장비창 열기
    time.sleep(random.uniform(1, 2))
    pag.click(random.uniform(26+960, 65+960), random.uniform(330, 360), 2, random.uniform(0.1, 0.3))
    # 무기 해제 
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26+960, 65+960), random.uniform(400, 430), 2, random.uniform(0.1, 0.3))
    # 투구 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26+960, 65+960), random.uniform(470, 500), 2, random.uniform(0.1, 0.3))
    # 갑옷 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26+960, 65+960), random.uniform(540, 570), 2, random.uniform(0.1, 0.3))
    # 장갑 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26+960, 65+960), random.uniform(610, 640), 2, random.uniform(0.1, 0.3))
    # 신발 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(26+960, 65+960), random.uniform(680, 710), 2, random.uniform(0.1, 0.3))
    # 망토 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 56+9600), random.uniform(330, 360), 2, random.uniform(0.1, 0.3))
    # 목걸이 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 560+960), random.uniform(400, 430), 2, random.uniform(0.1, 0.3))
    # 귀걸이 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 560+960), random.uniform(470, 500), 2, random.uniform(0.1, 0.3))
    # 팔찌 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 560+960), random.uniform(540, 570), 2, random.uniform(0.1, 0.3))
    # 반지 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 560+960), random.uniform(610, 640), 2, random.uniform(0.1, 0.3))
    # 벨트 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(530+960, 560+960), random.uniform(680, 700), 2, random.uniform(0.1, 0.3))
    # 호른 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(455+960, 490+960), random.uniform(670, 700), 2, random.uniform(0.1, 0.3))
    # 문장 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(455+960, 490+960), random.uniform(600, 630), 2, random.uniform(0.1, 0.3))
    # 완장 해제
    time.sleep(random.uniform(0.55, 1.19))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 장비창 나가기
    time.sleep(random.uniform(3.1, 4.99))
    pag.click(random.uniform(660+960, 690+960), random.uniform(965, 990), 1, random.uniform(0.3, 0.6))
    # 창고 가기
    time.sleep(random.uniform(15.11, 16.99))
    pag.click(random.uniform(600+960, 650+960), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670+960, 720+960), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740+960, 790+960), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810+960, 860+960), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880+960, 930+960), random.uniform(140, 180), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600+960, 650+960), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670+960, 720+960), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740+960, 790+960), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810+960, 860+960), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880+960, 930+960), random.uniform(210, 250), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600+960, 650+960), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670+960, 720+960), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(740+960, 790+960), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(810+960, 860+960), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(880+960, 930+960), random.uniform(280, 320), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(600+960, 650+960), random.uniform(350, 390), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(670+960, 720+960), random.uniform(350, 390), 1, random.uniform(0.3, 0.6))
    # 아이템 창고 보관
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(840+960, 930+960), random.uniform(995, 1015), 1, random.uniform(0.3, 0.6))
    # 보관 버튼
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
    # 창고 나가기
    time.sleep(random.uniform(4.5, 5.5))

def left_itemequip():
    time.sleep(random.uniform(40, 41))
    pag.click(random.uniform(660, 690), random.uniform(965, 990), 1, random.uniform(0.3, 0.6))
    # 창고가기
    time.sleep(random.uniform(10, 11))
    pag.click(random.uniform(30, 70), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100, 140), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170, 210), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240, 280), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30, 70), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100, 140), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170, 210), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240, 280), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30, 70), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100, 140), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170, 210), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240, 280), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30, 70), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100, 140), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170, 210), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240, 280), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30, 70), random.uniform(500, 540), 1, random.uniform(0.3, 0.6))
    # 창고 아이템 클릭
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(190, 285), random.uniform(995, 1015), 1, random.uniform(0.3, 0.6))
    # 꺼내기 버튼 
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 나가기 버튼
    time.sleep(random.uniform(1.001, 1.55))
    pag.click(random.uniform(852, 872), random.uniform(46, 64), 1, random.uniform(0.1, 0.3))
    # 장비창 열기
    time.sleep(random.uniform(3.001, 4.005))
    pag.click(random.uniform(840, 930), random.uniform(1000, 1015), 1, 0.5)
    # 자동 장착
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 나가기 버튼
    time.sleep(random.uniform(4.5, 5.5))
def right_itemequip():
    time.sleep(random.uniform(40, 41))
    pag.click(random.uniform(660+960, 690+960), random.uniform(965, 990), 1, random.uniform(0.3, 0.6))
    # 창고가기
    time.sleep(random.uniform(10, 11))
    pag.click(random.uniform(30,+960, 70+960), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100+960, 140+960), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170+960, 210+960), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240+960, 280+960), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30+960, 70+960), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100+960, 140+960), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170+960, 210+960), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240+960, 280+960), random.uniform(290, 330), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30+960, 70+960), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100+960, 140+960), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170+960, 210+960), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240+960, 280+960), random.uniform(360, 400), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30+960, 70+960), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(100+960, 140+960), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(170+960, 210+960), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(240+960, 280+960), random.uniform(430, 470), 1, random.uniform(0.3, 0.6))
    pag.click(random.uniform(30+960, 70+960), random.uniform(500, 540), 1, random.uniform(0.3, 0.6))
    # 창고 아이템 클릭
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(190+960, 285+960), random.uniform(995, 1015), 1, random.uniform(0.3, 0.6))
    # 꺼내기 버튼 
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 나가기 버튼
    time.sleep(random.uniform(1.001, 1.55))
    pag.click(random.uniform(852+960, 872+960), random.uniform(46, 64), 1, random.uniform(0.1, 0.3))
    # 장비창 열기
    time.sleep(random.uniform(3.001, 4.005))
    pag.click(random.uniform(840+960, 930+960), random.uniform(1000, 1015), 1, 0.5)
    # 자동 장착
    time.sleep(random.uniform(1.55, 2.12))
    pag.click(random.uniform(914+960, 939+960), random.uniform(45, 63), 1, random.uniform(0.1, 0.3))
    # 나가기 버튼
    time.sleep(random.uniform(4.5, 5.5))

def ctchange():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(726, 753), random.uniform(504, 532), 1, random.uniform(0.3, 0.6))
    # 케릭터 변경
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(488, 605), random.uniform(596, 617), 1, random.uniform(0.3, 0.6))
    # 캐릭터 선택 화면 이동 확인
    time.sleep(random.uniform(4.55, 5.12))

def ctselect(x1, x2, y1, y2):
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2))
    # 케릭터 선택
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(745, 920), random.uniform(975, 1005))
    # 게임시작하기
    time.sleep(random.uniform(10.5, 11.11))
# 첫 번째 (760, 915, 100, 130)
# 두 번째 (760, 915, 180, 215)
# 세 번째 (760, 915, 270, 290)
# 네 번째 (760, 915, 355, 375)
# 다섯 번째 (760, 915, 440, 460)

# 그림자 성채 37, 303, 373, 530
# 공허의 유적 349, 625, 377, 530
# 난쟁이 비밀 통로 661, 917, 375, 530
# 지하 감옥 650, 905, 380, 530
# 1단계 x3, x4, y3, y4 (23, 285, 99, 130)
# 2단계 (23, 282, 155, 185)
# 3단계 (23, 285, 215, 245)
# 6단계 23, 285, 385, 420


def oneclickgate():
    left_gateend()
    left_buy_potion()
    left_prisongate()

left_dailygate(349, 625, 377, 530, 23, 282, 155, 185)