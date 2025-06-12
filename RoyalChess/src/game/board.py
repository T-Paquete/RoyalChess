import pygame
from game.constants import ROWS, COLS, WHITE, LIGHT_COLOR, DARK_COLOR, SQSIZE

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or row == 9:
                    color = WHITE
                else:
                    color = DARK_COLOR if (row + col) % 2 == 0 else LIGHT_COLOR
                rect = col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE
                pygame.draw.rect(screen, color, rect)

