import pygame as pg

LIST_DICTIONARY = ["kitchen", "fireman", "house", "restaurant", "hotel",
                   "heaven", "beach", "sports", "games", "competition",
                   "recovery", "nutrition", "health", "meditation", "mind",
                   "movement", "passion", "high", "performance", "cocina",
                   "bombero", "casa", "negocio", "cielo", "playa", "deportes",
                   "juegos", "competencia", "recuperación", "nutrición", "salud",
                   "meditación", "mente", "movimiento", "pasión", "alto",
                   "rendimiento"]

pg.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
SCREEN = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
COLOR_INACTIVE = pg.Color('gold')
COLOR_ACTIVE = pg.Color('brown1')
FONT = pg.font.Font('century_gothic.ttf', 32)
PURPLE = (110, 0, 160)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE4 = pg.Color('blue4')

COLOR_LINES = pg.Color('darkblue')

