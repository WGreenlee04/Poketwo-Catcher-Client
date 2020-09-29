import time

import clipboard
import keyboard
import pyautogui


def main(prefix):
    if input(
            'Have discord open on your primary monitor in the "maximized"'
            ' mode. Type \'Confirm \'to continue: ').lower != 'confirm':
        exit()
    print('Place your cursor over the Discord text box and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    text_box_pos = pyautogui.position()
    print('Place your cursor behind the fist letter of the last sent message and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    message_pos = pyautogui.position()
    print('Place your cursor at the edge of where the longest message can reach on the screen and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    edge_pos = pyautogui.position()
    print('Bot Starting in 3 Seconds, hold esc to stop the loop.')
    time.sleep(3)

    while True:
        pyautogui.click(text_box_pos.x, text_box_pos.y)
        pyautogui.typewrite('.hint')
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):
            exit()
        time.sleep(1)
        if keyboard.is_pressed('esc'):
            exit()
        pyautogui.moveTo(message_pos.x, message_pos.y)
        pyautogui.mouseDown()
        pyautogui.dragTo(message_pos.x, edge_pos.y, duration=.2)
        pyautogui.mouseUp()
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp('ctrl')
        pyautogui.click(text_box_pos.x, text_box_pos.y)
        if clipboard.paste()[0] == '[':
            text = str(clipboard.paste()).strip('[').strip(']').strip("'")
            mons = text.split("','")
            for mon in mons:
                pyautogui.typewrite(prefix + 'c ' + mon)
                time.sleep(1)


def tester():
    print(pyautogui.size())
    return
    while True:
        print(pyautogui.position())
        time.sleep(1)


if __name__ == '__main__':
    # tester()
    main(input('Bot Prefix: '))
