from checkers.consts import *
from checkers.game import Game

FPS = 60

WIN = p.display.set_mode((WIDTH, HEIGHT))

p.display.set_caption("Python Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQSIZE
    col = x // SQSIZE
    return row, col


def main():
    run = True
    clock = p.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    p.quit()


main()
