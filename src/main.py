from matrix import Matrix
import pygame
from pygame.locals import QUIT, KEYUP
import random

# what number will spawn cell have
SPAWN_CELL_VALUE = 2
CELL_SIZE_X = 200
CELL_SIZE_Y = 200
FONT_SIZE = 100
TEXT_SPACING = 60
CELL_SPACING = 10

BACKGROUND_COLOR = (22, 26, 48)
CELL_COLOR = (124, 255,255)
CELL_OUTLINE_COLOR = (182, 187, 196)
TEXT_COLOR = (240, 236, 229)
CELL_COLOR_LIST = [(238, 228, 218),(237, 224, 200), (242, 177, 121), (245, 149, 99),(246, 124, 95), (246, 94, 59), (237, 207, 114), (237, 204, 97), (237, 200, 80), (237, 197, 63),(237, 194, 46)]

# COLOR_OTHER = Color.BLACK;
# COLOR_GAME_OVER = Color.rgb(238, 228, 218, 0.73);



class Game:
    def __init__(self):
        score = 0
        rows = 4
        columns = 4
        # first we create 4 by 4 matrix
        matrix = Matrix(rows, columns)
        # then we spawn 2 cells
        for i in range(0, 2):
            matrix.spawn_new_cell(2)

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
                elif event.type == KEYUP:
                    if event.key == pygame.K_LEFT and move_ticker < 0:
                        matrix.left()
                        if matrix.spawn_new_cell(2) is False:
                            running = False
                        move_ticker = 10
                    elif event.key == pygame.K_RIGHT and move_ticker < 0:
                        matrix.right()
                        if matrix.spawn_new_cell(2) is False:
                            running = False
                        move_ticker = 10
                    elif event.key == pygame.K_UP and move_ticker < 0:
                        matrix.up()
                        if matrix.spawn_new_cell(2) is False:
                            running = False
                        move_ticker = 10
                    elif event.key == pygame.K_DOWN and move_ticker < 0:
                        matrix.down()
                        if matrix.spawn_new_cell(2) is False:
                            running = False
                        move_ticker = 10

            display.fill(BACKGROUND_COLOR)
            # we render our matrix to thg screen
            self.draw_matrix(matrix.get_matrix(), display)

            move_ticker -= 1
            clock.tick(60)
            pygame.display.update()

        print(f"The game is ended :( you scored {matrix.get_score()}")

    def draw_matrix(self, matrix, display):
        for count_y, y in enumerate(matrix):
            for count_x, x in enumerate(y):
                import math
                if x != 0:
                    CELL_COLOR = CELL_COLOR_LIST[math.ceil(math.sqrt(x))-1]
                
                
                    print(math.floor(math.sqrt(x)))
                
                if x != 0:
                    # draw outline
                    pygame.draw.rect(
                        display,
                        CELL_OUTLINE_COLOR,
                        (
                            count_x * CELL_SIZE_X,
                            count_y * CELL_SIZE_Y,
                            CELL_SIZE_X,
                            CELL_SIZE_Y,
                        ),
                    )

                    # draw cell
                    pygame.draw.rect(
                        display,
                        CELL_COLOR,
                        (
                            count_x * CELL_SIZE_X + CELL_SPACING / 2,
                            count_y * CELL_SIZE_Y + CELL_SPACING / 2,
                            CELL_SIZE_X - CELL_SPACING,
                            CELL_SIZE_Y - CELL_SPACING,
                        ),
                    )
                # draw text if not zero
                if x != 0:
                    font = pygame.font.SysFont("arial", FONT_SIZE)
                    text = font.render(str(x), True, TEXT_COLOR)
                    display.blit(
                        text,
                        [
                            count_x * CELL_SIZE_X + TEXT_SPACING,
                            count_y * CELL_SIZE_Y + TEXT_SPACING,
                        ],
                    )


game = Game()
