from pynput.keyboard import Key, Listener
from os import waitpid
import mouse
import time
from pynput import keyboard


dPos = [500, 720]  # Detector position
cPos = [960, 560]  # Chest position (Middle of screen)


for _ in range(50):
    mouse.move(dPos[0], dPos[1])
    mouse.click()
    time.sleep(0.01)
    mouse.move(cPos[0], cPos[1])
    mouse.click()
    mouse.click()
