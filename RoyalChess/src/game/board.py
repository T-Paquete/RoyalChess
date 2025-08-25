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
        piece = self.grid[start_row][start_col]
        if piece is None:
            return

        # Normal captured piece at destination (may be None)
        captured_piece = self.grid[end_row][end_col]

        # Detect en-passant: diagonal move into an empty square by pawn or royal_guard
        is_en_passant = False
        en_passant_captured_position = None

        if captured_piece is None and start_col != end_col and piece.name in ("pawn", "royal_guard"):
            # Candidate captured piece is on same row as mover and in the column we move into
            candidate_row = start_row
            candidate_col = end_col
            candidate_piece = self.grid[candidate_row][candidate_col]

            # Validate candidate and that it was the last move with a two-square advance
            if candidate_piece is not None and candidate_piece.color != piece.color and candidate_piece.name in ("pawn", "royal_guard"):
                last_index = self.move_history.current_index
                if last_index >= 0:
                    last_move = self.move_history.moves[last_index]
                    if last_move.get('piece') is candidate_piece:
                        last_start_row, _ = last_move['start_pos']
                        last_end_row, _ = last_move['end_pos']
                        if abs(last_start_row - last_end_row) == 2:
                            # Valid en-passant
                            is_en_passant = True
                            en_passant_captured_position = (candidate_row, candidate_col)
                            captured_piece = candidate_piece

        # Move the piece
        self.grid[end_row][end_col] = piece
        self.grid[start_row][start_col] = None
        piece.row, piece.col = end_row, end_col

        # If en-passant, remove the captured pawn from its square
        if is_en_passant and en_passant_captured_position is not None:
            cap_row, cap_col = en_passant_captured_position
            self.grid[cap_row][cap_col] = None

        # Record move (include en-passant metadata)
        move_record = {
            'piece': piece,
            'start_pos': (start_row, start_col),
            'end_pos': (end_row, end_col),
            'captured': captured_piece,
            'en_passant': is_en_passant,
            'en_passant_captured_pos': en_passant_captured_position
        }

        self.move_history.add_move(move_record)

    def reset(self):
        """Reset board to initial state and clear move history."""
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.move_history = MoveHistory()
        self.initial_piece_setup()

    def swap_positions(self, row_a, col_a, row_b, col_b):
        """
        Swap two board squares (used for custom setup rearranging).
        Updates piece.row/piece.col for moved pieces. Does not record a move in history.
        """
        if not (0 <= row_a < self.rows and 0 <= col_a < self.cols):
            return
        if not (0 <= row_b < self.rows and 0 <= col_b < self.cols):
            return
        piece_a = self.grid[row_a][col_a]
        piece_b = self.grid[row_b][col_b]
        # swap on grid
        self.grid[row_a][col_a], self.grid[row_b][col_b] = piece_b, piece_a
        # update piece coords if pieces exist
        if piece_a:
            piece_a.row, piece_a.col = row_b, col_b
        if piece_b:
            piece_b.row, piece_b.col = row_a, col_a

    def undo_last_move(self):
        """
        Undo the last move recorded in move_history and restore board state.
        Returns True if a move was undone, False otherwise.
        """
        last_move = self.move_history.undo()
        if not last_move:
            return False

        moved_piece = last_move.get('piece')
        start_row, start_col = last_move.get('start_pos')
        end_row, end_col = last_move.get('end_pos')
        captured_piece = last_move.get('captured')
        was_en_passant = last_move.get('en_passant', False)
        en_passant_captured_pos = last_move.get('en_passant_captured_pos')

        # Move the piece back to its start square
        # Clear the end square (was occupied by moved_piece)
        # If other piece is now on start square (unlikely), overwrite
        self.grid[start_row][start_col] = moved_piece
        if 0 <= end_row < self.rows and 0 <= end_col < self.cols:
            self.grid[end_row][end_col] = None
        if moved_piece:
            moved_piece.row, moved_piece.col = start_row, start_col

        # Restore captured piece
        if was_en_passant and en_passant_captured_pos:
            cap_row, cap_col = en_passant_captured_pos
            self.grid[cap_row][cap_col] = captured_piece
            if captured_piece:
                captured_piece.row, captured_piece.col = cap_row, cap_col
        else:
            if captured_piece:
                # captured piece originally was on the end square
                self.grid[end_row][end_col] = captured_piece
                if captured_piece:
                    captured_piece.row, captured_piece.col = end_row, end_col

        return True






