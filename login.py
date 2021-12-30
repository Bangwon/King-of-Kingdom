import pyautogui as pag
import random
import time

my_id1 = ['bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'christxmas1@kakao.com',
    'jasonlee881007@gmail.com', 
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw1 = ['!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    '4865057a',
    'tobeone19', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a', 
    '!sungwoo88']

my_id2 = ['bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'christxmas1@kakao.com',
    'jasonlee881007@gmail.com', 
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw2 = ['!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    '4865057a',
    'tobeone19', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a', 
    '!sungwoo88']


def login(my_id1, my_pw1, my_id2, my_pw2):
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

    pag.typewrite(my_id1, interval=random.uniform(0.05, 0.15))
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

login(my_id1[11], my_pw1[11])