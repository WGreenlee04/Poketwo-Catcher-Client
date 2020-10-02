import random
import subprocess
import time
from pathlib import Path

import clipboard
import keyboard
import pyautogui


def main(prefix, high_duration):
    input(
        'Have discord open in browser to the channel you wish in the "maximized"'
        ' mode. IT MUST BE THE ONLY TAB OPEN IN THAT BROWSER. Type \'Confirm \'to continue: ')
    discord_url = input('Please give the url of your discord channel '
                        '(leave blank for no error checking): ')
    err_chk = bool(discord_url)
    if err_chk:
        browser_path = Path(input('Please give the path to your chosen browser executable on your system: '))
    print('Place your cursor over the Discord text box and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    text_box_pos = pyautogui.position()
    time.sleep(1)
    print('Place your cursor behind the fist letter of the last sent message and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    message_pos = pyautogui.position()
    time.sleep(1)
    print('Place your cursor at the edge of where the longest message can reach on the screen and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    edge_pos = pyautogui.position()
    time.sleep(1)
    print('Place your cursor over the exit button to the open browser tab and press esc.')
    while not keyboard.is_pressed('esc'):
        pass
    exit_button_pos = pyautogui.position()
    print('Bot Starting in 3 Seconds, hold esc to stop the loop.')
    time.sleep(3)

    while True:
        if err_chk:
            key = random.random()
            clipboard.copy(str(key))
        # should cover one pokemon spawn timer
        for i in range(0, 20):
            pyautogui.click(text_box_pos.x, text_box_pos.y)
            pyautogui.typewrite(f'{prefix}hint')
            pyautogui.press('enter')
            if keyboard.is_pressed('esc'):
                exit()
            time.sleep(1)
            if keyboard.is_pressed('esc'):
                exit()
            pyautogui.moveTo(message_pos.x, message_pos.y)
            pyautogui.mouseDown()
            pyautogui.dragTo(edge_pos.x, message_pos.y, duration=high_duration)
            pyautogui.mouseUp()
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('c')
            pyautogui.keyUp('c')
            pyautogui.keyUp('ctrl')
            pyautogui.click(text_box_pos.x, text_box_pos.y)
            try:
                pastebin = clipboard.paste()
                if pastebin and pastebin[0] == '[':
                    text = str(pastebin).strip().strip('\n').strip('[').strip(']').strip('\'')
                    mons = text.split('\', \'')
                    for mon in mons:
                        pyautogui.typewrite(prefix + 'c ' + mon)
                        pyautogui.press('enter')
            except IndexError:
                print("Pokemon detected.")
        try:
            test = float(clipboard.paste())
        except ValueError:
            test = 0
        if err_chk and test == key:
            # restart the discord window
            pyautogui.click(exit_button_pos.x, exit_button_pos.y)
            subprocess.run(browser_path)
            time.sleep(5)
            pyautogui.typewrite(discord_url)
            pyautogui.press('enter')
            time.sleep(5)


if __name__ == '__main__':
    main(input('Bot Prefix: '), float(input('Highlight Duration (default .12s): ') or .12))
