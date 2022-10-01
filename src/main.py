from ast import main
from statistics import mode
import sys
from tkinter import font
import pygame as pg
import pygame_menu as pgm
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
    if main_menu.is_enabled():
        main_menu.update()

    for event in pg.event.get():
      if event.type == QUIT:
        pg.quit()
        sys.exit()
    
    # Draw
    screen.fill((0, 0, 0))
    main_menu.draw(screen)
    pg.display.flip()
  
    fpsClock.tick(c.FPS)
    print("FPS: " + str(fpsClock.get_fps()))

if __name__ == '__main__':
  runpg()