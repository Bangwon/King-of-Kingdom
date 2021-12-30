import pyautogui as pag
import random
import time
from PIL import ImageGrab
import schedule

pag.FAILSAFE=False

def rewardget():
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
    pag.click(random.uniform(339, 390), random.uniform(367, 372), 1, random.uniform(0.1, 0.3))
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
    pag.click(11, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(11+640, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(1294, 297, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #4번 케릭
    pag.moveTo(316, 213+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579, 587),random.uniform(230+397, 238+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339, 390),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303, 362),random.uniform(83+397, 91+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339, 390),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280, 350),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(11, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #5번 케릭
    pag.moveTo(316+640, 225+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640, 587+640),random.uniform(230+397, 238+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640, 390+640),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640, 362+640),random.uniform(83+397, 91+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640, 390+640),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640, 350+640),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(11+640, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드


    #6번 케릭
    pag.moveTo(316+640+640, 225+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(579+640+640, 587+640+640),random.uniform(230+397, 238+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(303+640+640, 362+640+640),random.uniform(83+397, 91+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상인
    pag.click(random.uniform(339+640+640, 390+640+640),random.uniform(367+397, 372+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #모두 받기
    pag.click(random.uniform(280+640+640, 350+640+640),random.uniform(290+397, 295+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(1294, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def dailycheck():
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
    pag.click(random.uniform(525, 595),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85, 300)
    pag.drag(0, -250, 1.5)
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
    pag.click(11, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(525+640, 595+640),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85+640, 300)
    pag.drag(0, -250, 1.5)
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
    pag.click(11+640, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(350, 360), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85+640+640, 300)
    pag.drag(0, -250, 1.5)
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
    pag.click(1294, 297, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    pag.moveTo(316, 213+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540, 545),random.uniform(145+397, 155+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(525, 595),random.uniform(350+397, 360+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85, 300+397)
    pag.drag(0, -250, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525, 595),random.uniform(230+397, 240+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525, 595),random.uniform(360+397, 370+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610, 618),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
    pag.click(11, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    pag.moveTo(316+640, 225+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640, 545+640),random.uniform(145+397, 155+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(525+640, 595+640),random.uniform(350+397, 360+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85+640, 300+397)
    pag.drag(0, -250, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640, 595+640),random.uniform(230+397, 240+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640, 595+640),random.uniform(360+397, 370+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #출석 나가기
    pag.click(11+640, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    pag.moveTo(316+640+640, 225+397)
    pag.drag(200, 50, 1)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(540+640+640, 545+640+640),random.uniform(145+397, 155+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(350+397, 360+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #데일리 출석 체크 혜택 받기
    pag.moveTo(85+640+640, 300+397)
    pag.drag(0, -250, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #출석 스크롤 다운
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(230+397, 240+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌2
    pag.click(random.uniform(525+640+640, 595+640+640),random.uniform(360+397, 370+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 체크 시즌3
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #출석 나가기
    pag.click(1294, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def dailyqeust():
    #1번 케릭
    pag.click(random.uniform(580, 585),random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #퀘스트
    pag.click(random.uniform(230, 250),random.uniform(83, 90), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #미션
    pag.click(random.uniform(510, 530),random.uniform(365, 375), 3, random.uniform(0.5, 1))
    time.sleep(random.uniform(3.5, 4.5))
    #완료

# 땅 450, 500, 200, 230
# 이벤트 580, 610, 200, 230
# 1단계 425, 430, 129, 134
# 글루디오 던전 320, 370, 200, 230
def dailygate(x1, x2, y1, y2):
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
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129, 134), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250, 265), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(11, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(11+640, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(1294, 297, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580, 585), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1, x2), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(11, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(11+640, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(1294, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

def fieldgate(x1, x2, y1, y2):
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
    pag.click(11, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(11+640, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(1294, 297, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610, 618), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580, 585), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320, 340), random.uniform(80+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1, x2), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425, 430), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350, 370), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585, 590), random.uniform(240+397, 245+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(11, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640, 618+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640, 585+640), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640, 340+640), random.uniform(80+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640, x2+640), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640, 430+640), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640, 370+640), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640, 590+640), random.uniform(240+397, 245+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(11+640, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(610+640+640, 618+640+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #메뉴
    pag.click(random.uniform(580+640+640, 585+640+640), random.uniform(145+397, 150+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전
    pag.click(random.uniform(320+640+640, 340+640+640), random.uniform(80+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #일반
    pag.click(random.uniform(x1+640+640, x2+640+640), random.uniform(y1+397, y2+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #던전 선택
    pag.click(random.uniform(425+640+640, 430+640+640), random.uniform(129+397, 134+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #1단계
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(250+397, 265+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(585+640+640, 590+640+640), random.uniform(240+397, 245+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #자동 공격
    pag.click(1294, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드def buyticket():
    #1번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465, 470), random.uniform(53, 59), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305, 315), random.uniform(261, 264), 1, random.uniform(0.1, 0.3))
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
    pag.click(11, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(305+640, 315+640), random.uniform(261, 264), 1, random.uniform(0.1, 0.3))
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
    pag.click(11+640, 297, 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(305+640+640, 315+640+640), random.uniform(261, 264), 1, random.uniform(0.1, 0.3))
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
    pag.click(1294, 297, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드    
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #4번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465, 470), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305, 315), random.uniform(261+397, 264+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10, 20), random.uniform(342+397, 350+397), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305, 325), random.uniform(255+397, 260+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130, 160), random.uniform(83+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20, 40), random.uniform(155+397, 160+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175, 200), random.uniform(170+397, 205+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230, 245), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175, 200), random.uniform(307+397, 340+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230, 245), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350, 370), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610, 618),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(11, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300, 330), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #5번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640, 470+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640, 315+640), random.uniform(261+397, 264+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(10+640, 20+640), random.uniform(342+397, 350+397), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640, 325+640), random.uniform(255+397, 260+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640, 160+640), random.uniform(83+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640, 40+640), random.uniform(155+397, 160+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640, 200+640), random.uniform(170+397, 205+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640, 200+640), random.uniform(307+397, 340+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640, 245+640), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640, 370+640), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640, 618+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(11+640, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드
    pag.click(random.uniform(300+640, 330+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드

    #6번 케릭
    time.sleep(random.uniform(3.5, 4.5))
    pag.moveTo(316+640+640, 213+397)
    pag.drag(-100, 0, 1.5)
    time.sleep(random.uniform(3.5, 4.5))
    #자동 사냥 해제
    pag.click(random.uniform(465+640+640, 470+640+640), random.uniform(53+397, 59+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #상점
    pag.click(random.uniform(305+640+640, 315+640+640), random.uniform(261+397, 264+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #나중에 하기
    pag.click(random.uniform(30+640+640, 40+640+640), random.uniform(342+397, 350+397), 3, random.uniform(0.3, 0.9))
    time.sleep(random.uniform(3.5, 4.5))
    #오늘그만보기
    pag.click(random.uniform(305+640+640, 325+640+640), random.uniform(255+397, 260+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(130+640+640, 160+640+640), random.uniform(83+397, 90+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #교환소
    pag.click(random.uniform(20+640+640, 40+640+640), random.uniform(155+397, 160+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #소모품
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(170+397, 205+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #무기주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(175+640+640, 200+640+640), random.uniform(307+397, 340+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #갑옷주문서
    pag.click(random.uniform(230+640+640, 245+640+640), random.uniform(260+397, 268+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #+10
    pag.click(random.uniform(350+640+640, 370+640+640), random.uniform(315+397, 320+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #확인
    pag.click(random.uniform(610+640+640, 618+640+640),random.uniform(53+397, 59+397),1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #우편 나가기
    pag.click(1294, 297+397, 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #빠른 설정 모드    
    pag.click(random.uniform(300+640+640, 330+640+640), random.uniform(215+397, 235+397), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    #절전 모드
ig
def gotodesktop2():
    pag.click(402, 1052, 1, 0.2)
    time.sleep(4)
    pag.click(299, 61, 1, 0.2)

def gotodesktop1():
    pag.click(402, 1052, 1, 0.2)
    time.sleep(4)
    pag.click(83, 45, 1, 0.2)


# dailygate(580, 610, 200, 230)
dailygate(450, 500, 200, 230)
time.sleep(5)
dailycheck()
time.sleep(5)
rewardget()
gotodesktop1
time.sleep(60*123)
gotodesktop2()
time.sleep(30)
fieldgate(320, 370, 200, 230)
time.sleep(5)
rewardget()
time.sleep(5)
gotodesktop1

# buyticket()



# schedule.every().day.at("18:26:00").do(goto)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

