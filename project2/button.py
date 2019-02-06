import pygame as pg
from utils import COLOR_INACTIVE, COLOR_ACTIVE, FONT


class Button:
    def __init__(self, x, y, w, h, text='', action=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.action = action
        self.start_action = False
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action == 'quit':
                    pg.quit()
                    quit()
                if self.action == 'start':
                    self.active = not self.active
                    self.start_action = True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        return self.start_action

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)
