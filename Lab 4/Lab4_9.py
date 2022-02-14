from sense_hat import SenseHat
import time
import random

sense = SenseHat()
while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        sense.show_letter("U") # Up arro
      elif event.direction == "down":
        sense.show_letter("D") # Down arrow
      elif event.direction == "left":
        sense.show_letter("L") # Left arrow
      elif event.direction == "right":
        sense.show_letter("R") # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M") # Enter key
time.sleep(0.5)
sense.clear()