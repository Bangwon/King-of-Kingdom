from PIL import ImageGrab
import pyautogui as pag
import time
import random

# 퀘스트 순간이동 좌표 893, 216 900 223
# 917, 112 / 935, 147
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
    time.sleep(random.uniform(4.5, 5.55))
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
        cp = (34, 398)
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
    time.sleep(random.uniform(4.5, 5.55))
    # 확인


left_dailyquest()