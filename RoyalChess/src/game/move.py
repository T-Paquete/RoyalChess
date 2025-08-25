class Move:
    def get_possible_moves(self):
        """
        Returns a list of (row, col) tuples representing possible moves for the piece.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")


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
    
    
class RoyalGuardMove(Move):
    def get_possible_moves(self, piece, board):
        moves = []
        row, col = piece.row, piece.col
        
        # Orthogonal moves (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_row, delta_col in directions:
            new_row = row + delta_row
            new_col = col + delta_col
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                if board.grid[new_row][new_col] is None:
                    moves.append((new_row, new_col))

        # Two squares forward from starting row (like PawnMove logic)
        if piece.color == "white":
            start_row = board.rows - 3
            direction = -1
        else:
            start_row = 2
            direction = 1

        if row == start_row:
            # Forward two squares
            new_row = row + 2 * direction
            mid_row = row + direction
            if (
                0 <= new_row < board.rows
                and board.grid[mid_row][col] is None
                and board.grid[new_row][col] is None
            ):
                moves.append((new_row, col))
            
        # Diagonal captures only in the forward direction
        forward = -1 if piece.color == "white" else 1
        for delta_col in [-1, 1]:
            new_row = row + forward
            new_col = col + delta_col
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                target = board.grid[new_row][new_col]
                if target is not None and target.color != piece.color:
                    moves.append((new_row, new_col))
                    
        return moves


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
                    elif target.color != piece.color or piece.can_combine(target):
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
                        if target.color != piece.color or piece.can_combine(target):
                            moves.append((new_row, new_col))
                        break
                else:
                    break
        return moves


class JumpOverStraightMove(Move):
    def get_possible_moves(self, piece, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        moves = []
        for dir_row, dir_col in directions:
            adj_row = piece.row + dir_row
            adj_col = piece.col + dir_col
            land_row = piece.row + 2 * dir_row
            land_col = piece.col + 2 * dir_col
            if (
                0 <= adj_row < board.rows and 0 <= adj_col < board.cols and
                board.grid[adj_row][adj_col] is not None and
                0 <= land_row < board.rows and 0 <= land_col < board.cols
            ):
                target = board.grid[land_row][land_col]
                # Can move if landing square is empty
                if target is None:
                    moves.append((land_row, land_col))
                # Or can capture if landing square has opponent's piece
                elif target.color != piece.color:
                    moves.append((land_row, land_col))
        return moves

class JumpOverDiagonalMove(Move):
    def get_possible_moves(self, piece, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions
        moves = []
        for dir_row, dir_col in directions:
            adj_row = piece.row + dir_row
            adj_col = piece.col + dir_col
            land_row = piece.row + 2 * dir_row
            land_col = piece.col + 2 * dir_col
            if (
                0 <= adj_row < board.rows and 0 <= adj_col < board.cols and
                board.grid[adj_row][adj_col] is not None and
                0 <= land_row < board.rows and 0 <= land_col < board.cols
            ):
                target = board.grid[land_row][land_col]
                # Can move if landing square is empty
                if target is None:
                    moves.append((land_row, land_col))
                # Or can capture if landing square has opponent's piece
                elif target.color != piece.color:
                    moves.append((land_row, land_col))
        return moves
        
    
class SwapMove(Move):
    def get_possible_moves(self, piece, board):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),      # straight
            (-1, -1), (-1, 1), (1, -1), (1, 1)     # diagonal
        ]
        moves = []
        for dir_row, dir_col in directions:
            adj_row = piece.row + dir_row
            adj_col = piece.col + dir_col
            if (
                0 <= adj_row < board.rows and 0 <= adj_col < board.cols and
                board.grid[adj_row][adj_col] is not None and
                board.grid[adj_row][adj_col].color == piece.color
            ):
                target_piece = board.grid[adj_row][adj_col]
                if type(target_piece).__name__ not in ("Lion", "Dragon"):
                    moves.append((adj_row, adj_col))
        return moves
    
    def execute_swap(self, piece, board, target_row, target_col):
        target_piece = board.grid[target_row][target_col]
        if target_piece is not None and target_piece.color != piece.color:
            return # Invalid swap

        # Prevent swapping with Lion or Dragon
        if target_piece is not None and type(target_piece).__name__ in ("Lion", "Dragon"):
            return # Cannot swap with Lion or Dragon
        
        # Swap the pieces
        board.grid[piece.row][piece.col], board.grid[target_row][target_col] = target_piece, piece
        # Update their positions
        piece.row, piece.col, target_piece.row, target_piece.col = target_row, target_col, piece.row, piece.col


class CombinedMove(Move):
    def __init__(self, piece_classes):
        self.piece_classes = piece_classes
        
    def get_possible_moves(self, piece, board):
        combined_moves = set()
        for cls in self.piece_classes:
            # Create a temporary instanve of the class at the current position
            temp_piece = cls(piece.color, piece.row, piece.col)
            for move in temp_piece.moves:
                combined_moves.update(move.get_possible_moves(temp_piece, board))
        return list(combined_moves)
    
    def get_moves_by_type(self, move_type):
        moves = []
        for cls in self.piece_classes:
            temp_piece = cls("color", 0, 0)
            for move in temp_piece.moves:
                if isinstance(move, move_type):
                    moves.append(move)
        return moves
    

class NonCapturingQueenMove(Move):
    def get_possible_moves(self, piece, board):
        moves = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # straight
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonal
        ]
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
                        break # Stop at the first piece encountered
                else:
                    break # Out of bounds
        return moves

class NonCapturingHatMove(Move):
    def get_possible_moves(self, piece, board):
        moves = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # straight
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonal
        ]
        max_steps = piece.max_steps if piece.max_steps is not None else max(board.rows, board.cols)
        for dir_row, dir_col in directions:
            for step in range(1, max_steps + 1):
                new_row = piece.row + dir_row * step
                new_col = piece.col + dir_col * step
                if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                    target = board.grid[new_row][new_col]
                    # Allow moving to an empty square
                    if target is None:
                        moves.append((new_row, new_col))
                    # Allow moving onto the other hat
                    elif (
                        (piece.name == "white_hat" and target.name == "black_hat") or
                        (piece.name == "black_hat" and target.name == "white_hat")
                    ):
                        moves.append((new_row, new_col))
                        break # Stop at the first piece encountered
                    else:
                        break # Stop at the first piece encountered
                else:
                    break # Out of bounds
        return moves

class EnPassantMove(Move):
    def get_possible_moves(self, piece, board):
        """
        Returns en-passant capture square if the last move was an opponent pawn/royal_guard
        that moved two squares and ended adjacent to this piece.
        """
        possible_moves = []

        # Need a previous move
        last_index = board.move_history.current_index
        if last_index < 0:
            return possible_moves

        last_move = board.move_history.moves[last_index]
        last_moved_piece = last_move.get('piece')
        if last_moved_piece is None:
            return possible_moves

        # Only pawns / royal guards can be captured en passant
        if last_moved_piece.name not in ("pawn", "royal_guard"):
            return possible_moves

        # Last move must have been a two-square advance
        last_start_row, last_start_col = last_move['start_pos']
        last_end_row, last_end_col = last_move['end_pos']
        if abs(last_start_row - last_end_row) != 2:
            return possible_moves

        # The moved piece must be on the same row as this piece and adjacent column
        if last_end_row != piece.row:
            return possible_moves
        if abs(last_end_col - piece.col) != 1:
            return possible_moves

        # Landing square for en-passant is one forward from the capturer
        forward = -1 if piece.color == "white" else 1
        landing_row = piece.row + forward
        landing_col = last_end_col

        # Must be on board and landing square must be empty
        if 0 <= landing_row < board.rows and 0 <= landing_col < board.cols:
            if board.grid[landing_row][landing_col] is None:
                possible_moves.append((landing_row, landing_col))

        return possible_moves


