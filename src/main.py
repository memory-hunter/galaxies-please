import sys
import pygame as pg
from pygame.locals import *
import constants as c

def update(dt):
  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
 
def draw(screen):
  screen.fill((0, 0, 0))
  
  pg.display.flip()
 
def runpg():
  pg.init()

  fpsClock = pg.time.Clock()

  width, height = c.WIDTH, c.HEIGHT
  screen = pg.display.set_mode((width, height))

  dt = 1/c.FPS
  while True:
    update(dt)
    draw(screen)
    
    dt = fpsClock.tick(c.FPS)

if __name__ == '__main__':
  runpg()