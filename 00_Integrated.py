import pyautogui as pag
import random
import time
from PIL import ImageGrab
import schedule

my_id1 = ['bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'jasonlee881007@gmail.com', 
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'christxmas1@kakao.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw1 = ['!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    'tobeone19', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    '4865057a', 
    '!sungwoo88']

my_id2 = ['bangyim88@gmail.com', 
    'bangssa88@gmail.com', 
    'kimjoshyyy88@gmail.com',
    'christxmas@kakao.com',
    'line.step11@gmail.com', 
    'line.step22@gmail.com', 
    'christxmas@gmail.com',
    'jasonlee881007@gmail.com', 
    'Choisungwoo888@gmail.com', 
    'hbcqufdlvoa@gmail.com',
    'christxmas1@kakao.com',
    'xmas1104@nate.com',
    'bangsuk83@gmail.com']

my_pw2 = ['!sungwoo88', 
    '!sungwoo88', 
    'gksquf88',
    '4865057a',
    'gksquf88', 
    'gksquf88', 
    '4865057a',
    'tobeone19', 
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
    time.sleep(random.uniform(1.0, 1.5))
    # 접속 1 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 접속 1 (우)

    pag.click(random.uniform(150, 786), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 접속 2 (좌)
    pag.click(random.uniform(150+960, 786+960), random.uniform(289, 750), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 접속 2 (우)

    pag.click(random.uniform(777, 896), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 게임하기 (좌)
    pag.click(random.uniform(777+960, 896+960), random.uniform(974, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(20, 30))
    # 게임하기 (우)
    ##############로그인 후 접속#############

def left_BuyTicket():
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
    pag.click(random.uniform(224, 275), random.uniform(443, 496), 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(408, 470), random.uniform(448, 495), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛방어강화석(좌)        
    pag.click(random.uniform(549, 607), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420, 547), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (좌)
    pag.click(random.uniform(396, 476), random.uniform(220, 276), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛무기강화석(좌)
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
    pag.click(random.uniform(224+960, 275+960), random.uniform(443, 496), 1, random.uniform(0.1, 0.3))
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
    pag.click(random.uniform(408+960, 470+960), random.uniform(448, 495), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛방어강화석(우)        
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(396+960, 476+960), random.uniform(220, 276), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #빛무기강화석(우)
    pag.click(random.uniform(549+960, 607+960), random.uniform(660, 674), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    pag.click(random.uniform(420+960, 547+960), random.uniform(711, 731), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #최대 / 구매 (우)
    pag.click(random.uniform(919+960, 940+960), random.uniform(43, 63), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(4.5, 5.5))
    #상점나가기(우)
    time.sleep(random.uniform(4.5, 5.5))

def DailyQuest():
    pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 메뉴(좌)
    pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 메뉴(좌)

    pag.click(random.uniform(850, 866), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 마을의뢰(좌)
    pag.click(random.uniform(850+960, 866+960), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 마을의뢰(우)
    
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우)
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우)
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우)
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우)
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우) 
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(좌)
    pag.click(random.uniform(823+960, 906+960), random.uniform(998, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 수락하기(우)

    pag.click(random.uniform(924, 937), random.uniform(43, 65), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 닫기(좌)
    pag.click(random.uniform(924+960, 937+960), random.uniform(43, 65), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 닫기(우)

    pag.click(random.uniform(711, 858), random.uniform(222, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 퀘스트시작(좌) - 발할라 안깬 케릭 고려해서 2번째 퀘스트 클릭
    pag.click(random.uniform(711+960, 858+960), random.uniform(222, 235), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 퀘스트시작(우) - 발할라 안깬 케릭 고려해서 2번째 퀘스트 클릭

    time.sleep(random.uniform(35*60, 36*60))
    # 30분 명상타임

    pag.click(random.uniform(761, 878), random.uniform(113, 146), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(761+960, 878+960), random.uniform(113, 146), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)
    pag.click(random.uniform(721, 810), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(좌)
    pag.click(random.uniform(721+960, 810+960), random.uniform(217, 247), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 퀘스트 보상 받기(우)
    pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(좌)
    pag.click(random.uniform(586+960, 618+960), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    # 보상 선택(우)
    pag.click(random.uniform(331, 638), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(좌)
    pag.click(random.uniform(331+960, 638+960), random.uniform(179, 313), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.0, 1.5))
    # 허공 터치(우)

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
    time.sleep(random.uniform(4.5, 5.5))
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
    time.sleep(random.uniform(4.5, 5.5))
def left_buy_potion():
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
    # time.sleep(random.uniform(1.11, 2.22))
    # pag.click(random.uniform(21, 280), random.uniform(609, 655), 1, random.uniform(0.3, 0.6))
    # # 순간 이동 주문서 21, 609 / 280, 655
    # time.sleep(random.uniform(2, 3.4))
    # pag.click(random.uniform(550, 610), random.uniform(590, 595), 1, random.uniform(0.3, 0.6))
    # # 최대 버튼
    # time.sleep(random.uniform(2, 3.4))
    # pag.click(random.uniform(500, 600), random.uniform(685, 700), 1, random.uniform(0.3, 0.6))
    # # 물약 구매
    time.sleep(random.uniform(2, 3.4))
    pag.click(random.uniform(914, 939), random.uniform(45, 63), 1, random.uniform(0.3, 0.6))
    # 장비창 나가기
    time.sleep(random.uniform(4.5, 5.5))
def right_buy_potion():
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
    pag.click(random.uniform(21+960, 280+960), random.uniform(609, 655), 1, random.uniform(0.3, 0.6))
    # 순간 이동 주문서 21, 609 / 280, 655
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
def left_prisongate():
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
    pag.click(random.uniform(650, 905), random.uniform(380, 690), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(23, 285), random.uniform(99, 130), 1, random.uniform(0.3, 0.6))
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
def right_prisongate():
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
    pag.click(random.uniform(650+960, 905+960), random.uniform(380, 690), 1, random.uniform(0.3, 0.6))
    # 지하 감옥
    time.sleep(random.uniform(2.5, 3.5))
    pag.click(random.uniform(23+960, 285+960), random.uniform(99, 130), 1, random.uniform(0.3, 0.6))
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
def left_gateend():
    checkpoint=(25,50)
    skill=(625, 765)
    color1=(0,0,0)
    color2=(255,255,255)
    while True:
            screen = ImageGrab.grab()
            rgb1 = screen.getpixel(checkpoint)
            rgb2 = screen.getpixel(skill)
            if rgb1 == color1:
                time.sleep(random.uniform(40.11, 41.15))
                break
            
            elif rgb2 == color2:
                pag.click(625, 765, 3, 1)

            else :
                time.sleep(1)
                print(rgb1)
                print(time.ctime())
def right_gateend():
    checkpoint=(25,50)
    color=(0,0,0)
    while True:
            screen = ImageGrab.grab()
            rgb = screen.getpixel(checkpoint)
            if rgb == color:
                time.sleep(35)
                break
            else :
                time.sleep(1)
                print(rgb)
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
def itemunequip():
    time.sleep(random.uniform(1, 2))
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
def itemequip():
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
    time.sleep(random.uniform(4.5, 5.5))
def ctselect(x1, x2, y1, y2):
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2))
    # 케릭터 선택
    time.sleep(random.uniform(4.5, 5.11))
    pag.click(random.uniform(745, 920), random.uniform(975, 1005))
    # 게임시작하기
    time.sleep(random.uniform(4.5, 5.5))
# 첫 번째 (760, 915, 100, 130)
# 두 번째 (760, 915, 180, 215)
# 세 번째 (760, 915, 270, 290)
# 네 번째 (760, 915, 355, 375)
# 다섯 번째 (760, 915, 440, 460)

# 여름의 섬 x1, x2, y1, y2 (37, 303, 373, 690)
# 공허의 유적 (349, 625, 377, 687)
# 난쟁이 비밀 통로 (661, 917, 375, 684)
# 1단계 x3, x4, y3, y4 (23, 285, 99, 130)
# 2단계 (23, 282, 155, 185)
# 3단계 (23, 285, 215, 245)

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

    pag.click(random.uniform(533, 565), random.uniform(142, 178), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템클릭(좌)    

    pag.click(random.uniform(654, 704), random.uniform(626, 636), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #몬스터처치(좌)    

    pag.click(random.uniform(455, 583), random.uniform(409, 432), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    #해안가기지(좌) 

    pag.click(random.uniform(847, 872), random.uniform(994, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #빠른이동(좌) 

    pag.click(random.uniform(486, 606), random.uniform(606, 615), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #이동(좌) 

    pag.click(random.uniform(890, 909), random.uniform(877, 899), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #오토사냥(좌) 
    ###########해안기지이동#############

def right_MoveToOcean():
    pag.click(random.uniform(909+960, 929+960), random.uniform(42, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #메뉴바(우)
        
    pag.click(random.uniform(909+960, 931+960), random.uniform(147, 172), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템수집(우)

    pag.click(random.uniform(610+960, 656+960), random.uniform(98, 111), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #즐겨찾기(우)

    pag.click(random.uniform(533+960, 565+960), random.uniform(142, 178), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #아이템클릭(우)

    pag.click(random.uniform(654+960, 704+960), random.uniform(626, 636), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #몬스터처치(우)    

    pag.click(random.uniform(455+960, 583+960), random.uniform(409, 432), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(2.0, 2.5))
    #해안가기지(우)

    pag.click(random.uniform(847+960, 872+960), random.uniform(994, 1009), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #빠른이동(우)

    pag.click(random.uniform(486+960, 606+960), random.uniform(606, 615), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(8.851, 12.442))
    #이동(우)

    pag.click(random.uniform(890+960, 909+960), random.uniform(877, 899), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1.5, 2.0))
    #오토사냥(우) 
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


def oneclickgate():
    # left_returntotown()
    # itemunequip()
    # ctchange()
    # ctselect(760, 915, 100, 130)
    # itemequip()
    # left_guilddonate()
    # left_buy_potion()
    # left_dailygate(349, 625, 377, 687, 23, 285, 99, 130)
    # left_gateend()
    # left_buy_potion()
    # left_dailygate(661, 917, 375, 684, 23, 285, 99, 130)
    left_gateend()       
    itemunequip()
    # # 첫 번째

    ctchange()
    ctselect(760, 915, 180, 215)
    itemequip()
    left_guilddonate()
    left_buy_potion()
    left_dailygate(349, 625, 377, 687, 23, 285, 99, 130)
    left_gateend()
    left_buy_potion()
    left_dailygate(661, 917, 375, 684, 23, 285, 99, 130)
    left_gateend()
    itemunequip()
    # 두 번째

    ctchange()
    ctselect(760, 915, 270, 290)
    itemequip()
    left_guilddonate()
    left_buy_potion()
    left_dailygate(349, 625, 377, 687, 23, 285, 99, 130)
    left_gateend()
    left_buy_potion()
    left_dailygate(661, 917, 375, 684, 23, 285, 99, 130)
    left_gateend()
    # 세 번째

    ctchange()
    ctselect(760, 915, 100, 130)

    left_MoveToOcean()


oneclickgate()      
