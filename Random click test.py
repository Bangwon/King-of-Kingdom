import pyautogui as pag
import time
import random
import keyboard

login_button = {'top_left': {'x':1414, 'y':91}, 'bottom_right': {'x': 1553, 'y': 121}}
kakao_button = {'top_left': {'x':757, 'y':337}, 'bottom_right': {'x': 1160, 'y': 373}}
id_click = {'top_left': {'x':1078, 'y':317}, 'bottom_right': {'x': 1294, 'y': 327}}
gamestart = {'top_left': {'x':1566, 'y':145}, 'bottom_right': {'x': 1893, 'y': 205}}
connect = {'top_left': {'x':980, 'y':60}, 'bottom_right': {'x': 1885, 'y': 1007}}
first_id_connect = {'top_left': {'x':1830, 'y':100}, 'bottom_right': {'x': 1870, 'y': 135}}
gameconnect = {'top_left': {'x':1919, 'y':951}, 'bottom_right': {'x': 1880, 'y': 1007}}

time.sleep(5)
pag.hotkey('win', 'd')
time.sleep(0.5)
pag.click(40, 440, 2, 0.2)
# 오딘 아이콘 더블클릭
time.sleep(random.uniform(2.55, 3.59))
pag.click(1487, 106)
# 로그아웃 버튼
time.sleep(random.uniform(2.55, 3.59))
pag.moveTo(
x=random.uniform(login_button['top_left']['x'], login_button['bottom_right']['x']),
y=random.uniform(login_button['top_left']['y'], login_button['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# 로그인 버튼
time.sleep(random.uniform(2.55, 3.59))
pag.moveTo(
x=random.uniform(kakao_button['top_left']['x'], kakao_button['bottom_right']['x']),
y=random.uniform(kakao_button['top_left']['y'], kakao_button['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# 카카오계정 선택
time.sleep(random.uniform(2.55, 3.59))
pag.moveTo(
x=random.uniform(id_click['top_left']['x'], id_click['bottom_right']['x']),
y=random.uniform(id_click['top_left']['y'], id_click['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# 아이디 입력 선택
pag.typewrite("choisungwoo888@gmail.com", interval=random.uniform(0.124, 0.199))
pag.press("tab")
pag.typewrite("!sungwoo88", interval=random.uniform(0.124, 0.199))
# 아이디/비번입력
time.sleep(random.uniform(0.599, 1.32))
pag.press("tab")
pag.press("enter")
# 로그인 버튼
time.sleep(random.uniform(2.55, 3.59))
pag.moveTo(
x=random.uniform(gamestart['top_left']['x'], gamestart['bottom_right']['x']),
y=random.uniform(gamestart['top_left']['y'], gamestart['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# GAME START
time.sleep(random.uniform(20, 25))
pag.click(900, 1060)
time.sleep(2)
pag.click(960, 970)
pag.keyDown('winleft')
pag.press('right')
# 오딘 클라이언트 우측으로 보내기
time.sleep(random.uniform(20, 25))
pag.moveTo(
x=random.uniform(connect['top_left']['y'], connect['bottom_right']['y']),
y=random.uniform(connect['top_left']['y'], connect['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(2)
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
# 접속
time.sleep(random.uniform(4, 6))
pag.moveTo(
x=random.uniform(first_id_connect['top_left']['x'], first_id_connect['bottom_right']['x']),
y=random.uniform(first_id_connect['top_left']['y'], first_id_connect['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# 첫 번째 아이디 선택
time.sleep(random.uniform(2.55, 3.59))
pag.moveTo(
x=random.uniform(gameconnect['top_left']['x'], gameconnect['bottom_right']['x']),
y=random.uniform(gameconnect['top_left']['y'], gameconnect['bottom_right']['y']),
duration=random.uniform(0.456, 0.999))
pag.mouseDown()
time.sleep(random.uniform(0.139, 0.299))
pag.mouseUp()
time.sleep(random.uniform(0.139, 0.299))
# 게임하기선택