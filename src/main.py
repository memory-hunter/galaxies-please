import sys
import pygame as pg
from pygame.locals import *
from pygame import mixer
import constants as c
import helpers as h
from components import button as b
from documents import documenthandler

pg.init()
mixer.init()

font = pg.font.Font(c.BARLOW, 15)


def pick_documents(handler, screen):
    round = handler.playdocs[0].to_array()
    name = font.render(round[0], True, (0, 0, 0))
    name_rect = name.get_rect()
    name_rect.center = (c.WIDTH / 2, c.HEIGHT / 10)
    screen.blit(name, name_rect)
    distance = font.render(round[3], True, (0, 0, 0))
    distance_rect = distance.get_rect()
    distance_rect.bottomleft = (500, 145)
    screen.blit(distance, distance_rect)
    type = font.render(round[4], True, (0, 0, 0))
    type_rect = type.get_rect()
    type_rect.bottomleft = (477.5, 220)
    screen.blit(type, type_rect)
    constellation = font.render(round[5], True, (0, 0, 0))
    constellation_rect = constellation.get_rect()
    constellation_rect.bottomleft = (470, 303)
    screen.blit(constellation, constellation_rect)
    size = font.render(round[6], True, (0, 0, 0))
    size_rect = size.get_rect()
    size_rect.bottomleft = (527.5, 379)
    screen.blit(size, size_rect)
    img = pg.image.load(round[1]).convert_alpha()
    screen.blit(img, (685, 148))

    # if action == "acc":
    #     if not round[-1]:
    #         mistakes += 1
    #     playdocs.pop(0)

    # elif action == "den":
    #     if round[-1]:
    #         mistakes += 1
    #     playdocs.pop(0)

    # if mistakes >= 3:
    #     return False

    # if len(playdocs) == 0:
    #     print(mistakes)
    #     return True


def play_state(screen, items, documentsHandler):
    for item in items:
        if isinstance(item, b.Button):
            item.draw(screen)
        else:
            screen.blit(item, (0, 0))
    pick_documents(documentsHandler, screen)


def jwst_map_state():
    pass

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

    jwstbutton = b.Button(c.WIDTH / 1.175, c.HEIGHT / 2, pg.image.load(c.WEBBBUTTON).convert_alpha(), 0.3)

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
            if event.type == MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(pos)

        # Draw
        screen.fill((0, 0, 0))

        if main_menu.is_enabled():
            main_menu.draw(screen)
        else:
            if jwstbutton.action:
                jwstbutton.action = False
                jwst_map_state()
            play_state(screen, [table, jwstbutton], documentsHandler)

        pg.display.flip()


if __name__ == '__main__':
    run_game()
