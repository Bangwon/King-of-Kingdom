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

def rewardget():
    print("Rewardget Start")
    print(time.ctime())
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579, 587), random.uniform(230, 238), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339, 385), random.uniform(367, 372), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350), random.uniform(290, 295), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303, 362), random.uniform(83, 91), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339, 390), random.uniform(367, 372), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350), random.uniform(290, 295), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #2번 케릭
    pag.moveTo(316+640, 225)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640, 587+640),random.uniform(230, 238),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640, 390+640),random.uniform(367, 372),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290, 295),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640, 362+640),random.uniform(83, 91),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640, 390+640),random.uniform(367, 372),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290, 295),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #3번 케릭
    pag.moveTo(316+640+640, 225)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640+640, 587+640+640),random.uniform(230, 238),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367, 372),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290, 295),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640+640, 362+640+640),random.uniform(83, 91),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367, 372),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290, 295),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    pag.moveTo(316, 213+400)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579, 587),random.uniform(230+400, 238+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339, 390),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303, 362),random.uniform(83+400, 91+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339, 390),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #5번 케릭
    pag.moveTo(316+640, 225+400)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640, 587+640),random.uniform(230+400, 238+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640, 390+640),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640, 362+640),random.uniform(83+400, 91+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640, 390+640),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #6번 케릭
    pag.moveTo(316+640+640, 225+400)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640+640, 587+640+640),random.uniform(230+400, 238+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640+640, 362+640+640),random.uniform(83+400, 91+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367+400, 372+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290+400, 295+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Rewardget End")
    print(time.ctime())

def dailycheck(x, y):
    print("Dailycheck Start")
    print(time.ctime())
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+x, 213+y)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+x, 618+x),random.uniform(53+y, 59+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+x, 545+x),random.uniform(145+y, 155+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550+x, 580+x),random.uniform(220+y, 230+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550+x, 580+x),random.uniform(350+y, 360+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85+x, 385+y)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+x, 595+x),random.uniform(230+y, 240+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+x, 595+x),random.uniform(360+y, 370+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(134+x, 159+x),random.uniform(82+y, 92+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #혈맹
    pag.click(random.uniform(548+x, 591+x),random.uniform(218+y, 228+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #혈맹 체크1
    pag.click(random.uniform(548+x, 591+x),random.uniform(350+y, 360+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #혈맹 체크2
    pag.click(random.uniform(610+x, 618+x),random.uniform(53+y, 59+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Dailycheck End")
    print(time.ctime())

def dailycheckall():
    dailycheck(0, 0)
    dailycheck(640, 0)
    dailycheck(1280, 0)
    dailycheck(0, 400)
    dailycheck(640, 400)
    dailycheck(1280, 400)

def dailyquest():
    print("Dailyquest Start")
    print(time.ctime())
    #1번 케릭
    autoexit1(0, 0)
    pag.click(random.uniform(580, 585),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230, 250),random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510, 530),random.uniform(365, 375), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610, 618), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #2번 케릭
    autoexit1(640, 0)
    pag.click(random.uniform(580+640, 585+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230+640, 250+640),random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510+640, 530+640),random.uniform(365, 375), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610+640, 618+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #3번 케릭
    autoexit1(1280, 0)
    pag.click(random.uniform(580+640+640, 585+640+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230+640+640, 250+640+640),random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510+640+640, 530+640+640),random.uniform(365, 375), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    autoexit1(0, 400)
    pag.click(random.uniform(580, 585),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230, 250),random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510, 530),random.uniform(365+400, 375+400), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610, 618), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    autoexit1(640, 400)
    pag.click(random.uniform(580+640, 585+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230+640, 250+640),random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510+640, 530+640),random.uniform(365+400, 375+400), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610+640, 618+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    autoexit1(1280, 400)
    pag.click(random.uniform(580+640+640, 585+640+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230+640+640, 250+640+640),random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510+640+640, 530+640+640),random.uniform(365+400, 375+400), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Dailyquest End")
    print(time.ctime())

def dailygate(x1, x2, y1, y2, x3, y3):
    #1번 케릭
    print("Dailygate Start")
    print(time.ctime())
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+x3, 213+y3)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+x3, 618+x3), random.uniform(53+y3, 59+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+x3, 585+x3), random.uniform(145+y3, 150+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+x3, x2+x3), random.uniform(y1+y3, y2+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+x3, 430+x3), random.uniform(129+y3, 134+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+x3, 370+x3), random.uniform(250+y3, 265+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+x3, 590+x3), random.uniform(240+y3, 245+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(random.uniform(584+x3, 594+x3), random.uniform(357+y3, 367+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
    pag.click(15+x3, 299+y3, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x3, 330+x3), random.uniform(215+y3, 235+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    print("Dailygate End")
    print(time.ctime())

def dailygateall():
    dailygate(450, 500, 200, 230, 0, 0)
    dailygate(450, 500, 200, 230, 640, 0)
    dailygate(450, 500, 200, 230, 1280, 0)
    dailygate(450, 500, 200, 230, 0, 400)
    # dailygate(450, 500, 200, 230, 640, 400)
    # dailygate(450, 500, 200, 230, 1280, 400)

def fieldgate(x1, x2, y1, y2, x3, y3):
    print("Filedgate Start")
    print(time.ctime())
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+x3, 213+y3)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+x3, 618+x3), random.uniform(53+y3, 59+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+x3, 585+x3), random.uniform(145+y3, 150+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+x3, 340+x3), random.uniform(80+y3, 90+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+x3, x2+x3), random.uniform(y1+y3, y2+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+x3, 430+x3), random.uniform(129+y3, 134+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+x3, 370+x3), random.uniform(250+y3, 265+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+x3, 590+x3), random.uniform(240+y3, 245+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(15+x3, 299+y3, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x3, 330+x3), random.uniform(215+y3, 235+y3), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    print("Filedgate End")
    print(time.ctime())

def fieldgateall():
    fieldgate(320, 370, 200, 230, 0, 0)
    fieldgate(320, 370, 200, 230, 640, 0)
    fieldgate(320, 370, 200, 230, 1280, 0)
    fieldgate(320, 370, 200, 230, 0, 400)
    # fieldgate(320, 370, 200, 230, 640, 400)
    # fieldgate(320, 370, 200, 230, 1280, 400)

def buyticket():
    print("Buyticket Start")
    print(time.ctime())
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465, 470), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305, 315), random.uniform(261, 262), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10, 20), random.uniform(342, 350), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305, 325), random.uniform(255, 260), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130, 160), random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20, 40), random.uniform(155, 160), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175, 200), random.uniform(170, 205), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230, 245), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175, 200), random.uniform(307, 340), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230, 245), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #2번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640, 470+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640, 315+640), random.uniform(261, 262), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10+640, 20+640), random.uniform(342, 350), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640, 325+640), random.uniform(255, 260), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640, 160+640), random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640, 40+640), random.uniform(155, 160), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640, 200+640), random.uniform(170, 205), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640, 200+640), random.uniform(307, 340), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #3번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640+640, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640+640, 470+640+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640+640, 315+640+640), random.uniform(261, 262), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10+640+640, 20+640+640), random.uniform(342, 350), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640+640, 325+640+640), random.uniform(255, 260), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640+640, 160+640+640), random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640+640, 40+640+640), random.uniform(155, 160), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(170, 205), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(307, 340), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260, 268), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315, 320), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53, 59),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드    
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213+400)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465, 470), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305, 315), random.uniform(261+400, 262+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10, 20), random.uniform(342+400, 350+400), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305, 325), random.uniform(255+400, 260+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130, 160), random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20, 40), random.uniform(155+400, 160+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175, 200), random.uniform(170+400, 205+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230, 245), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175, 200), random.uniform(307+400, 340+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230, 245), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640, 213+400)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640, 470+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640, 315+640), random.uniform(261+400, 262+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10+640, 20+640), random.uniform(342+400, 350+400), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640, 325+640), random.uniform(255+400, 260+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640, 160+640), random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640, 40+640), random.uniform(155+400, 160+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640, 200+640), random.uniform(170+400, 205+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640, 200+640), random.uniform(307+400, 340+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640+640, 213+400)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640+640, 470+640+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640+640, 315+640+640), random.uniform(261+400, 262+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(30+640+640, 40+640+640), random.uniform(342+400, 350+400), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640+640, 325+640+640), random.uniform(255+400, 260+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640+640, 160+640+640), random.uniform(83+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640+640, 40+640+640), random.uniform(155+400, 160+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(170+400, 205+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(307+400, 340+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260+400, 268+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315+400, 320+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+400, 59+400),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드    
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Buyticket End")
    print(time.ctime())

def stockitem(x, y):
    autoexit1(x, y)
    pag.click(random.uniform(547+x, 564+x),random.uniform(353+y, 373+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #귀환
    pag.click(random.uniform(506+x, 519+x),random.uniform(49+y, 59+y),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #가방
    pag.click(random.uniform(549+x, 562+x),random.uniform(92+y, 100+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #기타
    pag.click(random.uniform(602+x, 612+x),random.uniform(324+y, 334+y),2, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #정렬
    pag.click(random.uniform(617+x, 625+x),random.uniform(83+y, 91+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #가방나가기   
    pag.click(random.uniform(554+x, 572+x),random.uniform(281+y, 297+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #방위
    pag.click(random.uniform(238+x, 253+x),random.uniform(211+y, 223+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #기능성
    pag.click(random.uniform(200+x, 219+x),random.uniform(206+y, 221+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(23.5, 24.5))
    #창고
    pag.click(random.uniform(544+x, 552+x),random.uniform(91+y, 101+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품

    p_list = pag.locateAllOnScreen("C:\\Users\\ODIN\\ODIN\\LineageW\\braveportion.png", confidence=0.79)
    p_list = list(p_list)
    f1 = [478+x, 122+y]
    f2 = [618+x, 327+y]

    if len(p_list) == 0:
        print("이미지없음")
        time.sleep(2)

    else:
        for p in p_list:
            ctr = pag.center(p)
            if ctr[0] >= f1[0] and ctr[0] <= f2[0] and ctr[1] >= f1[1] and ctr[1] <= f2[1]:
                pag.click(p, None, 1, 0.5)
                time.sleep(3)
                #용기물약 클릭
                pag.click(random.uniform(336+x, 356+x),random.uniform(365+y, 370+y), 1, random.uniform(0.1, 0.3))
                time.sleep(random.uniform(3.5, 4.5))
                #MAX
                pag.click(random.uniform(565+x, 608+x),random.uniform(362+y, 370+y), 1, random.uniform(0.1, 0.3))
                time.sleep(random.uniform(3.5, 4.5))
                #모두 맡기기

    pag.click(random.uniform(593+x, 621+x),random.uniform(46+y, 63+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나가기
    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def stockitemall():
    stockitem(0, 0)
    stockitem(640, 0)
    stockitem(1280, 0)
    stockitem(0, 400)
    # stockitem(640, 400)
    # stockitem(1280, 400)

def buyportion(x, y):
    print("Buyportion Start")
    print(time.ctime())
    #1번 케릭
    autoexit1(x, y)
    # pag.click(random.uniform(547, 564),random.uniform(353, 373), 1, random.uniform(0.1, 0.3))
    # time.sleep(random.uniform(3.5, 4.5))
    # #귀환
    pag.click(random.uniform(554+x, 572+x),random.uniform(281+y, 297+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #방위
    pag.click(random.uniform(385+x, 403+x),random.uniform(210+y, 231+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(418+x, 433+x), random.uniform(211+y, 225+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20.5, 21.5))
    #잡화상인
    pag.click(random.uniform(22+x, 38+x), random.uniform(129+y, 142+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빨간물약
    pag.click(random.uniform(261+x, 283+x), random.uniform(365+y, 375+y), 2, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #100개x2
    pag.click(random.uniform(22+x, 38+x), random.uniform(162+y, 178+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #초록물약
    pag.click(random.uniform(309+x, 328+x), random.uniform(365+y, 375+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #MAX
    pag.click(random.uniform(22+x, 38+x), random.uniform(271+y, 292+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #변신줌서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개X3
    pag.click(random.uniform(22+x, 38+x), random.uniform(310+y, 327+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #마법인형줌서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개X3
    pag.moveTo(52+x, 309+y)
    pag.drag(0, -102, 1.5)
    time.sleep(random.uniform(1, 2))
    pag.click(random.uniform(22+x, 38+x), random.uniform(244+y, 261+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동 주문서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 1, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개
    pag.click(random.uniform(22+x, 38+x), random.uniform(284+y, 296+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #귀환 주문서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 1, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개
    pag.click(random.uniform(564+x, 610+x), random.uniform(360+y, 373+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두구매
    pag.click(random.uniform(575+x, 620+x), random.uniform(50+y, 59+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나가기
    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Buyportion End")
    print(time.ctime())

def buyportiontail(x, y):
    print("Buyportion Start")
    print(time.ctime())
    #1번 케릭
    autoexit1(x, y)
    # pag.click(random.uniform(547, 564),random.uniform(353, 373), 1, random.uniform(0.1, 0.3))
    # time.sleep(random.uniform(3.5, 4.5))
    # #귀환
    pag.click(random.uniform(554+x, 572+x),random.uniform(281+y, 297+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #방위
    pag.click(random.uniform(385+x, 403+x),random.uniform(210+y, 231+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(418+x, 433+x), random.uniform(211+y, 225+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20.5, 21.5))
    #잡화상인
    pag.click(random.uniform(22+x, 38+x), random.uniform(129+y, 142+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빨간물약
    pag.click(random.uniform(261+x, 283+x), random.uniform(365+y, 375+y), 2, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #100개x2
    # pag.click(random.uniform(22+x, 38+x), random.uniform(162+y, 178+y), 1, random.uniform(0.1, 0.3))
    # time.sleep(random.uniform(3.5, 4.5))
    # #초록물약
    # pag.click(random.uniform(309+x, 328+x), random.uniform(365+y, 375+y), 1, random.uniform(0.1, 0.3))
    # time.sleep(random.uniform(3.5, 4.5))
    # #MAX
    pag.click(random.uniform(22+x, 38+x), random.uniform(271+y, 292+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #변신줌서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개X3
    pag.click(random.uniform(22+x, 38+x), random.uniform(310+y, 327+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #마법인형줌서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개X3
    pag.moveTo(52+x, 309+y)
    pag.drag(0, -102, 1.5)
    time.sleep(random.uniform(1, 2))
    pag.click(random.uniform(22+x, 38+x), random.uniform(244+y, 261+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동 주문서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 1, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개
    pag.click(random.uniform(22+x, 38+x), random.uniform(284+y, 296+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #귀환 주문서
    pag.click(random.uniform(219+x, 233+x), random.uniform(365+y, 375+y), 1, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #10개
    pag.click(random.uniform(564+x, 610+x), random.uniform(360+y, 373+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두구매
    pag.click(random.uniform(575+x, 620+x), random.uniform(50+y, 59+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나가기
    pag.click(15+x, 299+y, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+x, 330+x), random.uniform(215+y, 235+y), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Buyportion End")
    print(time.ctime())

def buyportionall():
    buyportion(0, 0)
    buyportion(640, 0)
    # buyportion(1280, 0)
    buyportion(0,400)
    buyportion(640, 400)
    buyportion(1280, 400)

def buyportiontailall():
    buyportiontail(0, 0)
    buyportiontail(640, 0)
    buyportiontail(1280, 0)
    buyportiontail(0,400)
    # buyportiontail(640, 400)
    # buyportiontail(1280, 400)
    
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
    summon1(0, 0)
    summon1(640, 0)
    summon1(1280, 0)
    summon1(0, 400)
    summon1(640, 400)
    summon1(1280, 400)

    
def gotodesktop2():
    pag.click(402, 1052, 1, 0.2)
    time.sleep(4)
    pag.click(299, 61, 1, 0.2)

def gotodesktop1():
    pag.click(402, 1052, 1, 0.2)
    time.sleep(4)
    pag.click(83, 45, 1, 0.2)

def time1():
    print(time.ctime())


# 땅 450, 500, 200, 230
# 이벤트 580, 610, 200, 230
# 1단계 425, 430, 129, 134
# 글루디오 던전 320, 370, 200, 230

schedule.every().day.at("10:01:00").do(gotodesktop2)
schedule.every().day.at("10:02:00").do(stockitemall)
schedule.every().day.at("10:09:00").do(buyportiontailall)
schedule.every().day.at("10:16:00").do(dailygateall)
schedule.every().day.at("10:23:00").do(dailycheckall)
schedule.every().day.at("10:30:00").do(rewardget)
schedule.every().day.at("10:37:00").do(gotodesktop1)
schedule.every().day.at("11:25:00").do(gotodesktop2)
schedule.every().day.at("11:26:00").do(fieldgateall)
schedule.every().day.at("11:33:00").do(rewardget)
schedule.every().day.at("11:40:00").do(gotodesktop1)
schedule.every().day.at("20:52:00").do(gotodesktop2)
schedule.every().day.at("20:53:00").do(rewardget)
schedule.every().day.at("21:01:00").do(rewardget)
schedule.every().day.at("21:08:00").do(dailyquest)
schedule.every().day.at("21:22:00").do(gotodesktop1)
schedule.every(5).minutes.do(time1)
schedule.every().monday.at("21:15:00").do(buyticket)
schedule.every().thursday.at("21:15:00").do(buyticket)
schedule.every().saturday.at("21:15:00").do(buyticket)
schedule.every().sunday.at("21:15:00").do(summon1all)

# stockitem(1280, 0)
# buyportiontail(1280,0)
# buyticket()
# gotodesktop2()
# stockitemall()
# buyportionall()
# dailygateall()
# dailycheckall()
# rewardget()
# gotodesktop1()
# gotodesktop2()
# rewardget()
# gotodesktop1()
# gotodesktop2()
# dailygate()
# rewardget()
# rewardget()
# dailyquest()
# gotodesktop1()
# gotodesktop2()
# fieldgate(320, 370, 200, 230)
# gotodesktop1()

while True:
    schedule.run_pending()
    time.sleep(1)
