from microbit import *

while True:
  if button_a.is_pressed() and butt/on_b.is_pressed():
    display.show(Image.ARROW_N)
  elif button_a.is_pressed():
    display.show(Image.ARROW_W)
  elif button_b.is_pressed():
    display.show(Image.ARROW_E)