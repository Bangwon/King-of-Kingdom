import pyautogui as pag
import time
import random
from PIL import ImageGrab

def left_dailyquest(x1, x2, y1, y2):
    time.sleep(random.uniform(3.5, 4.5))
    pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 메뉴(좌)
    pag.click(random.uniform(850, 866), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 마을의뢰(좌)
    pag.click(random.uniform(x1, x2), random.uniform(y1, y2), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 미드가르드 20, 150, 100, 120
    # 요툰하임 180, 300, 100, 120
    pag.click(random.uniform(823, 906), random.uniform(998, 1015), 6, random.uniform(1, 2))
    time.sleep(random.uniform(3.5, 4.5))
    # 수락하기(좌)
    pag.click(random.uniform(25, 300), random.uniform(550, 580), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 8번째 의뢰 선택
    pag.click(random.uniform(665, 785), random.uniform(1000, 1015), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 빠른 이동 
    pag.click(random.uniform(470, 630), random.uniform(605, 620), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(10.5, 14.5))
    # 무료이동 클릭
    while True:
        pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 메뉴(좌)
        pag.click(random.uniform(850, 866), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 마을의뢰(좌)
        pag.click(random.uniform(20, 150), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
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
            time.sleep(1)
            pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
            time.sleep(random.uniform(20.5, 24.5))
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
        pag.click(random.uniform(586, 618), random.uniform(605, 638), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 보상 선택(좌)
        pag.click(random.uniform(331, 638), random.uniform(179, 313), 2, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 허공 터치(좌)
        i += 1
    pag.click(random.uniform(907, 929), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.55))
    # 나가기
def right_dailyquest():
    time.sleep(random.uniform(3.5, 4.5))
    pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 메뉴(좌)
    pag.click(random.uniform(850+960, 866+960), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(3.5, 4.5))
    # 마을의뢰(좌)
    pag.click(random.uniform(20+960, 150+960), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
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
    time.sleep(random.uniform(10.5, 14.5))
    # 무료이동 클릭
    while True:
        pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 메뉴(좌)
        pag.click(random.uniform(850+960, 866+960), random.uniform(221, 243), 1, random.uniform(0.1, 0.3))
        time.sleep(random.uniform(3.5, 4.5))
        # 마을의뢰(좌)
        pag.click(random.uniform(20+960, 150+960), random.uniform(100, 120), 1, random.uniform(0.1, 0.3))
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
            time.sleep(1)
            pag.click(random.uniform(907+960, 929+960), random.uniform(47, 62), 1, random.uniform(0.1, 0.3))
            time.sleep(random.uniform(20.5, 24.5))
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


# 미드가르드 20, 150, 100, 120
# 요툰하임 180, 300, 100, 120

left_dailyquest(20, 150, 100, 120)