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
        # Example: rook/queen straight lines 
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


