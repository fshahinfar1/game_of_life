"""
Farbod Shahinfar
Game Of Life
"""

import pygame
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from random import randrange
from copy import deepcopy
from time import sleep

pygame.init()

pic_0 = pygame.image.load("resource/image/0.png")
pic_1 = pygame.image.load("resource/image/1.png")

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
flag_run = True


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

    def get_adjacent(self, row, col):
        adjacent = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                tmp_row = row + i
                tmp_col = col + j
                if tmp_row >= 0 and tmp_col >= 0 and tmp_row < self.grid_height \
                        and tmp_col < self.grid_width and not (i == j == 0):
                    adjacent.append(self.board[tmp_row][tmp_col])
        return tuple(adjacent)

    def tick(self):
        tmp_board = deepcopy(self.board)
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                adjacent = self.get_adjacent(row, col)
                alive_adj = adjacent.count(1)
                if alive_adj < 2 and self.board[row][col] == 1:
                    tmp_board[row][col] = 0  # dies
                elif alive_adj > 3 and self.board[row][col] == 1:
                    tmp_board[row][col] = 0  # dies
                elif alive_adj == 3 and self.board[row][col] == 0:
                    tmp_board[row][col] = 1  # reproduce
        self.board = tmp_board

    def set_randomly(self, r: int):
        if r > self.grid_height * self.grid_width:
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


def main(r):
    """
    main function
    :return: None
    """
    size = width, height = 610, 610  # screen size
    clock = pygame.time.Clock()  # type: pygame.time.Clock
    screen = pygame.display.set_mode(size)  # type: pygame.display
    board = Board(5, 5)
    board.set_randomly(r)  # fill cell randomly
    # board.board[50][50] = 1
    # board.board[50][51] = 1
    # board.board[50][52] = 1
    # board.board[50][53] = 1
    # board.board[50][54] = 1
    # board.board[50][55] = 1
    # board.board[50][56] = 1
    #
    global flag_run
    while flag_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                break

        screen.fill(gray)
        board.draw(screen)
        pygame.display.update()
        clock.tick(30)  # it should keep it 30 fps

        board.tick()

        # sleep(1)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # thread_pool = ThreadPoolExecutor(max_workers=1)
    r = int(input("please enter initial value for the game: "))
    # thread_pool.map()
    game_thread = threading.Thread(target=main, args=(r,))
    game_thread.start()
    while True:
        command = input("quit/new? (q/n): ")  # type: str
        if command[0].lower() == 'q':
            flag_run = False
            sys.exit(0)
        elif command[0].lower() == 'n':
            r = int(input("please enter initial value for the game: "))
            flag_run = False
            sleep(1)
            flag_run = True
            game_thread = threading.Thread(target=main, args=(r,))
            game_thread.start()
