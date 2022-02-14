
from sense_hat import SenseHat
import time

sense = SenseHat()
state = 0
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

red = [
n, n, n, r, r, n, n, n,
n, n, n, r, r, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
red_yellow =[ 
n, n, n, r, r, n, n, n,
n, n, n, r, r, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
yellow = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
green = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, g, g, n, n, n,
n, n, n, g, g, n, n, n
]
black = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]

def color_state(color,duration):
  sense.set_pixels(color)
  time.sleep(duration)
  sense.clear()

def out_of_order_state():
  sense.set_pixels(yellow)
  time.sleep(0.5)
  sense.clear()
  time.sleep(0.5)

def set_state():
  global state
  if state < 3:
    state += 1
  elif state == 3:
    state = 0
  else: pass

def freezing():
  global previousstate
  if previousstate == 0:
    color_state(red,3)
  elif previousstate == 1:
    color_state(red_yellow,1)
  elif previousstate == 2:
    color_state(green,2)
  elif previousstate == 3:
    color_state(yellow,1)
  elif previousstate == 4:
    out_of_order_state()

def button_event2(event):
  global firstRun, state, previousstate
  if firstRun:
    previousstate = state
    firstRun = False
  if event.action == 'released':
    if state != 5:
      state = 5
    else:
      state = previousstate
      firstRun = True

def button_event(event):
  global state
  if event.action == 'released':
    if state != 4:
      state = 4
    else:
      state = 3

def main():
  global state
  global previousstate
  while True:
    if state == 0:
      color_state(red,3)
    elif state == 1:
      color_state(red_yellow,1)
    elif state == 2:
      color_state(green,2)
    elif state == 3:
      color_state(yellow,1)
    elif state == 4:
      out_of_order_state()
    else:
      freezing()
    set_state()


sense = SenseHat()
state = 0
previousstate = 0
sense.stick.direction_middle = button_event
sense.stick.direction_up = button_event2
firstRun = True
main()