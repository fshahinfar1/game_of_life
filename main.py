"""
Farbod Shahinfar
Game Of Life
"""

import pygame, sys

pygame.init()

board = [[0 for col in range(grid_width)] for row in range(grid_height)]  # this is our game board


def main():
    """
    main function
    :return: None
    """
    size = width, height = 300, 300  # screen size
    clock = pygame.time.Clock()  # type: pygame.time.Clock
    screen = pygame.display.set_mode(size)
    flag_run = True

    black = (0, 0, 0)
    white = (255, 255, 255)

    grid_size = grid_width, grid_height = 100, 100

    while flag_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                break

        screen.fill(white)
        screen.update()
        clock.tick(30)  # it should keep it 30 fps

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
