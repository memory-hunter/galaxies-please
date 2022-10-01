import sys
import pygame as pg
from pygame.locals import *
from pygame import mixer
import constants as c
import helpers as h


def run_game():
    pg.init()
    mixer.init()

    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption(c.TITLE)
    pg.display.set_icon(pg.image.load(c.ICON))

    main_menu = h.setup_main_menu()

    mixer.music.load(c.MMBG)
    mixer.music.play(-1, fade_ms=500)
    mixer.music.set_volume(0.5)

    while True:
        # Update
        events = pg.event.get()
        if main_menu.is_enabled():
            if (c.MUSIC):
                mixer.music.unpause()
            else:
                mixer.music.pause()
            main_menu.update(events)
        else:
            mixer.music.fadeout(500)
            mixer.music.load(c.IGBG)
            mixer.music.play(-1, fade_ms=500)
            mixer.music.set_volume(0.5)

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
    run_game()
