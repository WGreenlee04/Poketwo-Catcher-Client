import random
import time
import webbrowser

import clipboard
import keyboard
import pyautogui


def main(prefix, high_duration):
    print('This bot uses the WEB BASED version of discord.')
    discord_url = input('Please give the url of your chosen discord channel: ')
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
    input(
        'Make sure the browser you choose to run discord in has NO TABS OPEN and is not running.'
        'Type \'Confirm \'to continue: ')
    print('Bot Starting in 3 Seconds, hold esc to stop the loop.')
    time.sleep(3)
    webbrowser.open(discord_url)
    time.sleep(5)
    clipboard.copy(str(random.random()))

    def sendMessage(message):
        pyautogui.click(text_box_pos.x, text_box_pos.y)
        pyautogui.typewrite(message)
        pyautogui.press('enter')

    def copy():
        pyautogui.moveTo(message_pos.x, message_pos.y)
        pyautogui.mouseDown()
        pyautogui.dragTo(edge_pos.x, message_pos.y, duration=high_duration)
        pyautogui.mouseUp()
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp('ctrl')

    while True:
        start_clipboard = clipboard.paste()
        cb_changed = False
        # should cover one pokemon spawn timer
        for i in range(0, 30):
            sendMessage('spawn')
            if keyboard.is_pressed('esc'):
                exit()
            time.sleep(1)
            if keyboard.is_pressed('esc'):
                exit()

        sendMessage(f'{prefix}hint')
        copy()
        cb_changed = cb_changed or (clipboard.paste() != start_clipboard)
        pyautogui.click(text_box_pos.x, text_box_pos.y)
        pastebin = clipboard.paste()
        if pastebin and len(pastebin) != 0 and pastebin[0] == '[':
            text = str(pastebin).strip().strip('\n').strip('[').strip(']').strip('\'')
            mons = text.split('\', \'')
            for mon in mons:
                pyautogui.typewrite(f'{prefix}c {mon}')
                pyautogui.press('enter')

        if not cb_changed:
            # restart the discord window
            pyautogui.click(exit_button_pos.x, exit_button_pos.y)
            webbrowser.open(discord_url)
            time.sleep(8)


if __name__ == '__main__':
    main(input('Bot Prefix: '), float(input('Highlight Duration (default .12s): ') or .12))
