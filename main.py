from checkers.consts import *
from checkers.board import Board

FPS = 60

WIN = p.display.set_mode((WIDTH, HEIGHT))

p.display.set_caption("Python Checkers")


def main():
    run = True
    clock = p.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

            if event.type == p.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        p.display.update()

    p.quit()


main()
