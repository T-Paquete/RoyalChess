class Move:
    def get_possible_moves(self, piece, board):
        """
        Returns a list of (row, col) tuples representing possible moves for the piece.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

class StraightMove(Move):
    def get_possible_moves(self, piece, board):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        max_steps = piece.max_steps if piece.max_steps is not None else max(len(board.grid), len(board.grid[0]))

        for direction_row, direction_col in directions:
            for step in range(1, max_steps + 1):
                new_row = piece.row + direction_row * step
                new_col = piece.col + direction_col * step
                if 0 <= new_row < len(board.grid) and 0 <= new_col < len(board.grid[0]):
                    target = board.grid[new_row][new_col]
                    if target is None:
                        moves.append((new_row, new_col))
                    elif target.color != piece.color:
                        moves.append((new_row, new_col))
                        break  # Can't move past capture
                    else:
                        break  # Blocked by own piece
                else:
                    break  # Out of bounds
        return moves

class DiagonalMove(Move):
    def get_possible_moves(self, piece, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        moves = []
        max_steps = piece.max_steps if piece.max_steps is not None else max(board.rows, board.cols)
        for dir_row, dir_col in directions:
            for step in range(1, max_steps + 1):
                new_row = piece.row + dir_row * step
                new_col = piece.col + dir_col * step
                if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                    target = board.grid[new_row][new_col]
                    if target is None:
                        moves.append((new_row, new_col))
                    else:
                        if target.color != piece.color:
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
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                target = board.grid[new_row][new_col]
                if target is None or target.color != piece.color:
                    moves.append((new_row, new_col))
        return moves


class PawnMove(Move):
    def get_possible_moves(self, piece, board):
        moves = []
        direction = -1 if piece.color == "white" else 1  # White moves up, black moves down
        # Set correct starting row for each color (white at bottom, black at top)
        start_row = board.rows - 3 if piece.color == "white" else 2

        # One square forward
        new_row = piece.row + direction
        if 0 <= new_row < board.rows and board.grid[new_row][piece.col] is None:
            moves.append((new_row, piece.col))

            # Two squares forward from starting row
            if piece.row == start_row:
                new_row2 = piece.row + 2 * direction
                if 0 <= new_row2 < board.rows and board.grid[new_row2][piece.col] is None:
                    moves.append((new_row2, piece.col))
                    
         # Diagonal captures
        for delta_col in [-1, 1]:
            capture_col = piece.col + delta_col
            if 0 <= new_row < len(board.grid) and 0 <= capture_col < len(board.grid[0]):
                target = board.grid[new_row][capture_col]
                if target is not None and target.color != piece.color:
                    moves.append((new_row, capture_col))
            
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



