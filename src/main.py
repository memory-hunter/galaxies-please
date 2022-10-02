import sys
import pygame as pg
from pygame.locals import *
from pygame import mixer
import constants as c
import helpers as h
from components import button as b


def play_state(screen, items):
    for item in items:
        if isinstance(item, b.Button):
            item.draw(screen)
        else:
            screen.blit(item, (0, 0))

def jwst_map_state():
    pass

def change_music():
    if(c.MUSIC):
        if c.TRACKSTATE == -1:
            c.TRACKSTATE = 0
            mixer.music.load(c.MMBG)
            mixer.music.play(-1, fade_ms=500)
            mixer.music.set_volume(0.5)

        elif c.TRACKSTATE == 0:
            c.TRACKSTATE = 1
            mixer.music.fadeout(500)
            mixer.music.load(c.IGBG)
            mixer.music.play(-1, fade_ms=500)

        elif c.TRACKSTATE == 1:
            c.TRACKSTATE = 0
            mixer.music.fadeout(500)
            mixer.music.load(c.MMBG)
            mixer.music.play(-1, fade_ms=500)
            mixer.music.set_volume(0.5)

def run_game():
    pg.init()
    mixer.init()

    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption(c.TITLE)
    pg.display.set_icon(pg.image.load(c.ICON))

    main_menu = h.setup_main_menu()
    
    table = pg.image.load(c.WORKTABLE).convert_alpha()
    table = pg.transform.scale(table, (c.WIDTH, c.HEIGHT))

    jwstbutton = b.Button(c.WIDTH/1.175, c.HEIGHT/2, pg.image.load(c.WEBBBUTTON).convert_alpha(), 0.3)

    change_music()
    c.GAMESTATE = 0

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
            if c.GAMESTATE == 0:
                change_music()
                c.GAMESTATE = 1

        for event in events:
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        # Draw
        screen.fill((0, 0, 0))

        if main_menu.is_enabled():
            main_menu.draw(screen)
        else:
            if jwstbutton.action:
                jwstbutton.action = False
                jwst_map_state()
            play_state(screen, [table, jwstbutton])

        pg.display.flip()

if __name__ == '__main__':
    run_game()
