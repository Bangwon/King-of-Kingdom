from pynput.mouse import Controller
import time

mouse = Controller()
mouse.position = (0, 0)
mouse.move(50, 50)
for i in range(1000):
	mouse.move(75, 75)
	time.sleep(1)
	mouse.position = (50, 50)
	time.sleep(1)