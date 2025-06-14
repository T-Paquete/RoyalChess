import pygame
from game.constants import ROWS, COLS, WHITE, LIGHT_COLOR, DARK_COLOR, SQSIZE
from game.piece import Piece

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.initial_piece_setup()

    @property
    def rows(self):
        return len(self.grid) 

    @property
    def cols(self):
        return len(self.grid[0]) if self.grid else 0

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or row == 9:
                    color = WHITE
                else:
                    color = DARK_COLOR if (row + col) % 2 == 0 else LIGHT_COLOR
                rect = col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE
                pygame.draw.rect(screen, color, rect)

    def initial_piece_setup(self):
        # Place Pawns for white (rows 7, cols 0-3 and 8-11)
        for col in list(range(0, 4)) + list(range(8, 12)):
            self.grid[7][col] = Piece("pawn", "white", 7, col)
        # Place Pawns for black (rows 2, cols 0-3 and 8-11)
        for col in list(range(0, 4)) + list(range(8, 12)):
            self.grid[2][col] = Piece("pawn", "black", 2, col)

        # Place Royal Guards for white (row 7, cols 4-7)
        for col in range(4, 8):
            self.grid[7][col] = Piece("royal_guard", "white", 7, col)
        # Place Royal Guards for black (row 2, cols 4-7)
        for col in range(4, 8):
            self.grid[2][col] = Piece("royal_guard", "black", 2, col)
        
        # Place Rooks for white (row 8, cols 0 and 11)
        self.grid[8][0] = Piece("rook", "white", 8, 0)
        self.grid[8][11] = Piece("rook", "white", 8, 11)
        # Place Rooks for black (row 1, cols 0 and 11)
        self.grid[1][0] = Piece("rook", "black", 1, 0)
        self.grid[1][11] = Piece("rook", "black", 1, 11)
        
        # Place Knights for white (row 7, cols 1 and 10)
        self.grid[8][1] = Piece("knight", "white", 7, 1)
        self.grid[8][10] = Piece("knight", "white", 7, 10)
        # Place Knights for black (row 2, cols 1 and 10)
        self.grid[1][1] = Piece("knight", "black", 2, 1)
        self.grid[1][10] = Piece("knight", "black", 2, 10)
        
        #Place Dragons for white (row 8, col 2)
        self.grid[8][2] = Piece("dragon", "white", 8, 2)
        #Place Dragons for black (row 1, col 2)
        self.grid[1][2] = Piece("dragon", "black", 1, 2)
        
        #Place Wizard for white (row 8, col 3)
        self.grid[8][3] = Piece("wizard", "white", 8, 3)
        #Place Wizard for black (row 1, col 3)
        self.grid[1][3] = Piece("wizard", "black", 1, 3)
        
        # Place Lion for white (row 8, col 9)
        self.grid[8][9] = Piece("lion", "white", 8, 9)
        # Place Lion for black (row 1, col 9)
        self.grid[1][9] = Piece("lion", "black", 1, 9)
        
        # Place Prince for white (row 8, col 8)
        self.grid[8][8] = Piece("prince", "white", 8, 8)
        # Place Prince for black (row 1, col 8)
        self.grid[1][8] = Piece("prince", "black", 1, 8)
        
        # Place Councelors for white (row 8, cols 4 and 7)
        self.grid[8][4] = Piece("counselor", "white", 8, 4)
        self.grid[8][7] = Piece("counselor", "white", 8, 7)
        # Place Counselors for black (row 1, cols 4 and 7)
        self.grid[1][4] = Piece("counselor", "black", 1, 4)
        self.grid[1][7] = Piece("counselor", "black", 1, 7)
        
        # Place King for white (row 8, col 6)
        self.grid[8][6] = Piece("king", "white", 8, 6)
        # Place King for black (row 1, col 6)
        self.grid[1][6] = Piece("king", "black", 1, 6)
        
        # Place Queen for white (row 8, col 5)
        self.grid[8][5] = Piece("queen", "white", 8, 5)
        # Place Queen for black (row 1, col 5)
        self.grid[1][5] = Piece("queen", "black", 1, 5)
        
        # Place Symbols for white (row 9, cols 5-6)
        self.grid[9][5] = Piece("symbol", "white", 9, 5)
        self.grid[9][6] = Piece("symbol", "white", 9, 6)
        # Place Symbols for black (row 0, cols 5-6)
        self.grid[0][5] = Piece("symbol", "black", 0, 5)
        self.grid[0][6] = Piece("symbol", "black", 0, 6)

        # Place White Hat for white (row 9, col 4)
        self.grid[9][4] = Piece("white_hat", "white", 9, 4)
        # Place White Hat for black (row 0, col 4)
        self.grid[0][4] = Piece("white_hat", "black", 0, 4)
        
        # Place Black Hat for white (row 9, col 7)
        self.grid[9][7] = Piece("black_hat", "white", 9, 7)
        # Place Black Hat for black (row 0, col 7)
        self.grid[0][7] = Piece("black_hat", "black", 0, 7)





