from microbit import *
import random

while not button.a.get_pressed():
    display.scroll("ONE")
    sleep(2000)
