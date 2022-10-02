import pygame as pg


class Button:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.action = False

    def draw(self, screen):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = pg.transform.scale(self.original_image,
                                            (int(self.rect.width * 1.1), int(self.rect.height * 1.1)))
            if pg.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.action = True
        else:
            self.image = self.original_image

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
