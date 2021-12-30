import pyautogui as pag
import random
import time
from PIL import ImageGrab
import schedule
pag.FAILSAFE=False
my_id1 = ['bangwon2@naver.com', 
    'jasonlee881007@gmail.com',
    'bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'christxmas1@kakao.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw1 = ['!tobeone22',
    'tobeone19', 
    '!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    '4865057a', 
    '!sungwoo88']

my_id2 = ['bangwon2@naver.com', 
    'jasonlee881007@gmail.com',
    'bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'christxmas1@kakao.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw2 = ['!tobeone22',
    'tobeone19', 
    '!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    '4865057a', 
    '!sungwoo88']


def login(my_id1, my_pw1, my_id2, my_pw2):
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1840,15)
    time.sleep(0.2)
    pag.click(1840,15)
    # 브라우저 더블클릭
    time.sleep(random.uniform(9.8, 10.2))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id1, interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw1, interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595,1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1450, 1500), random.uniform(5, 10), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼 

    time.sleep(random.uniform(9.8, 10.2))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id2, interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw2, interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595,1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1450, 1500), random.uniform(5, 10), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼 
    pag.click(random.uniform(1790, 1815), random.uniform(5, 15), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 크롬 로그인창 내리기
    
def loginA():
    
    pag.click(random.uniform(557, 1244), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 선택

    pag.keyDown('win', random.uniform(0.3, 0.5))
    pag.keyDown('left', random.uniform(0.1, 0.3))
    pag.keyUp('left', random.uniform(0.1, 0.3))
    pag.keyUp('win', random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 왼쪽 보내기

    pag.click(random.uniform(101, 776), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창1 재선택

    pag.click(random.uniform(961, 1292), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 선택

    pag.keyDown('win', random.uniform(0.3, 0.5))
    pag.keyDown('right', random.uniform(0.1, 0.3))
    pag.keyUp('right', random.uniform(0.1, 0.3))
    pag.keyUp('win', random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 오른쪽 보내기

    pag.click(random.uniform(1072, 1700), random.uniform(1, 11), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 창2 재선택

    pag.click(random.uniform(150, 786), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.0, 3.5))
    # 접속 1 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.0, 3.5))
    # 접속 1 (우)

    pag.click(random.uniform(150, 786), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.0, 3.5))
    # 접속 2 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.0, 3.5))
    # 접속 2 (우)

    pag.click(random.uniform(777, 896), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.0, 3.5))
    # 게임하기 (좌)
    pag.click(random.uniform(777+960, 896+960), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20, 30))
    # 게임하기 (우)
    ##############로그인 후 접속#############


def left_buyavater():
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(791, 811), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점(좌)
    pag.click(random.uniform(171, 280), random.uniform(90, 116), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #소환
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(210, 370), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환1
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(400, 560), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환2
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(590, 750), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환3
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(210, 370), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환1
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(400, 560), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환2
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(590, 750), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환3
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(780, 940), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #룬 소환 1
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(780, 940), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #룬 소환 2
    pag.click(random.uniform(400, 555), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(420, 540), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.click(random.uniform(919, 940), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점나가기(좌)
    time.sleep(random.uniform(4.5, 5.5))
def right_buyavater():
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(791+960, 811+960), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점(좌)
    pag.click(random.uniform(171+960, 280+960), random.uniform(90, 116), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #소환
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(210+960, 370+960), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환1
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(400+960, 560+960), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환2
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(590+960, 750+960), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #아바타 소환3
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(210+960, 370+960), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환1
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(400+960, 560+960), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환2
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(590+960, 750+960), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #탈 것 소환3
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(780+960, 940+960), random.uniform(140, 255), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #룬 소환 1
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.moveTo(840+960, 145)
    pag.drag(-700, 0, 2)
    time.sleep(random.uniform(4.5, 5.5))
    #드래그
    pag.click(random.uniform(780+960, 940+960), random.uniform(360, 475), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #룬 소환 2
    pag.click(random.uniform(420+960, 540+960), random.uniform(660, 680), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #구매
    pag.click(random.uniform(400+960, 500+960), random.uniform(975, 990), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #허공
    pag.click(random.uniform(919+960, 940+960), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점나가기(좌)
    time.sleep(random.uniform(4.5, 5.5))

def left_buyticket():
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(791, 811), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점(좌)
    pag.click(random.uniform(343, 391), random.uniform(99, 110), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #일반상품(좌)
    pag.click(random.uniform(44, 109), random.uniform(231, 241), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #강화/세공(좌)
    pag.click(random.uniform(224, 275), random.uniform(443, 490), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #방어강화석(좌)        
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(214, 279), random.uniform(210, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #무기강화석(좌)        
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(408, 470), random.uniform(448, 490), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛방어강화석(좌)        
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(396, 476), random.uniform(220, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛무기강화석(좌)
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(550, 700), random.uniform(220, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    # 황금 각인 도장 550, 140 / 760, 335
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(550, 700), random.uniform(365, 465), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    # 황금 유물 동전 
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(919, 940), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점나가기(좌)
    time.sleep(random.uniform(4.5, 5.5))
def right_buyticket():
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(791+960, 811+960), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점(우)
    pag.click(random.uniform(343+960, 391+960), random.uniform(99, 110), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #일반상품(우)
    pag.click(random.uniform(44+960, 109+960), random.uniform(231, 241), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #강화/세공(우)
    pag.click(random.uniform(224+960, 275+960), random.uniform(443, 490), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #방어강화석(우)
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(214+960, 279+960), random.uniform(210, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #무기강화석(우)        
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(408+960, 470+960), random.uniform(448, 490), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛방어강화석(우)        
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(396+960, 476+960), random.uniform(220, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛무기강화석(우)
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(550+960, 700+960), random.uniform(220, 267), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    # 황금 각인 도장 550, 140 / 760, 335
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)    
    pag.click(random.uniform(550+960, 700+960), random.uniform(365, 465), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    # 황금 유물 동전 
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(919+960, 940+960), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점나가기(우)
    time.sleep(random.uniform(4.5, 5.5))

def left_dailyquest(x1, x2, y1, y2):
    time.sleep(random.uniform(3.5, 4.5))
    pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(3.5, 4.5))
    # 메뉴(좌)
    pag.click(random.uniform(850, 866), random.uniform(221, 243), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(3.5, 4.5))
    # 마을의뢰(좌)
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(3.5, 4.5))
    # 마을선택 
    # 미드가르드 20, 150, 100, 120
    # 요툰하임 180, 305, 100, 120
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 6, random.uniform(1, 2))
    time.sleep(random.uniform(3.5, 4.5))
    # 수락하기(좌)
    pag.click(random.uniform(25, 300), random.uniform(550, 580), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(3.5, 4.5))
    # 8번째 의뢰 선택
    pag.click(random.uniform(665, 785), random.uniform(1000, 1015), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(3.5, 4.5))
    # 빠른 이동 
    pag.click(random.uniform(470, 630), random.uniform(605, 620), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(20.5, 21.5))
    # 무료이동 클릭
    while True:
        pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.3, 0.6))
        time.sleep(random.uniform(3.5, 4.5))
        # 메뉴(좌)
        pag.click(random.uniform(850, 866), random.uniform(221, 243), 1, random.uniform(0.3, 0.6))
        time.sleep(random.uniform(3.5, 4.5))
        # 마을의뢰(좌)
        pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.3, 0.6))
        time.sleep(random.uniform(3.5, 4.5))
        # 미드가르드
        cp = (34, 457)
        color = (214, 161, 255)
        rgb = ImageGrab.grab().getpixel(cp)
        if rgb == color:
            time.sleep(5)
            print(time.ctime)
            break
        else :
            time.sleep(random.uniform(3.5, 4.5))
            pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.3, 0.6))
            time.sleep(random.uniform(3*60, 4.*60))
            # 나가기
            print(rgb)
            print(time.ctime())
    # 다섯 번째 퀘스트 완료 36, 398 / 여섯 34, 457 / 214, 161, 255
    i = 1
    while i <= 6:
        pag.click(random.uniform(25, 300), random.uniform(145, 175), 2, random.uniform(1, 2))
        time.sleep(random.uniform(3.5, 4.5))
        # 첫번째 퀘스트 클릭
        pag.click(random.uniform(823, 906), random.uniform(998, 1015), 2, random.uniform(1, 2))
        time.sleep(random.uniform(3.5, 4.5))
        # 보상받기(좌)
        pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.3, 0.6))
        time.sleep(random.uniform(3.5, 4.5))
        # 보상 선택(좌)
        pag.click(random.uniform(331, 638), random.uniform(179, 313), 2, random.uniform(0.3, 0.6))
        time.sleep(random.uniform(3.5, 4.5))
        # 허공 터치(좌)
        i += 1
    pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 나가기
    pag.click(random.uniform(80, 165), random.uniform(170, 240), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 지도 클릭
    pag.click(random.uniform(60, 95), random.uniform(940, 970), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 월드 보기
    pag.click(random.uniform(700, 740), random.uniform(565, 595), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 마을 클릭
    pag.click(random.uniform(345, 465), random.uniform(985, 1000), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 마을 이동 클릭
    pag.click(random.uniform(490, 610), random.uniform(610, 620), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(24.5, 25.55))
    # 확인
def right_dailyquest(x1, x2, y1, y2):
    time.sleep(random.uniform(3.5, 4.5))
    pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 메뉴(좌)
    pag.click(random.uniform(850+960, 866+960), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 마을의뢰(좌)
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 미드가르드
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 6, random.uniform(1, 2))
    time.sleep(random.uniform(3.5, 4.5))
    # 수락하기(좌)
    pag.click(random.uniform(25+960, 300+960), random.uniform(550, 580), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 8번째 의뢰 선택
    pag.click(random.uniform(665+960, 785+960), random.uniform(1000, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 빠른 이동 
    pag.click(random.uniform(470+960, 630+960), random.uniform(605, 620), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20.5, 21.5))
    # 무료이동 클릭
    while True:
        pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 메뉴(좌)
        pag.click(random.uniform(850+960, 866+960), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 마을의뢰(좌)
        pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 미드가르드
        cp = (34+960, 457)
        color = (214, 161, 255)
        rgb = ImageGrab.grab().getpixel(cp)
        if rgb == color:
            time.sleep(5)
            print(time.ctime)
            break
        else :
            time.sleep(1)
            pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
            time.sleep(random.uniform(3*60, 4*60))
            # 나가기
            print(rgb)
            print(time.ctime())
    # 다섯 번째 퀘스트 완료 36, 398 / 여섯 34, 457 / 214, 161, 255
    i = 1
    while i <= 6:
        pag.click(random.uniform(25+960, 300+960), random.uniform(145, 175), 2, random.uniform(1, 2))
        time.sleep(random.uniform(3.5, 4.5))
        # 첫번째 퀘스트 클릭
        pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 2, random.uniform(1, 2))
        time.sleep(random.uniform(3.5, 4.5))
        # 보상받기(좌)
        pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 보상 선택(좌)
        pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 2, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 허공 터치(좌)
        i += 1
    pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.55))
    # 나가기
    pag.click(random.uniform(80+960, 165+960), random.uniform(170, 240), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 지도 클릭
    pag.click(random.uniform(60+960, 95+960), random.uniform(940, 970), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 월드 보기
    pag.click(random.uniform(700+960, 740+960), random.uniform(565, 595), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 마을 클릭
    pag.click(random.uniform(345+960, 465+960), random.uniform(985, 1000), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(4.5, 5.55))
    # 마을 이동 클릭
    pag.click(random.uniform(490+960, 610+960), random.uniform(610, 620), 1, random.uniform(0.3, 0.6))
    time.sleep(random.uniform(24.5, 25.55))
    # 확인

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
    pag.click(random.uniform(90, 280), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
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
    pag.click(random.uniform(90+960, 280+960), random.uniform(150,190), 1, random.uniform(0.3, 0.6))
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
    pag.moveTo(890+960, 380)
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

def right_prison_gateend(x1, x2, y1, y2, x3, x4, y3, y4):
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
            time.sleep(random.uniform(12.5, 13.5))
            pag.click(random.uniform(917+960, 930+960), random.uniform(170, 185), 1, random.uniform(0.3, 0.6))
            # 파티 917, 170 / 930, 185
            time.sleep(random.uniform(2.5, 3.5))
            pag.click(random.uniform(880+960, 900+960), random.uniform(260, 270), 1, random.uniform(0.3, 0.6))
            # 파티장에게 이동 800, 260 / 900, 270  
            # 3명 파티 800, 260 / 900, 270
            
        else :
            time.sleep(1)
            print(time.ctime())


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
    time.sleep(random.uniform(4.5, 5.5))
def right_returntotown():
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(19+960, 33+960), random.uniform(255, 267), 1, random.uniform(0.1, 0.3))
    # 귀환 19, 255 / 33, 267
    time.sleep(random.uniform(3.5, 4.7))
    pag.click(random.uniform(490+960, 600+960), random.uniform(600, 615), 1, random.uniform(0.1, 0.3))
    # 귀환 확인 490, 600 / 600, 615
    time.sleep(random.uniform(4.5, 5.5))

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
    time.sleep(random.uniform(2, 2.19))
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
    pag.click(random.uniform(530+960, 560+960), random.uniform(330, 360), 2, random.uniform(0.1, 0.3))
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
    time.sleep(random.uniform(2, 2.19))
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
    time.sleep(random.uniform(5, 6))
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
    time.sleep(random.uniform(5, 6))
    pag.click(random.uniform(660+960, 690+960), random.uniform(965, 990), 1, random.uniform(0.3, 0.6))
    # 창고가기
    time.sleep(random.uniform(10, 11))
    pag.click(random.uniform(30+960, 70+960), random.uniform(220, 260), 1, random.uniform(0.3, 0.6))
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

def left_ctchange():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907, 931), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(726, 753), random.uniform(504, 532), 1, random.uniform(0.3, 0.6))
    # 케릭터 변경
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(488, 605), random.uniform(596, 617), 1, random.uniform(0.3, 0.6))
    # 캐릭터 선택 화면 이동 확인
    time.sleep(random.uniform(4.5, 5.5))
def left_ctselect(x1, x2, y1, y2):
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2))
    # 케릭터 선택
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(745, 920), random.uniform(975, 1005))
    # 게임시작하기
    time.sleep(random.uniform(24.5, 25.5))

def right_ctchange():
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(907+960, 931+960), random.uniform(46, 61), 1, random.uniform(0.3, 0.6))
    # 메뉴
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(726+960, 753+960), random.uniform(504, 532), 1, random.uniform(0.3, 0.6))
    # 케릭터 변경
    time.sleep(random.uniform(3.55, 4.12))
    pag.click(random.uniform(488+960, 605+960), random.uniform(596, 617), 1, random.uniform(0.3, 0.6))
    # 캐릭터 선택 화면 이동 확인
    time.sleep(random.uniform(4.5, 5.5))
def right_ctselect(x1, x2, y1, y2):
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(x1+960, x2+960), random.uniform(y1, y2))
    # 케릭터 선택
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(745+960, 920+960), random.uniform(975, 1005))
    # 게임시작하기
    time.sleep(random.uniform(24.5, 25.5))


# 첫 번째 (760, 915, 100, 130)
# 두 번째 (760, 915, 180, 215)
# 세 번째 (760, 915, 270, 290)
# 네 번째 (760, 915, 355, 375)
# 다섯 번째 (760, 915, 440, 460)

# 그림자 성채 37, 303, 430, 530
# 공허의 유적 350, 625, 430, 530
# 난쟁이 비밀 통로 670, 917, 430, 530
# - 330, 600, 430, 530
# 지하 감옥 650, 905, 430, 530
# 1단계 x3, x4, y3, y4 (23, 285, 99, 130)
# 2단계 (23, 282, 155, 185)
# 3단계 (23, 285, 215, 245)
# 4단계 23, 285, 275, 305
# 6단계 23, 285, 385, 420

# 미드 순간 이동 주문서 30, 280, 535, 575
# 요툰 순간 이동 주문서 21, 280, 609, 655
# 니다 순간 이동 주문서 90, 280, 690, 740
# 미드가르드 일일퀘 20, 150, 100, 120
# 요툰하임 일일퀘 180, 300, 100, 120

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

def left_MoveToOcean():
    pag.click(random.uniform(909, 929), random.uniform(42, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #메뉴바(좌)
        
    pag.click(random.uniform(909, 931), random.uniform(147, 172), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템수집(좌)

    pag.click(random.uniform(610, 656), random.uniform(98, 111), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #즐겨찾기(좌)

    pag.click(random.uniform(533, 572), random.uniform(144, 177), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템클릭(좌)    

    pag.click(random.uniform(654, 704), random.uniform(626, 636), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #몬스터처치(좌)    

    pag.click(random.uniform(405, 763), random.uniform(406, 443), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    #해안가기지(좌) 

    pag.click(random.uniform(847, 872), random.uniform(994, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #빠른이동(좌) 

    pag.click(random.uniform(486, 606), random.uniform(606, 615), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(19.5, 20.5))
    #이동(좌) 

    pag.click(random.uniform(890, 909), random.uniform(877, 899), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #오토사냥(좌) 
    ###########해안기지이동#############

def right_MoveToOcean():
    pag.click(random.uniform(909+960, 929+960), random.uniform(42, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #메뉴바(좌)
        
    pag.click(random.uniform(909+960, 931+960), random.uniform(147, 172), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템수집(좌)

    pag.click(random.uniform(610+960, 656+960), random.uniform(98, 111), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #즐겨찾기(좌)

    pag.click(random.uniform(420+960, 454+960), random.uniform(145, 177), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템클릭(좌)    

    pag.click(random.uniform(654+960, 704+960), random.uniform(626, 636), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #몬스터처치(좌)    

    pag.click(random.uniform(405+960, 763+960), random.uniform(406, 443), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    #해안가기지(좌) 

    pag.click(random.uniform(847+960, 872+960), random.uniform(994, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #빠른이동(좌) 

    pag.click(random.uniform(486+960, 606+960), random.uniform(606, 615), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(19.5, 20.5))
    #이동(좌) 

    pag.click(random.uniform(890+960, 909+960), random.uniform(877, 899), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #오토사냥(좌) 
    ###########해안기지이동#############

def left_Out():
    pag.click(random.uniform(19, 35), random.uniform(363, 378), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #절전모드(좌)

    pag.click(random.uniform(831, 927), random.uniform(997, 1020), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #방치모드(좌)

    pag.click(random.uniform(506, 585), random.uniform(721, 733), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #확인(좌)

def right_Out():
    pag.click(random.uniform(19+960, 35+960), random.uniform(363, 378), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #절전모드(우)

    pag.click(random.uniform(831+960, 927+960), random.uniform(997, 1020), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #방치모드(우)

    pag.click(random.uniform(506+960, 585+960), random.uniform(721, 733), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #확인(우)


def left_jasonlee():
    left_returntotown()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 100, 130)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 690, 740)
    left_dailygate(37, 303, 430, 530, 23, 282, 155, 185)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 690, 740)
    left_dailygate(670, 917, 430, 530, 23, 285, 215, 245)
    gateend(670, 917, 430, 530, 23, 285, 215, 245)
    # 공허의 유적
    left_buy_potion(90, 280, 690, 740)
    left_prisongate(330, 600, 375, 530, 23, 285, 215, 245)
    prison_gateend(330, 600, 375, 530, 23, 285, 215, 245)
    # 난쟁이 유적
    left_guilddonate()
    left_buyavater()
    left_buyticket()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 180, 215)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적
    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 270, 290)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 355, 375)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 440, 460)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적
    left_guilddonate()
    left_itemunequip()

def left_jasonlee1():
    # left_returntotown()
    # left_itemunequip()

    # left_ctchange()
    # left_ctselect(760, 915, 100, 130)
    # left_returntotown()
    # left_itemequip()
    # left_buy_potion(90, 280, 690, 740)
    # left_dailygate(37, 303, 430, 530, 23, 282, 155, 185)
    # gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # # 달빛 정원
    # left_buy_potion(90, 280, 690, 740)
    # left_dailygate(670, 917, 430, 530, 23, 285, 215, 245)
    # gateend(670, 917, 430, 530, 23, 285, 215, 245)
    # # 공허의 유적
    # left_buy_potion(90, 280, 690, 740)
    # left_prisongate(330, 600, 375, 530, 23, 285, 215, 245)
    # prison_gateend(330, 600, 375, 530, 23, 285, 215, 245)
    # # 난쟁이 유적
    # left_guilddonate()
    # left_buyavater()
    # left_buyticket()
    # left_itemunequip()

    # left_ctchange()
    # left_ctselect(760, 915, 180, 215)
    # left_returntotown()
    # left_itemequip()
    # left_buy_potion(90, 280, 609, 655)
    # left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적
    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 270, 290)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 355, 375)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_guilddonate()
    left_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 440, 460)
    left_returntotown()
    left_itemequip()
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적
    left_guilddonate()
    left_itemunequip()


def oneclick_bangwon_jasonlee():
    # login(my_id1[1], my_pw1[1], my_id2[0], my_pw2[0])
    # loginA()

    left_returntotown()
    left_itemunequip()

    right_returntotown()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 100, 130)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 100, 130)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 690, 740)
    left_dailygate(37, 303, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    left_buyavater()
    left_buyticket()
    left_guilddonate()
    right_buyavater()
    right_buyticket()
    right_guilddonate()
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 690, 740)
    left_dailygate(670, 917, 430, 530, 23, 285, 215, 245)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 285, 215, 245)
    # 공허의 유적
    left_buy_potion(90, 280, 690, 740)
    left_prisongate(330, 600, 375, 530, 23, 285, 215, 245)
    right_buy_potion(90, 280, 609, 655)
    right_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 285, 215, 245)
    # 난쟁이 유적

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 180, 215)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 180, 215)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    left_guilddonate()
    right_guilddonate()
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 270, 290)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 270, 290)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    left_guilddonate()
    right_guilddonate()
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 355, 375)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 355, 375)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    left_guilddonate()
    right_guilddonate()
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 440, 460)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 440, 460)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(37, 303, 430, 530, 23, 285, 99, 130)
    left_guilddonate()
    right_guilddonate()
    gateend(37, 303, 430, 530, 23, 285, 99, 130)
    # 달빛 정원
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 공허의 유적
    left_buy_potion(90, 280, 609, 655)
    left_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_prisongate(330, 600, 375, 530, 23, 282, 155, 185)
    prison_gateend(330, 600, 375, 530, 23, 282, 155, 185)
    # 난쟁이 유적

def oneclick_bangwon_jasonlee1():
    # login(my_id1[1], my_pw1[1], my_id2[0], my_pw2[0])
    # loginA()

    # left_returntotown()
    # left_itemunequip()

    # right_returntotown()
    # right_itemunequip()

    # left_ctchange()
    # left_ctselect(760, 915, 100, 130)
    # left_returntotown()
    # left_itemequip()

    # right_ctchange()
    # right_ctselect(760, 915, 100, 130)
    # right_returntotown()
    # right_itemequip()

    # left_buy_potion(90, 280, 690, 740)
    # left_dailygate(350, 625, 430, 530, 23, 285, 215, 245)
    # right_buy_potion(90, 280, 609, 655)
    # right_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    left_buyavater()
    left_buyticket()
    left_guilddonate()
    right_buyavater()
    right_buyticket()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 285, 215, 245)
    # 공허
    left_buy_potion(90, 280, 690, 740)
    left_dailygate(670, 917, 430, 530, 23, 285, 215, 245)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 285, 215, 245)
    # 난쟁이

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 180, 215)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 180, 215)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    left_guilddonate()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 282, 155, 185)
    # 공허
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 난쟁이

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 270, 290)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 270, 290)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    left_guilddonate()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 282, 155, 185)
    # 공허
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 난쟁이

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 355, 375)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 355, 375)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    left_guilddonate()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 282, 155, 185)
    # 공허
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 난쟁이

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 440, 460)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 440, 460)
    right_returntotown()
    right_itemequip()

    left_buy_potion(90, 280, 609, 655)
    left_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(350, 625, 430, 530, 23, 282, 155, 185)
    left_guilddonate()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 282, 155, 185)
    # 공허
    left_buy_potion(90, 280, 609, 655)
    left_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 282, 155, 185)
    # 난쟁이

    left_itemunequip()
    right_itemunequip()

    left_ctchange()
    left_ctselect(760, 915, 100, 130)
    left_returntotown()
    left_itemequip()

    right_ctchange()
    right_ctselect(760, 915, 100, 130)
    right_returntotown()
    right_itemequip()

    left_MoveToOcean()
    right_MoveToOcean()


