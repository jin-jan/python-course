import pygame as pg
import random
from utils import LIST_DICTIONARY, COLOR_LINES, ORANGE, PURPLE, FONT

class GuessWord:
    def __init__(self):
        self.guess_word = ""
        self.x = 150
        self.w = 190
        self.new_x = 40
        self.new_y = 50
        self.space = 10
        self.y, self.h, = 130, 130
        self.color = COLOR_LINES
        self.rect = []
        self.txt_surface = FONT.render('', True, self.color)
        self.txt_surf_win = FONT.render('You won!', True, ORANGE)
        self.rect_win = pg.Rect(self.x + 150, self.y + 60, self.w - 50, self.h - 80)

    def random_word(self):
        rand_num = random.randint(0, len(LIST_DICTIONARY) - 1)
        self.guess_word = LIST_DICTIONARY[rand_num]
        return self.guess_word

    def check_in(self, letter, print_word):
        for i in range(len(self.guess_word)):
            if self.guess_word[i] == letter:
                print_word[i] = letter
        return print_word

    def draw_lines(self, screen, print_word):
        x = self.x
        w = self.w
        new_x = self.new_x
        space = self.space
        y, h = self.y, self.h
        txt = [" " if not i else i for i in print_word]
        for i in range(len(self.guess_word)):
            self.rect.append(pg.Rect(x, y-self.new_y, new_x, new_x))
            self.txt_surface = FONT.render(txt[i], True, self.color)
            screen.blit(self.txt_surface, (self.rect[i].x + 5, self.rect[i].y-5))
            pg.draw.line(
                screen, COLOR_LINES, (x, y), (w, h), 5)
            pg.draw.rect(screen, PURPLE, self.rect[i], 2)
            x = x + new_x + space
            w = w + new_x + space
        if all([' ' != i for i in txt]):
            screen.blit(self.txt_surf_win, (self.rect_win.x + 5, self.rect_win.y - 5))
            pg.draw.rect(screen, PURPLE, self.rect_win, 2)


