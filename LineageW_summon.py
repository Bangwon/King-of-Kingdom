import pyautogui as pag
import random
import time
from PIL import ImageGrab
import schedule
import os

pag.FAILSAFE=False

def autoexit1(x, y):
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+x, 213+y)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제

def summon(x, y):
    autoexit1(x, y)
    pag.click(random.uniform(506+x, 519+x),random.uniform(49+y, 59+y),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #가방
    pag.click(random.uniform(549+x, 562+x),random.uniform(92+y, 100+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #기타
    pag.click(random.uniform(602+x, 612+x),random.uniform(324+y, 334+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #정렬
    a=0
    while a<3:
        p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\summon.png", confidence=0.78)
        p_list = list(p_list)
        if len(p_list) == 0:
            pag.moveTo(496+x, 246+y)
            pag.drag(0, -100, 1)
            time.sleep(3)
            a=a+1
        elif len(p_list) >0 :
            p=pag.center(p_list[0])
            print(p)
            k=0
            while len(p_list)>0:
                pag.click(p[0], p[1], 2, 1)
                time.sleep(3)
                #카드 더블 클릭
                if k == 0:
                    pag.click(random.uniform(587+x, 617+x), random.uniform(61+y, 67+y), 1, random.uniform(0.5, 1))
                    time.sleep(3)
                    #SKIP
                    pag.click(random.uniform(610+x, 613+x), random.uniform(373+y, 376+y), 1, random.uniform(0.5, 1))
                    time.sleep(3)
                    #컷신스킵하기
                    k=+1
                
                elif len(p_list) == 0:
                    break

                else :
                    pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                    time.sleep(3)
                    #소환 확인

    pag.click(random.uniform(506+x, 519+x),random.uniform(49+y, 59+y),2, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #가방
    pag.click(random.uniform(549+x, 562+x),random.uniform(92+y, 100+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #기타
    pag.click(random.uniform(602+x, 612+x),random.uniform(324+y, 334+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #정렬
    b=0
    while b<3:
        p1_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\dollsummon.png", confidence=0.73)
        p1_list = list(p1_list)
        b=b+1
        if len(p1_list) == 0:
            pag.moveTo(496+x, 246+y)
            pag.drag(0, -100, 1)
            time.sleep(3)
            print(p1_list)

        elif len(p1_list) > 0:
            p1=pag.center(p1_list[0])
            print(p1)
            k=0
            while len(p1_list)>0:
                time.sleep(2)
                pag.click(p1[0], p1[1], 2, 1)
                time.sleep(3)
                #카드 더블 클릭
                if k == 0:
                    pag.click(random.uniform(587+x, 617+x), random.uniform(61+y, 67+y), 1, random.uniform(0.5, 1))
                    time.sleep(3)
                    #SKIP
                    pag.click(random.uniform(610+x, 613+x), random.uniform(373+y, 376+y), 1, random.uniform(0.5, 1))
                    time.sleep(3)
                    #컷신스킵하기
                    k=+1

                else :
                    pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                    time.sleep(3)
                    #소환 확인

        else :
            break

        

    time.sleep(random.uniform(3.5, 4.5))    
    pag.click(random.uniform(610+x, 618+x),random.uniform(53+y, 59+y),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def summon1(x, y):
    autoexit1(x, y)
    color = 199, 198, 196
    color1 = 106, 95, 86
    screen=ImageGrab.grab()
    rgb = screen.getpixel((304+x,360+y))
    rgb1 = screen.getpixel((341+x,360+y))
    time.sleep(3)
    #329, 349
    if rgb == color:
        while True:
            pag.click(random.uniform(296+x, 311+x),random.uniform(353+y, 373+y),2, random.uniform(0.5, 1))
            time.sleep(random.uniform(4.5, 5.5))
            #변신클릭
            p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\summon1.png", confidence=0.9)
            p_list = list(p_list)

            if len(p_list) > 0:
                pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                time.sleep(2)
                rgb = screen.getpixel((304+x,306+y))
                print(rgb)
                #소환 확인

            elif not rgb== color :
                break

            else :
                pag.click(random.uniform(587+x, 617+x), random.uniform(61+y, 67+y), 1, random.uniform(0.5, 1))
                time.sleep(3)
                #SKIP
                pag.click(random.uniform(610+x, 613+x), random.uniform(373+y, 376+y), 1, random.uniform(0.5, 1))
                time.sleep(3)
                #컷신스킵하기
                pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                time.sleep(3)
                #소환 확인

    if not rgb == color and rgb1 == color1:
        while True:
            pag.click(random.uniform(332+x, 346+x),random.uniform(353+y, 373+y),2, random.uniform(0.5, 1))
            time.sleep(random.uniform(4.5, 5.5))
            #변신클릭
            p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\summon1.png", confidence=0.9)
            p_list = list(p_list)

            if len(p_list) > 0:
                pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                time.sleep(2)
                rgb1 = screen.getpixel((304+x,306+y))
                print(rgb1)
                #소환 확인

            elif not rgb1== color1 :
                break

            else :
                pag.click(random.uniform(587+x, 617+x), random.uniform(61+y, 67+y), 1, random.uniform(0.5, 1))
                time.sleep(3)
                #SKIP
                pag.click(random.uniform(610+x, 613+x), random.uniform(373+y, 376+y), 1, random.uniform(0.5, 1))
                time.sleep(3)
                #컷신스킵하기
                pag.click(random.uniform(299+x, 337+x), random.uniform(371+y, 379+y), 2, random.uniform(0.5, 1))
                time.sleep(3)
                #소환 확인

    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def summon1all():
    # summon1(0, 0)
    # summon1(640, 0)
    summon1(1280, 0)
    summon1(0, 400)
    summon1(640, 400)
    summon1(1280, 400)

summon1all()