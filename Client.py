import time

import keyboard
import pyautogui


def main(prefix, sleep_time, message):
    time.sleep(3)
    true_sleep_time = int(round(float(sleep_time)))
    screen_dim = pyautogui.size()

    while True:
        pyautogui.click(390 / screen_dim[0] * 1920, 990 / screen_dim[1] * 1080)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):
            exit()
        time.sleep(true_sleep_time)
        if keyboard.is_pressed('esc'):
            exit()
        pyautogui.moveTo(380 / screen_dim[0] * 1920, 930 / screen_dim[1] * 1080)
        pyautogui.mouseDown()
        pyautogui.dragTo(1580 / screen_dim[0] * 1920, 930 / screen_dim[1] * 1080, duration=.2)
        pyautogui.mouseUp()
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp('ctrl')
        pyautogui.click(390 / screen_dim[0] * 1920, 990 / screen_dim[1] * 1080)
        pyautogui.typewrite(prefix + 'c ')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('v')
        pyautogui.keyUp('v')
        pyautogui.keyUp('ctrl')
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):
            exit()


def tester():
    print(pyautogui.size())
    return
    while True:
        print(pyautogui.position())
        time.sleep(1)


if __name__ == '__main__':
    # tester()
    main(input('Bot Prefix: '), input('Clock Speed (seconds): '), input('Start Message: '))
