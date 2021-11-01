from pynput.keyboard import Listener
import mouse
import time
from fight_mob import kill_mobs_if_exists
from reset_km import reset_km
from config import minersX, minersY, skipKm, maxKm, startAt
import win32com.client as comctl
wsh = comctl.Dispatch("WScript.Shell")


###################################################


def pick_chests():
    for xPos in minersX:
        mouse.move(xPos, minersY)
        time.sleep(0.000001)
        mouse.click()

    # Uncomment for chest image detection (not necessary)

    # isChest = check_screen_status('chest')
    # if isChest:
    #     print('Grabbing chest')
    #     mouse.move(cPos[0], cPos[1])
    #     mouse.click()
    #     mouse.click()


def skip_km(curI):
    i = curI
    while True:
        if i in skipKm:
            print('Skipping', i)
            mouse.wheel(-1)
            time.sleep(0.5)
            i += 1
        if i not in skipKm:
            break
    return i


def go_down(i):
    mouse.move(minersX[len(minersX)-1] + 100, minersY)
    mouse.wheel(-1)
    time.sleep(0.0001)

    # Press esc every row to ensure no cave popup
    mouse.move(minersX[5], minersY)
    time.sleep(0.0001)
    mouse.click()
    wsh.SendKeys("{esc}")

    return (i + 1)


while True:
    def on_press_start(key):
        if (hasattr(key, 'char')):
            if key.char == 'u':
                print('starting...')
                return False

    def on_press_loop(key):
        if (hasattr(key, 'char')):
            if key.char == 'i':
                return False

    with Listener(on_press=on_press_start) as listener:
        listener.join()

    with Listener(on_press=on_press_loop) as listener:
        i = startAt
        while listener.running:

            i = skip_km(i)
            pick_chests()
            i = go_down(i)

            if i % 3 == 0:
                kill_mobs_if_exists()

            if (i == maxKm):
                i = reset_km()
                continue

        time.sleep(1)
        if not listener.running:
            break
