import pyautogui as pag
import random
import time

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

def Out():
    pag.click(random.uniform(19, 35), random.uniform(363, 378), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #절전모드(좌)
    pag.click(random.uniform(19+960, 35+960), random.uniform(363, 378), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #절전모드(우)

    pag.click(random.uniform(831, 927), random.uniform(997, 1020), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #방치모드(좌)
    pag.click(random.uniform(831+960, 927+960), random.uniform(997, 1020), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #방치모드(우)

    pag.click(random.uniform(506, 585), random.uniform(721, 733), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #확인(좌)
    pag.click(random.uniform(506+960, 585+960), random.uniform(721, 733), 1, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(1, 1.5))
    #확인(우)

time.sleep(5)
# MoveToOcean()
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

