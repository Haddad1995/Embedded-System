from sense_hat import SenseHat
import time
import random

sense = SenseHat()
# Generate a random color
def random_colour():
  random_red = random.randint (0, 255)
  random_green = random.randint(0, 255)
  random_blue = random.randint(0, 255)
  return (random_red, random_green, random_blue)
  
sense.show_letter("H", random_colour())
# sleep - temporarily pause your program
time.sleep(1)
sense.show_letter("a", random_colour())
time.sleep(1)
sense.show_letter("d", random_colour())
# sleep - temporarily pause your program
time.sleep(1)
sense.show_letter("d", random_colour())
time.sleep(1)
sense.show_letter("a", random_colour())
# sleep - temporarily pause your program
time.sleep(1)
sense.show_letter("d", random_colour())
time.sleep(1)

sense.clear()