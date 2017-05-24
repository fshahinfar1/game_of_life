"""
Farbod Shahinfar
Game Of Life
"""

import pygame
import sys
from random import randrange

pygame.init()

pic_0 = pygame.image.load("resource/image/0.png")
pic_1 = pygame.image.load("resource/image/1.png")

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)


class Board:

    def __init__(self, x: int, y: int):
        """
        zero : empty
        one : filled
        :param x: int
        :param y: int
        """
        self.grid_size = self.grid_width, self.grid_height = 100, 100
        # this is our game board
        self.board = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.position = self.x, self.y = x, y

    def set_randomly(self, r: int):
        if r > self.grid_height*self.grid_width:
            raise Exception("Error you want to set more than what you can")
        # clear board
        self.board = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        for i in range(r):
            while True:
                row = randrange(self.grid_height)
                col = randrange(self.grid_width)
                if self.board[row][col] == 0:
                    self.board[row][col] = 1
                    break

    def draw(self, screen):
        d = 1
        image_size = 5
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                current_cell_state = self.board[row][col]
                cell_x = self.x + col * (image_size + d)
                cell_y = self.y + row * (image_size + d)
                if current_cell_state == 0:
                    pic = pic_0
                elif current_cell_state == 1:
                    pic = pic_1
                screen.blit(pic, (cell_x, cell_y))


def main():
    """
    main function
    :return: None
    """
    size = width, height = 610, 610  # screen size
    clock = pygame.time.Clock()  # type: pygame.time.Clock
    screen = pygame.display.set_mode(size)  # type: pygame.display
    flag_run = True
    board = Board(5, 5)
    board.set_randomly(1000)  # fill 1000 cell randomly

    while flag_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                break

        screen.fill(gray)
        board.draw(screen)
        pygame.display.update()
        clock.tick(30)  # it should keep it 30 fps

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
