import time
import ahk
import pyautogui
import asyncio
from threading import Thread
import keyboard
import pydirectinput
# pyautogui.sleep(75)

def unblock():
    pyautogui.press('o')
    time.sleep(0.3)
    pyautogui.press('q')
    time.sleep(0.3)
    pyautogui.press('Esc')
def dire_1d_boost():

    def active_window_1d_boost():
        time.sleep(2)
        pydirectinput.moveTo(166,469)
        pydirectinput.doubleClick()
        pyautogui.sleep(0.3)
        unblock()

    active_window_1d_boost()


    def map_navigation_1dboost():
        # save_zone
        ahk.mouse_move(554,425, speed=80)
        pyautogui.sleep(1)
        ahk.right_click()


    map_navigation_1dboost()

    time.sleep(50)


    def line_self_1dboost():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')


    line_self_1dboost()


    def line_patrol_1dboost():
        pyautogui.sleep(2)
        pyautogui.press('p')
        ahk.mouse_move(568,312, speed=45.241)
        pyautogui.sleep(2)
        ahk.click()


    line_patrol_1dboost()
    pyautogui.sleep(0.3)
    pyautogui.hotkey('alt', 'tab')

dire_1d_boost()

def direboost_2():

    def active_window_2d():
        pydirectinput.moveTo(798,474)
        pydirectinput.click()
        time.sleep(0.3)
        unblock()

    active_window_2d()
    # keyboard.press_and_release('shift+s, space')
    def map_navigation_2d():
        pydirectinput.moveTo(1181,427)
        pyautogui.sleep(0.3)
        pyautogui.rightClick()
    #     pyautogui.moveTo(1011,263)ё
    #     pyautogui.doubleClick()
    #     pyautogui.sleep(0.3)
    #
    map_navigation_2d()
    #

    pyautogui.sleep(55)
    def line_self_2d():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.sleep(0.34)
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')

    line_self_2d()
    def line_patrol_2d():
        pyautogui.sleep(4)
        pyautogui.press('p')
        pydirectinput.moveTo(1188,166)
        pyautogui.sleep(2)
        ahk.click()
    line_patrol_2d()
    #
    # map_navigation_2d()
    pyautogui.sleep(0.3)
    pyautogui.hotkey('alt', 'tab')


direboost_2()
# t1 = Thread(target = radiant_1boost)

def radiant_3():

    def active_window_3r():
        time.sleep(6)
        pydirectinput.moveTo(1447,461)
        pydirectinput.doubleClick()
        time.sleep(0.3)
        unblock()
    active_window_3r()
    # keyboard.press_and_release('shift+s, space')
    def map_navigation_3r():
        pydirectinput.moveTo(1850,462)
        pyautogui.sleep(0.3)
        ahk.right_click()
    #     pyautogui.moveTo(1011,263)ёp
    #     pyautogui.doubleClick()
    #     pyautogui.sleep(0.3)
    #
    map_navigation_3r()
    #

    pyautogui.sleep(50)

    def line_self_3r():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')
    line_self_3r()
    def line_patrol_3r():
        pyautogui.sleep(3)
        pyautogui.press('p')
        pydirectinput.moveTo(1762,388)
        pyautogui.sleep(2)
        ahk.click()
    line_patrol_3r()

    pyautogui.sleep(0.3)
    pyautogui.hotkey('alt', 'tab')

def dire_3():

    def active_window_3d():
        time.sleep(6)
        pydirectinput.moveTo(1437,465)
        pydirectinput.doubleClick()
        time.sleep(0.3)

    active_window_3d()
    # keyboard.press_and_release('shift+s, space')oq
    def map_navigation_3d():
        pydirectinput.moveTo(1862,460)
        pyautogui.sleep(0.3)
        ahk.right_click()
    #     pyautogui.moveTo(1011,263)ёp
    #     pyautogui.doubleClick()
    #     pyautogui.sleep(0.3)
    #
    map_navigation_3d()
    #

    pyautogui.sleep(50)

    def line_self_3d():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')
    line_self_3d()
    def line_patrol_3d():
        pyautogui.sleep(3)
        pyautogui.press('p')
        pydirectinput.moveTo(1413,178)
        pyautogui.sleep(2)
        ahk.click()
    line_patrol_3d()

    pyautogui.sleep(0.3)
    pyautogui.hotkey('alt', 'tab')

dire_3()


def dire_4():
    def active_window_4d():
        pyautogui.sleep(7)
        pydirectinput.moveTo(146,973)
        pydirectinput.doubleClick()
        time.sleep(0.3)
        unblock()

    active_window_4d()
    # keyboard.press_and_release('shift+s, space')
    def map_navigation_4d():
        pydirectinput.moveTo(618,985)
        pyautogui.sleep(0.3)
        pyautogui.rightClick()
    #     pyautogui.moveTo(1011,263)ё
    #     pyautogui.doubleClick()
    #     pyautogui.sleep(0.3)
    #
    map_navigation_4d()
    #

    pyautogui.sleep(45)

    def line_self_4d():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')

    line_self_4d()
    def line_patrol_4d():
        pyautogui.sleep(2)
        pyautogui.press('p')
        pydirectinput.moveTo(580,675)
        pyautogui.sleep(2)
        ahk.click()
    line_patrol_4d()
    #
    # map_navigation_2r()

    pyautogui.sleep(0.5)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(0.5)

dire_4()

def dire_5boost():
    def active_window_5d():
        pyautogui.sleep(7)
        pydirectinput.moveTo(803,974)
        pydirectinput.doubleClick()
        time.sleep(0.6)
        pydirectinput.click()
        unblock()
        pyautogui.sleep(0.3)


    active_window_5d()
    # keyboard.press_and_release('shift+s, space')
    def map_navigation_5d():
        pydirectinput.moveTo(1258,986)
        pyautogui.sleep(0.3)
        pyautogui.rightClick()
    #     pyautogui.moveTo(1011,263)ё
    #     pyautogui.doubleClick()
    #     pyautogui.sleep(0.3)
    #
    map_navigation_5d()
    #

    pyautogui.sleep(50)

    def line_self_5d():
        pyautogui.sleep(3)
        pyautogui.press('f1')
        pyautogui.press('f1')
        pyautogui.sleep(1.2)
        pyautogui.press('f1')

    line_self_5d()
    def line_patrol_5d():
        pyautogui.sleep(2)
        pyautogui.press('p')
        pydirectinput.moveTo(961,702)
        pyautogui.sleep(2)
        ahk.click()
    line_patrol_5d()
    #
    # map_navigation_2r()

    pyautogui.sleep(0.5)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(0.5)

dire_5boost()

# t4 = Thread(target=radiant_4)