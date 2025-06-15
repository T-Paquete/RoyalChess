class Move:
    def get_possible_moves(self, piece, board):
        """
        Returns a list of (row, col) tuples representing possible moves for the piece.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

class StraightMove(Move):
    def __init__(self, max_steps=None):
        self.max_steps = max_steps  # None means unlimited

    def get_possible_moves(self, piece, board):
        directions = [(-1,0), (1,0), (0,-1), (0,1)] # Moves: up, down, left, right
        moves = []
        for dir_row, dir_col in directions:
            for step in range(1, self.max_steps+1 if self.max_steps else max(board.rows, board.cols)):
                new_row = piece.row + dir_row * step
                new_col = piece.col + dir_col * step
                if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                    if board.grid[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    else:
                        if board.grid[new_row][new_col].color != piece.color:
                            moves.append((new_row, new_col))
                        break
                else:
                    break
        return moves

class DiagonalMove(Move):
    def __init__(self, max_steps=None):
        self.max_steps = max_steps  # None means unlimited

    def get_possible_moves(self, piece, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # Moves: up-left, up-right, down-left, down-right
        moves = []
        for dir_row, dir_col in directions:
            for step in range(1, self.max_steps+1 if self.max_steps else max(board.rows, board.cols)):
                new_row = piece.row + dir_row * step
                new_col = piece.col + dir_col * step
                if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                    if board.grid[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    else:
                        if board.grid[new_row][new_col].color != piece.color:
                            moves.append((new_row, new_col))
                        break
                else:
                    break
        return moves

class KnightMove(Move):
    def get_possible_moves(self, piece, board):
        # All possible L-shaped moves for a knight
        deltas = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        moves = []
        for dir_row, dir_col in deltas:
            new_row = piece.row + dir_row
            new_col = piece.col + dir_col
            print(f"Checking: ({new_row}, {new_col})")
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                target = board.grid[new_row][new_col]
                if target is None or target.color != piece.color:
                    moves.append((new_row, new_col))
        print(f"Knight possible moves: {moves}") # <-- Debug print
        return moves


class PawnMove(Move):
    def get_possible_moves(self, piece, board):
        # Use piece.direction if set, otherwise default: -1 for white, +1 for black
        direction = piece.direction if piece.direction is not None else (-1 if piece.color == "white" else 1)
        moves = []
        row, col = piece.row, piece.col
        next_row = row + direction

        # Forward move (one square)
        if 0 <= next_row < board.rows and board.grid[next_row][col] is None:
            moves.append((next_row, col))

        # Diagonal captures
        for dir_col in [-1, 1]:
            diag_col = col + dir_col
            if 0 <= next_row < board.rows and 0 <= diag_col < board.cols:
                target = board.grid[next_row][diag_col]
                if target is not None and target.color != piece.color:
                    moves.append((next_row, diag_col))
        return moves
    
class JumpOverMove(Move):
    def get_possible_moves(self, piece, board):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),      # straight
            (-1, -1), (-1, 1), (1, -1), (1, 1)     # diagonal
        ]
        moves = []
        for dir_row, dir_col in directions:
            adj_row = piece.row + dir_row
            adj_col = piece.col + dir_col
            land_row = piece.row + 2 * dir_row
            land_col = piece.col + 2 * dir_col
            # Check if adjacent square is on board and has a piece
            if (
                0 <= adj_row < board.rows and 0 <= adj_col < board.cols and
                board.grid[adj_row][adj_col] is not None and
                0 <= land_row < board.rows and 0 <= land_col < board.cols and
                board.grid[land_row][land_col] is None
            ):
                moves.append((land_row, land_col))
        return moves

class SwapMove(Move):
    def get_possible_moves(self, piece, board):
        # Directions: straight and diagonal
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),      # straight
            (-1, -1), (-1, 1), (1, -1), (1, 1)     # diagonal
        ]
        moves = []
        for dir_row, dir_col in directions:
            adj_row = piece.row + dir_row
            adj_col = piece.col + dir_col
            # Check if adjacent square is on board and has a piece
            if (
                0 <= adj_row < board.rows and 0 <= adj_col < board.cols and
                board.grid[adj_row][adj_col] is not None
            ):
                # The move is to swap with the adjacent piece
                moves.append((adj_row, adj_col))
        return moves

    def execute_swap(self, piece, board, target_row, target_col):
        # Swap the positions of the piece and the target piece
        target_piece = board.grid[target_row][target_col]
        board.grid[piece.row][piece.col], board.grid[target_row][target_col] = target_piece, piece
        piece.row, piece.col, target_piece.row, target_piece.col = target_row, target_col, piece.row, piece.col



