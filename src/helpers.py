from ctypes import alignment
import pygame_menu as pgm
import constants as c

def setup_custom_theme():
    custom_theme = pgm.themes.THEME_DARK.copy()
    custom_theme.title_bar_style = pgm.widgets.MENUBAR_STYLE_NONE
    custom_theme.widget_font = c.BARLOW
    custom_theme.title_font = c.TITILLIUM
    custom_theme.background_color = (0, 0, 0, 0)
    custom_theme.title_offset = (18, 0)

    return custom_theme

def setup_main_menu():
    menu = pgm.Menu(c.TITLE, c.WIDTH/2, c.HEIGHT/2, theme=setup_custom_theme(), center_content=True, mouse_enabled=True, mouse_motion_selection=True, mouse_visible=True)
    menu.add.button("Play")
    menu.add.button("Settings")
    menu.add.button("Quit", pgm.events.EXIT)

    return menu
    
