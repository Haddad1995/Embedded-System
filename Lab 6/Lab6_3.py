from sense_hat import SenseHat
import time

sense = SenseHat()
p = [2,3]
light_len = 3
space_size = 8
speed = 1/7

r = (255,0,0)
n = (0,0,0)

space = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
r, r, r, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]



def shift_right():
  sense.set_pixel(p[1]-3,p[0],n) 
  sense.set_pixel(p[0]+1,p[1],r) 
  
def shift_left():
  sense.set_pixel(p[0],p[1],n)
  sense.set_pixel(p[0]-3,p[1],r)
  

def main():
  global p
while True:
  while True:
    shift_right()
    time.sleep(speed)
    p[0] += 1
    if p[0] == space_size-1: break
  while True:
    shift_left()
    time.sleep(speed)
    p[0]-= 1
    if p[0] == light_len-1: break