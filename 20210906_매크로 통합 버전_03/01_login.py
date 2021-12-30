import pyautogui as pag
import random
import time


my_id = ['bangyim88@gmail.com', 'bangssa88@gmail.com', 'kimjoshyyy88@gmail.com','christxmas@kakao.com', 'line.step11@gmail.com', 'line.step22@gmail.com', 'christxmas@gmail.com', 'jasonlee881007@gmail.com', 'Choisungwoo888@gmail.com', 'hbcqufdlvoa@gmail.com', 'christxmas1@kakao.com']
my_pw = ['!sungwoo88', '!sungwoo88', 'gksquf88','4865057a', 'gksquf88', 'gksquf88', '4865057a', 'tobeone19', '!sungwoo88', 'gksquf88', '4865057a']

def loginA():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[0], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[0], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[1], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[1], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############

def loginB():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[2], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[2], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[3], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[3], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############

def loginC():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[4], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[4], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[5], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[5], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############

def loginD():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[6], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[6], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[10], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[10], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############

def loginE():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[7], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[7], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[8], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[8], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############

def loginF():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[9], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[9], interval=random.uniform(0.05, 0.15))
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

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############


def loginG():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite(my_id[11], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[11], interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite(my_id[12], interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite(my_pw[12], interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############


def loginZ():
    time.sleep(1)
    pag.hotkey('win', 'd')
    time.sleep(0.5)
    # 바탕화면으로
    pag.click(1408,127)
    time.sleep(0.2)
    pag.click(1408,127)
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

    pag.typewrite("joshyyy88@gmail.com", interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite("gksquf88", interval=random.uniform(0.05, 0.15))
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

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼 

    pag.click(random.uniform(757, 1160), random.uniform(337, 373), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 카카오계정 선택

    pag.click(random.uniform(1078, 1294), random.uniform(317, 327), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.45, 0.55))
    # 아이디 입력 선택

    pag.typewrite("uri4958@daum.net", interval=random.uniform(0.05, 0.15))
    pag.press("tab", interval=random.uniform(0.1, 0.15))
    pag.typewrite("Ktjdnfl23!!", interval=random.uniform(0.05, 0.15))
    # 아이디/비번입력

    pag.click(random.uniform(1180, 1329), random.uniform(534, 565), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그인 버튼

    pag.click(random.uniform(1595, 1861), random.uniform(155, 200), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # GAME START

    time.sleep(random.uniform(19.45, 20.35))
    pag.click(random.uniform(1700, 1850), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
    # 창 한번 클릭

    time.sleep(random.uniform(1, 1.5))
    pag.click(random.uniform(1414, 1553), random.uniform(91, 121), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.8, 3.2))
    # 로그아웃 버튼

    pag.click(random.uniform(1883, 1908), random.uniform(6, 20), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.5, 1))
    # 창닫기
    ##############로그인#############


loginZ()
# loginB()
# #'2400g' 한별컴퓨터

# loginC()
# loginD()
# #'3400g' 한별사무실

# loginE()
# loginF()
# #'Odin_no.1' 새로산 컴퓨터

# loginG()
# #'미노네' 민호 컴퓨터