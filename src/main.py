import sys
import pygame as pg
from pygame.locals import *
import constants as c
import helpers as h

def runpg():
  pg.init()
  fpsClock = pg.time.Clock()

  screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
  pg.display.set_caption(c.TITLE)
  pg.display.set_icon(pg.image.load(c.ICON))

  main_menu = h.setup_main_menu()
  main_menu.mainloop(screen)

  while True:
    # Update
    events = pg.event.get()
    if main_menu.is_enabled():
        main_menu.update(events)

    for event in events:
      if event.type == QUIT:
        pg.quit()
        sys.exit()
    
    # Draw
    screen.fill((0, 0, 0))

    if main_menu.is_enabled():
        main_menu.draw(screen)
        
    pg.display.flip()

if __name__ == '__main__':
  runpg()