import pygame as pg
from utils import COLOR_INACTIVE, COLOR_ACTIVE, BLUE4, PURPLE, FONT


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.rect_message = pg.Rect(x-200, y-100, 500, h)
        self.color_message = BLUE4
        self.color = COLOR_INACTIVE
        self.txt_surf_msg = FONT.render("Guess the word, type one letter", True, self.color_message)
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                if len(self.text) > 1:
                    self.rect_message.w = 248
                    self.txt_surf_msg = FONT.render("One letter only", True, self.color_message)
                    self.text = self.text[:-1]
                self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surf_msg, (self.rect_message.x, self.rect_message.y))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        self.rect.w = 100
        pg.draw.rect(screen, self.color, self.rect, 2)
        pg.draw.rect(screen, PURPLE, self.rect_message, 2)