def oneclick_bangwon_jasonlee2():
    # login(my_id1[1], my_pw1[1], my_id2[0], my_pw2[0])
    # loginA()

    # left_returntotown()
    # left_itemunequip()

    # right_returntotown()
    # right_itemunequip()

    # left_ctchange()
    # left_ctselect(760, 915, 100, 130)
    # left_returntotown()
    # left_itemequip()

    # right_ctchange()
    # right_ctselect(760, 915, 100, 130)
    # right_returntotown()
    # right_itemequip()

    left_buy_potion(90, 280, 690, 740)
    left_dailygate(350, 625, 430, 530, 23, 285, 215, 245)
    right_buy_potion(90, 280, 609, 655)
    right_dailygate(350, 625, 430, 530, 23, 285, 215, 245)
    left_buyavater()
    left_buyticket()
    left_guilddonate()
    right_buyavater()
    right_buyticket()
    right_guilddonate()
    gateend(350, 625, 430, 530, 23, 285, 215, 245)
    # 공허
    left_buy_potion(90, 280, 690, 740)
    left_dailygate(670, 917, 430, 530, 23, 285, 215, 245)
    right_buy_potion(90, 280, 690, 740)
    right_dailygate(670, 917, 430, 530, 23, 282, 155, 185)
    gateend(670, 917, 430, 530, 23, 285, 215, 245)
    # 난쟁이

    left_MoveToOcean()
    right_MoveToOcean()



# left_prison_gateend(650, 905, 430, 530, 23, 285, 215, 245)

# oneclick_bangwon_jasonlee2()

oneclick_bangwon_jasonlee1()

# schedule.every().day.at("04:05:00").do(oneclick_bangwon_jasonlee2)

while True:
    schedule.run_pending()
    time.sleep(1)
