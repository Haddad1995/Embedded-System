from sense_hat import SenseHat
import random
from time import sleep

w = (0,0,0)
r = (255,0,0)
g = (0,128,0)

game_space = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,g,g,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

def update_space(x,y,color):
  p = x*8 + y
  game_space[p] = color
  sense.set_pixels(game_space)
def up(event):
  global direction
  direction = 'up'
def down(event):
  global direction
  direction = 'down'
def left(event):
  global direction
  direction = 'left'
def right(event):
  global direction
  direction = 'right'

def right2():
  global game_alive
  if worm[0][1] == 7 or [worm[0][0],worm[0][1]+1] in worm:
    game_alive = False
  else:
    worm.insert(0,[worm[0][0],worm[0][1]+1])
    update_space(worm[0][0],worm[0][1],g)
    hej = worm.pop()
    update_space(hej[0],hej[1],w)
    update_space(worm[len(worm)-1][0],worm[len(worm)-1][1],g)

def left2():
  global game_alive
  if worm[0][1] == 0 or [worm[0][0],worm[0][1]-1] in worm:
    game_alive = False
  else:
    worm.insert(0,[worm[0][0],worm[0][1]-1])
    update_space(worm[0][0],worm[0][1],g)
    hej = worm.pop()
    update_space(hej[0],hej[1],w)
    update_space(worm[len(worm)-1] [0],worm[len(worm)-1][1],g)

def up2():
  global game_alive
  if worm[0][0] == 0 or [worm[0][0]-1,worm[0][1]] in worm:
    game_alive = False
  else:
    worm.insert(0,[worm[0][0]-1,worm[0][1]])
    update_space(worm[0][0],worm[0][1],g)
    hej = worm.pop()
    update_space(hej[0],hej[1],w)
    update_space(worm[len(worm)-1][0],worm[len(worm)-1][1],g)

def down2():
  global game_alive
  if worm[0][0] == 7 or [worm[0][0]+1,worm[0][1]] in worm:
    game_alive = False
  else:
    worm.insert(0,[worm[0][0]+1,worm[0][1]])
    update_space(worm[0][0],worm[0][1],g)
    hej = worm.pop()
    update_space(hej[0],hej[1],w)
    update_space(worm[len(worm)-1] [0],worm[len(worm)-1][1],g)

def DONOTHING():
  pass

sense = SenseHat()
sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_left = left
sense.stick.direction_right = right

worm = [[4,4],[4,3]]
direction_functions ={'':DONOTHING,'left':left2,'right':right2,'up':up2,'down':down2}
speed = 0.7
direction = ""
sense.clear()
sense.set_pixels(game_space)
game_alive = True

while game_alive:
  score = 0
  while True:
    x = random.randint(0,7)
    y = random.randint(0,7)
    if [x,y] not in worm:
      update_space(x,y,r)
      break
    update_space(x,y,r)
  while True:
    sleep(speed)
    direction_functions[direction]()
    if not game_alive:
      break

#if worm eats the food
if worm[0] == [x,y]:
  worm.append(worm[len(worm)-1])
  speed-=0.05
  score+=1
  while True:
    y = random.randint(0,7)
    x = random.randint(0,7)
    if [x,y] not in worm:
      update_space(x,y,r)
      break

sense.clear()
sense.show_message('Game over!',scroll_speed = 0.05, back_colour = w)
sense.show_message('Score:' + str(score),scroll_speed=0.01, back_colour=w)