import time
import mouse
from check_status import check_screen_status
from config import startPositions, storageSpace


def open_storage():
    dX, dY = startPositions[0]['pos']
    cX, cY = startPositions[1]['pos']

    for _ in range(storageSpace):
        mouse.move(dX, dY)
        mouse.click()
        time.sleep(0.01)
        mouse.move(cX, cY)
        mouse.click()
        mouse.click()
        time.sleep(0.01)


def reset_km():
    i = 0
    print('Reseting')
    while True:
        mouse.wheel(1)
        time.sleep(0.001)
        i += 1

        if i % 100 == 0:
            if check_screen_status('start'):
                print("Opening storage")
                open_storage()

                for x in range(4):
                    mouse.wheel(-1)
                    time.sleep(0.5)

                print('Reseted')
                break
    return 0
