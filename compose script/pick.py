import pyautogui
import keyboard
import sys
import time
from datetime import datetime, timedelta
# 3 урок сделай сам
# import win32api, win32con

from ahk import AHK

ahk = AHK()

# pyautogui.hotkey('alt', 'tab')
timeStart = datetime.now()
timeFinish = timeStart + timedelta(seconds=60)

# 1 и 2 окно в разных группах

while timeStart < timeFinish:
    # image=r перед картинкой вставка
    try: button1 = pyautogui.locateCenterOnScreen('random_hero.png', minSearchTime=120, confidence=0.9, region=(1815,383, 400, 400))
    except: print('gg')
    pyautogui.sleep(3)
    pyautogui.doubleClick(button1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(3)


    try: button2 = pyautogui.locateCenterOnScreen('random_hero.png', minSearchTime=120, confidence=0.9, region=(1171,376, 400, 400))
    except: print('gg')
    pyautogui.sleep(3)
    pyautogui.doubleClick(button2)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(3)

    try: button3 = pyautogui.locateCenterOnScreen('random_hero.png', minSearchTime=120, confidence=0.9,
                                             region=(541,375, 400, 400))
    except: print('gg')
    pyautogui.sleep(3)
    pyautogui.doubleClick(button3)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(3)

    try:button4 = pyautogui.locateCenterOnScreen('random_hero.png', minSearchTime=120, confidence=0.9,
                                             region=(541,892, 400, 400))
    except: print('gg')
    pyautogui.sleep(3)
    pyautogui.doubleClick(button4)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(2)

    pyautogui.sleep(3)
    try: button5 = pyautogui.locateCenterOnScreen('random_hero.png', minSearchTime=120, confidence=0.9,
                                             region=(1176,891, 400, 400))
    except: print('gg')
    pyautogui.doubleClick(button5)
    pyautogui.sleep(6)
    pyautogui.hotkey('alt', 'tab')
        # прерывает цикл полностью
    print('Я прокликал')
    break



