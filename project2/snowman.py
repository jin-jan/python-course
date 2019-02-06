import pygame as pg
from utils import WHITE, BLACK, PURPLE, ORANGE, RED, COLOR_ACTIVE, FONT


class SnowMan:
    def __init__(self, wrong_letter=''):
        self.x = 150
        self.y = 450
        self.wrong_letter = wrong_letter
        self.rect = pg.Rect(self.x - 40, self.y - 270, 100, 50)
        self.color = PURPLE
        self.text = 'Lost!'
        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw_snowman(self, screen):
        if len(self.wrong_letter) == 1:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
        elif len(self.wrong_letter) == 2:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
        elif len(self.wrong_letter) == 3:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
        elif len(self.wrong_letter) == 4:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
        elif len(self.wrong_letter) == 5:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK,
                         (self.x - 90, self.y - 120),
                         (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
        elif len(self.wrong_letter) == 6:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
        elif len(self.wrong_letter) == 7:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
        elif len(self.wrong_letter) == 8:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
        elif len(self.wrong_letter) == 9:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
        elif len(self.wrong_letter) == 10:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 80), 5)
        elif len(self.wrong_letter) == 11:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 80), 5)
            pg.draw.polygon(screen, ORANGE,
                            ((self.x, self.y - 140), (self.x, self.y - 155), (self.x + 60, self.y - 155)), 0)
        elif len(self.wrong_letter) == 12:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 80), 5)
            pg.draw.polygon(screen, ORANGE,
                            ((self.x, self.y - 140), (self.x, self.y - 155), (self.x + 60, self.y - 155)), 0)
            pg.draw.circle(screen, BLACK, (self.x - 10, self. y - 160), 10)
        elif len(self.wrong_letter) == 13:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 80), 5)
            pg.draw.polygon(screen, ORANGE,
                            ((self.x, self.y - 140), (self.x, self.y - 155), (self.x + 60, self.y - 155)), 0)
            pg.draw.circle(screen, BLACK, (self.x - 10, self. y - 160), 10)
            pg.draw.circle(screen, BLACK, (self.x + 15, self.y - 160), 6)
        elif len(self.wrong_letter) == 14:
            pg.draw.circle(screen, WHITE, (self.x, self.y), 80)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 80), 50)
            pg.draw.circle(screen, WHITE, (self.x, self.y - 150), 40)
            pg.draw.line(screen, BLACK, (self.x - 90, self.y - 120), (self.x - 40, self.y - 90), 7)
            pg.draw.line(screen, BLACK, (self.x + 40, self.y - 90), (self.x + 90, self.y - 120), 7)
            pg.draw.lines(screen, BLACK, False, [(self.x - 120, self.y - 100),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 130, self.y - 120),
                                                 (self.x - 90, self.y - 120),
                                                 (self.x - 125, self.y - 140)], 5)
            pg.draw.lines(screen, BLACK, False, [(self.x + 120, self.y - 100),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 130, self.y - 120),
                                                 (self.x + 90, self.y - 120),
                                                 (self.x + 125, self.y - 140)], 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 110), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 95), 5)
            pg.draw.circle(screen, RED, (self.x, self.y - 80), 5)
            pg.draw.polygon(screen, ORANGE,
                            ((self.x, self.y - 140), (self.x, self.y - 155), (self.x + 60, self.y - 155)), 0)
            pg.draw.circle(screen, BLACK, (self.x - 10, self. y - 160), 10)
            pg.draw.circle(screen, BLACK, (self.x + 15, self.y - 160), 6)
            pg.draw.polygon(screen, BLACK, ((self.x - 50, self.y - 185),
                                            (self.x + 50, self.y - 185),
                                            (self.x + 50, self.y - 200),
                                            (self.x - 30, self.y - 200),
                                            (self.x - 30, self.y - 220),
                                            (self.x + 30, self.y - 220),
                                            (self.x + 30, self.y - 200),
                                            (self.x - 50, self.y - 200),
                                            (self.x - 50, self.y - 185)), 0)
            self.txt_surface = FONT.render(self.text, True, COLOR_ACTIVE)
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            pg.draw.rect(screen, self.color, self.rect, 2)
