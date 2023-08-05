from .consts import *


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQSIZE * self.col + SQSIZE // 2
        self.y = SQSIZE * self.row + SQSIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQSIZE // 2 - self.PADDING
        p.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        p.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.color)
