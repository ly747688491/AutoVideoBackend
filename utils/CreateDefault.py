import math
import random
import time


def create_default_name():
    time_stamp = lambda: int(round(time.time() * 1000))
    random_number = random.randint(1, time_stamp())
    if int(math.log10(random_number) + 1) < 13:
        random_number = random_number * 10 * (13 - int(math.log10(random_number) + 1))
    return f"无名氏{random_number}"
