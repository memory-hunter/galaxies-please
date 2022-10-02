import sys

import pygame as pg
from pygame import mixer
from pygame.locals import *

import constants as c
import helpers as h
from components import button as b
from documents import documenthandler

pg.init()
mixer.init()

font = pg.font.Font(c.BARLOW, 15)


def you_are_fired(screen):
    fired = pg.image.load(c.LOST).convert_alpha()
    screen.blit(fired, (0, 0))
    pg.display.update()
    pg.time.wait(3000)
    pg.quit()
    sys.exit()


def you_have_won(screen):
    pass


def pick_documents(handler, screen, buttons):
    arrayforhandler = handler.playdocs[0].to_array()

    name = font.render(arrayforhandler[0], True, (0, 0, 0))
    name_rect = name.get_rect()
    name_rect.center = (c.WIDTH / 2, c.HEIGHT / 10)
    screen.blit(name, name_rect)
    distance = font.render(str(arrayforhandler[3]), True, (0, 0, 0))
    distance_rect = distance.get_rect()
    distance_rect.bottomleft = (500, 145)
    screen.blit(distance, distance_rect)
    type = font.render(arrayforhandler[4], True, (0, 0, 0))
    type_rect = type.get_rect()
    type_rect.bottomleft = (477.5, 220)
    screen.blit(type, type_rect)
    constellation = font.render(arrayforhandler[5], True, (0, 0, 0))
    constellation_rect = constellation.get_rect()
    constellation_rect.bottomleft = (470, 303)
    screen.blit(constellation, constellation_rect)
    size = font.render(arrayforhandler[6], True, (0, 0, 0))
    size_rect = size.get_rect()
    size_rect.bottomleft = (527.5, 379)
    screen.blit(size, size_rect)
    img = pg.image.load(arrayforhandler[1]).convert_alpha()
    screen.blit(img, (685, 148))

    if buttons[1].action:
        buttons[1].action = False
        if not arrayforhandler[-1]:
            handler.mistakes += 1
        handler.playdocs.pop(0)

    elif buttons[2].action:
        buttons[2].action = False
        if arrayforhandler[-1]:
            handler.mistakes += 1
        handler.playdocs.pop(0)

    elif buttons[0].action:
        jwst_map_state(screen, arrayforhandler, buttons)

    if handler.mistakes >= 3:
        handler.playdocs = []
        handler.mistakes = 0
        you_are_fired(screen)
        handler.reinit()

    if len(handler.playdocs) == 0:
        you_have_won(screen)
        handler.reinit()


def play_state(screen, documentsHandler, items):
    for item in items:
        if isinstance(item, list):
            for buttons in item:
                buttons.draw(screen)
        else:
            screen.blit(item, (0, 0))
    c.GAMESTATE = 1
    pick_documents(documentsHandler, screen, items[1])

def jwst_map_state(screen, round, buttons):
    screen.fill((0, 0, 0))
    screen.blit(pg.image.load(round[2]), (0, 0))
    constellation = font.render("Constellation: " + round[5], True, (255, 255, 255))
    distance = font.render("Distance: " + str(round[3] / c.LY) + " Parsecs", True, (255, 255, 255))
    constellation_rect = constellation.get_rect()
    distance_rect = distance.get_rect()
    constellation_rect.bottomleft = (0, c.HEIGHT - 50)
    distance_rect.bottomleft = (0, c.HEIGHT - 25)
    screen.blit(constellation, constellation_rect)
    screen.blit(distance, distance_rect)

    c.GAMESTATE = 2

    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                c.GAMESTATE = 1
                buttons[0].action = False


def change_music():
    if (c.MUSIC):
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
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption(c.TITLE)
    pg.display.set_icon(pg.image.load(c.ICON))

    main_menu = h.setup_main_menu()

    table = pg.image.load(c.WORKTABLE).convert_alpha()
    table = pg.transform.scale(table, (c.WIDTH, c.HEIGHT))

    approve = pg.image.load(c.APPROVEBUTTON).convert_alpha()
    approve = pg.transform.scale(approve, (approve.get_width() / 3, approve.get_height() / 3))
    disapprove = pg.image.load(c.DISAPPROVEBUTTON).convert_alpha()
    disapprove = pg.transform.scale(disapprove, (disapprove.get_width() / 3, disapprove.get_height() / 3))

    jwstbutton = b.Button("JWST", c.WIDTH / 1.175, c.HEIGHT / 2, pg.image.load(c.WEBBBUTTON).convert_alpha(), 0.3)
    approvebutton = b.Button("approve", 100, 650, approve, 1)
    disapprovebutton = b.Button("disapprove", 300, 650, disapprove, 1)
    buttons = [jwstbutton, approvebutton, disapprovebutton]
    documentsHandler = documenthandler.DocumentHandler(2)

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
            play_state(screen, documentsHandler, [table, buttons])

        pg.display.flip()


if __name__ == '__main__':
    run_game()
