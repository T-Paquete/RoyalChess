from game.constants import ROWS, COLS
from game.piece import (
    Pawn, RoyalGuard, Knight, Counselor, Rook, Wizard, Prince, Dragon, Lion, King, Queen,
    Symbol, WhiteHat, BlackHat
)
from history.move_history import MoveHistory

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.move_history = MoveHistory()
        self.initial_piece_setup()

    @property
    def rows(self):
        return len(self.grid)

    @property
    def cols(self):
        return len(self.grid[0]) if self.grid else 0


# -------------------------------------------


    def initial_piece_setup(self):
        # Pawns
        for col in list(range(0, 4)) + list(range(8, 12)):
            self.grid[7][col] = Pawn("white", 7, col)
            self.grid[2][col] = Pawn("black", 2, col)

        # Royal Guards
        for col in range(4, 8):
            self.grid[7][col] = RoyalGuard("white", 7, col)
            self.grid[2][col] = RoyalGuard("black", 2, col)

        # Rooks
        self.grid[8][0] = Rook("white", 8, 0)
        self.grid[8][11] = Rook("white", 8, 11)
        self.grid[1][0] = Rook("black", 1, 0)
        self.grid[1][11] = Rook("black", 1, 11)

        # Knights
        self.grid[8][1] = Knight("white", 8, 1)
        self.grid[8][10] = Knight("white", 8, 10)
        self.grid[1][1] = Knight("black", 1, 1)
        self.grid[1][10] = Knight("black", 1, 10)

        # Dragons
        self.grid[8][2] = Dragon("white", 8, 2)
        self.grid[1][2] = Dragon("black", 1, 2)

        # Wizards
        self.grid[8][3] = Wizard("white", 8, 3)
        self.grid[1][3] = Wizard("black", 1, 3)

        # Lions
        self.grid[8][9] = Lion("white", 8, 9)
        self.grid[1][9] = Lion("black", 1, 9)

        # Princes
        self.grid[8][8] = Prince("white", 8, 8)
        self.grid[1][8] = Prince("black", 1, 8)

        # Counselors
        self.grid[8][4] = Counselor("white", 8, 4)
        self.grid[8][7] = Counselor("white", 8, 7)
        self.grid[1][4] = Counselor("black", 1, 4)
        self.grid[1][7] = Counselor("black", 1, 7)

        # Kings
        self.grid[8][6] = King("white", 8, 6)
        self.grid[1][6] = King("black", 1, 6)

        # Queens
        self.grid[8][5] = Queen("white", 8, 5)
        self.grid[1][5] = Queen("black", 1, 5)

        # Symbols
        self.grid[9][5] = Symbol("white", 9, 5)
        self.grid[9][6] = Symbol("white", 9, 6)
        self.grid[0][5] = Symbol("black", 0, 5)
        self.grid[0][6] = Symbol("black", 0, 6)

        # White Hats
        self.grid[9][4] = WhiteHat("white", 9, 4)
        self.grid[0][4] = WhiteHat("black", 0, 4)

        # Black Hats
        self.grid[9][7] = BlackHat("white", 9, 7)
        self.grid[0][7] = BlackHat("black", 0, 7)
        
        
# -------------------------------------------


    def move_piece(self, start_row, start_col, end_row, end_col):
        """
        Moves a piece from (start_row, start_col) to (end_row, end_col) and records it in move_history.
        """
        piece = self.grid[start_row][start_col]
        captured = self.grid[end_row][end_col]
        self.grid[end_row][end_col] = piece
        self.grid[start_row][start_col] = None # Clear the starting position
        piece.row, piece.col = end_row, end_col
        if not piece:
            return
        
        # Create a dictionary to record the move
        move_record = {
            'piece': piece,
            'start_pos': (start_row, start_col),
            'end_pos': (end_row, end_col),
            'captured': captured
        }
        
        # Log the move in MoveHistory
        self.move_history.add_move(move_record)






