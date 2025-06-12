
from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        # Each col has a list of 10 zeros (8 + 2 as defined in the const file)
        # The zeros will become the square objects
        # This creates a 2 dimension array
        # create a 10 x 12 grid of zeros
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # Create the board
        self._create()
        # Add pieces to the board
        self._add_pieces("white")
        self._add_pieces("black")




    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                # Creates a board full of square objects
                # Populates the 2 dimention array with objects (instead of zeros)
                self.squares[row][col] = Square(row, col)


    def _add_pieces(self, color):
        row_pawn, row_other = (7, 8) if color == "white" else (2, 1)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        # Royal Guards

        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][10] = Square(row_other, 10, Knight(color))

        # Counselors
        self.squares[row_other][4] = Square(row_other, 4, Counselor(color))
        self.squares[row_other][7] = Square(row_other, 7, Counselor(color))

         # Rook
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][11] = Square(row_other, 11, Rook(color))

        # King
        self.squares[row_other][6] = Square(row_other, 6, King(color))

        # Queen
        self.squares[row_other][5] = Square(row_other, 5, Queen(color))

        # Prince
        self.squares[row_other][8] = Square(row_other, 8, Prince(color))

        # Wizard
        self.squares[row_other][3] = Square(row_other, 3, Wizard(color))

        # Dragon
        self.squares[row_other][2] = Square(row_other, 2, Dragon(color))

        # Lion
        self.squares[row_other][9] = Square(row_other, 9, Lion(color))
