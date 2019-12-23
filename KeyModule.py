import pyautogui
import time

KEY_HOLD_TIME = 1
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'


def press_key(key):
    pyautogui.keyDown(key)
    time.sleep(KEY_HOLD_TIME)
    pyautogui.keyUp(key)


def initiate():
    print('Starting:')
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
