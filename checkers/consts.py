import pygame as p

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQSIZE = WIDTH // COLS

RED = (119, 154, 88)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = p.transform.scale(p.image.load("assets/crown.png"), (45, 25))
