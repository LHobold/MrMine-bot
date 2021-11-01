import mouse
import time
from check_status import check_screen_status
from config import combatPositions


posX = combatPositions['posX']
posY = combatPositions["posY"]


def move_and_click(x, y):
    mouse.move(x, y)
    mouse.click()
    time.sleep(0.01)


def kill_mobs():
    for ci, c in enumerate(posX):
        for ri, r in enumerate(posY):
            move_and_click(c, r)


def kill_mobs_if_exists():
    inCombat = check_screen_status('combat')
    if inCombat:
        print('In combat')
        while True:
            for _ in range(5):
                kill_mobs()
            inCombatStill = check_screen_status('combat')

            if inCombatStill == False:
                break
