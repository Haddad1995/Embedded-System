from sense_hat import SenseHat
import time
import random

sense = SenseHat()
w = (255, 255, 255) # white
b = (0, 0, 255) # blue

smiley_pixels = [
  w, w, w, w, w, w, w, w,
  w, b, b, w, w, b, b, w,
  w, b, b, w, w, b, b, w,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  w, b, w, w, w, w, b, w,
  w, w, b, b, b, b, w, w,
  w, w, w, w, w, w, w, w]
  
sense.set_pixels(smiley_pixels)