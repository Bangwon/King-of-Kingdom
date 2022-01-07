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

def dailycheck():
    print("Dailycheck Start")
    print(time.ctime())
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540, 545),random.uniform(145, 155), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550, 580),random.uniform(220, 230), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550, 580),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85, 385)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525, 595),random.uniform(230, 240), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525, 595),random.uniform(360, 370), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610, 618),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
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
    pag.click(random.uniform(610+640, 618+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640, 545+640),random.uniform(145, 155), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550+640, 580+640),random.uniform(220, 230), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550+640, 580+640),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85+640, 385)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640, 595+640),random.uniform(230, 240), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640, 595+640),random.uniform(360, 370), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640, 618+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
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
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640+640, 545+640+640),random.uniform(145, 155), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550+640+640, 580+640+640),random.uniform(220, 230), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550+1280, 580+1280),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85+640+640, 385)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(230, 240), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(360, 370), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
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
    pag.click(random.uniform(610, 618),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540, 545),random.uniform(145+400, 155+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550, 580),random.uniform(220+400, 230+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550, 580),random.uniform(350+400, 360+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85, 385+400)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525, 595),random.uniform(230+400, 240+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525, 595),random.uniform(360+400, 370+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610, 618),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
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
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640, 545+640),random.uniform(145+400, 155+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550+640, 580+640),random.uniform(220+400, 230+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550+640, 580+640),random.uniform(350+400, 360+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85+640, 385+400)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640, 595+640),random.uniform(230+400, 240+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640, 595+640),random.uniform(360+400, 370+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
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
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640+640, 545+640+640),random.uniform(145+400, 155+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(550+640+640, 580+640+640),random.uniform(220+400, 230+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌4
    pag.click(random.uniform(550+1280, 580+1280),random.uniform(350+400, 360+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌1
    pag.moveTo(85+640+640, 385+400)
    pag.drag(0, -650, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(230+400, 240+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(360+400, 370+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 나가기
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Dailycheck End")
    print(time.ctime())

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


# 땅 450, 500, 200, 230
# 이벤트 580, 610, 200, 230
# 1단계 425, 430, 129, 134
# 글루디오 던전 320, 370, 200, 230
def dailygate(x1, x2, y1, y2):
    #1번 케릭
    print("Dailygate Start")
    print(time.ctime())
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580, 585), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584, 594), random.uniform(357, 367), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
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
    pag.click(random.uniform(610+640, 618+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584+640, 594+640), random.uniform(357, 367), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
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
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584+640+640, 594+640+640), random.uniform(357, 367), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
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
    pag.click(random.uniform(610, 618), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580, 585), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1, x2), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584, 594), random.uniform(357+400, 367+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
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
    pag.click(random.uniform(610+640, 618+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584+640, 594+640), random.uniform(357+400, 367+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
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
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(584+640+640, 594+640+640), random.uniform(357+400, 367+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #순간이동
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Dailygate End")
    print(time.ctime())

def fieldgate(x1, x2, y1, y2):
    print("Filedgate Start")
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
    pag.click(random.uniform(580, 585), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320, 340), random.uniform(80, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585, 590), random.uniform(240, 245), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
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
    pag.click(random.uniform(610+640, 618+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640, 340+640), random.uniform(80, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640, 590+640), random.uniform(240, 245), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
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
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145, 150), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640+640, 340+640+640), random.uniform(80, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640+640, 590+640+640), random.uniform(240, 245), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
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
    pag.click(random.uniform(610, 618), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580, 585), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320, 340), random.uniform(80+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1, x2), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585, 590), random.uniform(240+400, 245+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
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
    pag.click(random.uniform(610+640, 618+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640, 340+640), random.uniform(80+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640, 590+640), random.uniform(240+400, 245+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
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
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53+400, 59+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145+400, 150+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640+640, 340+640+640), random.uniform(80+400, 90+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1+400, y2+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129+400, 134+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250+400, 265+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640+640, 590+640+640), random.uniform(240+400, 245+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(15+640+640, 299+400, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+400, 235+400), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
    print("Filedgate End")
    print(time.ctime())

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

schedule.every().day.at("10:01:00").do(gotodesktop2)
schedule.every().day.at("10:02:00").do(dailygate, x1=450, x2=500, y1=200, y2=230)
schedule.every().day.at("10:09:00").do(dailycheck)
schedule.every().day.at("10:16:00").do(rewardget)
schedule.every().day.at("10:23:00").do(gotodesktop1)
schedule.every().day.at("11:03:00").do(gotodesktop2)
schedule.every().day.at("11:04:00").do(fieldgate, x1=320, x2=370, y1=200, y2=230)
schedule.every().day.at("11:11:00").do(rewardget)
schedule.every().day.at("11:18:00").do(gotodesktop1)
schedule.every().day.at("20:45:00").do(gotodesktop2)
schedule.every().day.at("20:53:00").do(rewardget)
schedule.every().day.at("21:01:00").do(rewardget)
schedule.every().day.at("21:08:00").do(dailyquest)
schedule.every().day.at("21:23:00").do(gotodesktop1)
schedule.every(5).minutes.do(time1)
schedule.every().monday.at("21:15:00").do(buyticket)
schedule.every().thursday.at("21:15:00").do(buyticket)
schedule.every().saturday.at("21:15:00").do(buyticket)

# buyticket()
# gotodesktop2()
# dailygate(450, 500, 200, 230)
# dailycheck()
# rewardget()
# gotodesktop1()
# gotodesktop2()
# fieldgate()
# rewardget()
# gotodesktop1()
# gotodesktop2()
# dailygate()
# rewardget()
# rewardget()
# dailyquest()
# gotodesktop1()
# gotodesktop2()
# fieldgate()
# gotodesktop1()

while True:
    schedule.run_pending()
    time.sleep(1)
