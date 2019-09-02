import datetime
import os
import random

# startX = random.randint(197, 876)
# startY = random.randint(1356, 1634, 1)
# endX = random.randint(321, 965)
# endY = random.randint(567, 789)
# watchTime = random.randint(14, 36)
# swipeTime = random.randint(0.9, 1.5)
import time


def tap(x, y):
    cmd_tap = 'adb shell input tap {x} {y}'.format(
        x=x,
        y=y
    )
    os.system(cmd_tap)
    print(cmd_tap + ' tap')


def sleep(s):
    print('sleep ' + str(s) + 'S')
    time.sleep(s)


def input_str(string):
    get_time()
    print('------------------ input------------')
    # vivo
    # tap('1000', '1800')
    # xiaomi
    tap('960', '1400')
    sleep(1)
    # vivo
    # tap('540', 2280)
    #xiaomi
    tap('540', '1845')
    sleep(1)
    cmd_input = 'adb shell input text "{s}"'.format(s=string)
    os.system(cmd_input)
    print(cmd_input + ' input')
    time.sleep(random.uniform(0.8, 1.5))
    tap('970', '1845')
    print('enter ' + string)
    time.sleep(random.uniform(1, 1.8))
    cmd_back = 'adb shell input keyevent 4'
    os.system(cmd_back)
    print(cmd_back + ' back')
    input_sleep = random.uniform(0.9, 1.5)
    print('input_sleep ' + str(input_sleep) + 'S')
    time.sleep(input_sleep)


def like():
    get_time()
    # cmd_like = 'adb shell input tap {x} {y}'.format(
    #     x=random.randint(321, 784),
    #     y=random.randint(456, 1456)
    # )
    # # os.system(cmd_like)
    # tap('500', '1000')
    # time.sleep(0.1)
    print('------------------ like------------')
    tap('968', '1040')
    # os.system(cmd_like)
    like_sleep = random.uniform(1.2, 1.8)
    print('like sleep ' + str(like_sleep) + 'S')
    time.sleep(like_sleep)


def swipe():
    get_time()
    print('------------------ swipe------------')
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=random.randint(197, 876),
        y1=random.randint(1356, 1634),
        x2=random.randint(321, 965),
        y2=random.randint(567, 789),
        duration=random.randint(234, 321)
    )
    os.system(cmd)
    print(cmd + ' swipe')
    t = random.randint(14, 30)
    print('swipe sleep ' + str(t) + 's')
    time.sleep(t)


def get_time():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


while True:
    swipe()
    #input_str('66666')
    like()
