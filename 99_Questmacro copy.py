import pyautogui as pag
import random
import keyboard
import time
from PIL import ImageGrab

cp3 = (689, 130)
color = (255, 235, 161)

# skip 좌표 890 45 940 60

def left_quest():
    # 센터 (좌)
    Left_Center = {
    'top_left': {
    'x': 428,
    'y': 762
    },
    'bottom_right': {
    'x':574,
    'y':837
    }
    }


    # 퀘스트 (좌)
    Left_Quest = {
    'top_left': {
    'x': 718,
    'y': 111
    },
    'bottom_right': {
    'x':871,
    'y':150
    }
    }

    while True:

        # 조건부 센터 클릭
        t = 0  
        while True:
            rgb = ImageGrab.grab().getpixel(cp3)
            if rgb == color:
                pag.moveTo(
                    x = random.uniform(Left_Center['top_left']['x'], Left_Center['bottom_right']['x']),
                    y = random.uniform(Left_Center['top_left']['y'], Left_Center['bottom_right']['y']),
                duration=random.uniform(0.1, 0.2)
                )
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.20))
                pag.mouseUp()
                time.sleep(random.uniform(0.05, 0.20))
                t += 1
                time.sleep(random.uniform(1.55, 4.89))
                print(time.ctime())
                print(rgb)
            else :
                time.sleep(1)
                print(rgb)
                print(time.ctime())
                break
            
        # 퀘스트 클릭 (좌)        
        pag.moveTo(
            x = random.uniform(Left_Quest['top_left']['x'], Left_Quest['bottom_right']['x']),
            y = random.uniform(Left_Quest['top_left']['y'], Left_Quest['bottom_right']['y']),
        duration=random.uniform(0.2, 0.5)
        )
        pag.mouseDown()
        time.sleep(random.uniform(0.15001, 0.29987))
        pag.mouseUp()
        time.sleep(random.uniform(0.32591, 1.16987))
        
        pag.moveTo(
            x = random.uniform(Left_Quest['top_left']['x'], Left_Quest['bottom_right']['x']),
            y = random.uniform(Left_Quest['top_left']['y'], Left_Quest['bottom_right']['y']),
        duration=random.uniform(0.2, 0.5)
        )
        pag.mouseDown()
        time.sleep(random.uniform(0.15001, 0.29987))
        pag.mouseUp()
        time.sleep(random.uniform(0.32591, 1.16987))

        pag.moveTo(
            x = random.uniform(Left_Quest['top_left']['x'], Left_Quest['bottom_right']['x']),
            y = random.uniform(Left_Quest['top_left']['y'], Left_Quest['bottom_right']['y']),
        duration=random.uniform(0.2, 0.5)
        )
        pag.mouseDown()
        time.sleep(random.uniform(0.15001, 0.29987))
        pag.mouseUp()
        time.sleep(random.uniform(0.32591, 1.16987))

        time.sleep(random.uniform(0.5, 1.234))

        if keyboard.is_pressed('F4'): # F4 누르면
            break # while문 탈출

def right_quest():
    # 센터 (우)
    Right_Center = {
    'top_left': {
    'x': 1371,
    'y': 773
    },
    'bottom_right': {
    'x':1535,
    'y':837
    }
    }

    # 퀘스트 (우)
    Right_Quest  = {
    'top_left': {
    'x': 1668,
    'y': 112
    },
    'bottom_right': {
    'x':1822,
    'y':153
    }
    }

    while True:
    
        # 센터 10연타 (우)
        t = 0  
        while True:
            pag.moveTo(
                x = random.uniform(Right_Center['top_left']['x'], Right_Center['bottom_right']['x']),
                y = random.uniform(Right_Center['top_left']['y'], Right_Center['bottom_right']['y']),
            duration=random.uniform(0.1, 0.2)
            )
            pag.mouseDown()
            time.sleep(random.uniform(0.05, 0.20))
            pag.mouseUp()
            time.sleep(random.uniform(0.05, 0.20))
            t += 1
            time.sleep(0.5)
            if t==10 :
                break
            # 퀘스트 클릭 (우)        
            pag.moveTo(
                x = random.uniform(Right_Quest['top_left']['x'], Right_Quest['bottom_right']['x']),
                y = random.uniform(Right_Quest['top_left']['y'], Right_Quest['bottom_right']['y']),
            duration=random.uniform(0.2, 0.5)
            )
            pag.mouseDown()
            time.sleep(random.uniform(0.15001, 0.29987))
            pag.mouseUp()
            time.sleep(random.uniform(0.32591, 1.16987))
            
            time.sleep(20)

            if keyboard.is_pressed('F4'): # F4 누르면
                break # while문 탈출

left_quest()