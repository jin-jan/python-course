import pygame as pg
from utils import ORANGE,PURPLE, FONT

class Player():
    def __init__(self, x, y, w, h, text= ''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = ORANGE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)

    def draw(self, screen):
        self.txt_surface = FONT.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, PURPLE, self.rect, 2)

