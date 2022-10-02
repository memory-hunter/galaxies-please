import pygame as pg
import pygame_menu as pgm
import constants as c


def setup_custom_theme():
    custom_theme = pgm.themes.THEME_DARK.copy()
    custom_theme.title_bar_style = pgm.widgets.MENUBAR_STYLE_NONE
    custom_theme.widget_font = c.BARLOW
    custom_theme.title_font = c.TITILLIUM
    custom_theme.background_color = pgm.BaseImage(image_path=c.WEBB)
    custom_theme.title_close_button = False
    custom_theme.widget_background_color = (30, 30, 30, 200)

    return custom_theme

def toggle_music(menu):
    c.MUSIC = not c.MUSIC
    menu.get_widget("Music").set_title(
        "Music: " + ("On" if c.MUSIC else "Off"))

def setup_main_menu():
    menu = pgm.Menu("", c.WIDTH, c.HEIGHT,
                    theme=setup_custom_theme(),
                    center_content=True,
                    mouse_enabled=True,
                    mouse_motion_selection=True,
                    mouse_visible=True,
                    onclose=pgm.events.CLOSE
                    )
    menu.add.button("Play", pgm.events.CLOSE)
    menu.add.button("Music: " + ("On" if c.MUSIC else "Off"),
                    lambda: toggle_music(menu), button_id="Music")
    menu.add.button("Quit", pgm.events.EXIT)

    return menu