import pygame
from pygame.locals import QUIT
import random

# what number will spawn cell have
SPAWN_CELL_VALUE = 2
CELL_SIZE_X = 200
CELL_SIZE_Y = 200
FONT_SIZE = 100

CELL_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)





class Game:
    def __init__(self):
        score = 0
        rows = 4
        columns = 4
        # first we create 4 by 4 matrix
        matrix = Matrix(rows, columns)
        # then we spawn 2 cells
        for i in range(0, 2):
            matrix.spawn_new_cell()

        # initialise pygame and set display to 800 by 800
        pygame.init()
        display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("2048")

        clock = pygame.time.Clock()
        move_ticker = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            # if keys[pygame.K_UP] and move_ticker < 0:
            #     if matrix.spawn_new_cell() is False:
            #         running = False
            #     move_ticker = 10
            if keys[pygame.K_LEFT] and move_ticker < 0:
                matrix.left()
                # matrix.spawn_new_cell()
                matrix.print()
                move_ticker = 30
                print()

            display.fill("black")
            # we render our matrix to thg screen
            self.draw_matrix(matrix.get_matrix(), display)

            move_ticker -= 1
            clock.tick(60)
            pygame.display.update()

        print(f"The game is ended :( you scored {score}")

    def draw_matrix(self, matrix, display):
        for count_y, y in enumerate(matrix):
            for count_x, x in enumerate(y):
                if x != 0:
                    pygame.draw.rect(
                        display,
                        CELL_COLOR,
                        (
                            count_x * CELL_SIZE_X,
                            count_y * CELL_SIZE_Y,
                            CELL_SIZE_X,
                            CELL_SIZE_Y,
                        ),
                    )
                font = pygame.font.SysFont("arial", FONT_SIZE)
                text = font.render(str(x), True, TEXT_COLOR)
                display.blit(
                    text, [count_x * CELL_SIZE_X, count_y * CELL_SIZE_Y])


game = Game()
