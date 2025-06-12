import pygame
from .constants import COLS, ROWS, SQSIZE, LIGHT_COLOR, DARK_COLOR, WHITE

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        