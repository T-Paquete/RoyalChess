from game.move import SwapMove, CombinedMove

class GameManager:
    def __init__(self, board):
        self.board = board

    def make_move(self, piece, target_row, target_col):
        """
        Executes a move for the given piece to the specified target position on the board.
        This method first gathers all possible moves for the piece. If the target position
        is not a valid move, the method returns without making any changes. If the move is valid,
        it checks for special move types:
          - Mounting: If the move is a mounting action (as determined by `is_mounting`), the piece
            is mounted onto the target piece, and its original position is cleared.
          - Dismounting: If the move is a dismounting action (as determined by `is_dismounting`),
            the piece is dismounted.
          - Standard Move: Otherwise, the piece is moved to the target position using the board's
            `move_piece` method.
        Args:
            piece: The piece to move.
            target_row (int): The row index of the target position.
            target_col (int): The column index of the target position.
        Returns:
            None
        """
        possible_moves = []
        swap_move = None
        for move in piece.moves:
            if isinstance(move, SwapMove) and (target_row, target_col) in move.get_possible_moves(piece, self.board):
                swap_move = move
            elif isinstance(move, CombinedMove):
                # Look for SwapMove inside CombinedMove
                for sub_move in move.get_moves_by_type(SwapMove):
                    if (target_row, target_col) in sub_move.get_possible_moves(piece, self.board):
                        swap_move = sub_move
            possible_moves.extend(move.get_possible_moves(piece, self.board))
        if (target_row, target_col) not in possible_moves:
            return # Invalid move

        target_piece = self.board.grid[target_row][target_col]

        # Hat combining logic
        if self.is_combining_hats(piece, target_piece):
            self.combine_hats(piece, target_piece)
            self.board.grid[piece.row][piece.col] = None
            return

        # Mounting logic (for wizard/dragon, prince/lion)
        if self.is_mounting(piece, target_piece):
            self.mount(piece, target_piece)
            self.board.grid[piece.row][piece.col] = None
            return

        # Dismounting logic
        if self.is_dismounting(piece):
            self.dismount(piece)
            return

        # Swap logic
        if swap_move is not None:
            self.swap(piece, swap_move, target_row, target_col)
            return  # <-- This prevents a capture after swap

        # Standard move
        self.board.move_piece(piece.row, piece.col, target_row, target_col)
        
        
# ---------------------------------------------
# Mount and Dismount Wizard and Prince
# ---------------------------------------------

    def is_mounting(self, piece, target_piece):
        """
        Determines if a given piece is mounting another piece according to specific rules.
        A piece is considered to be mounting another piece if:
          - The piece is a Wizard and the target_piece is a Dragon of the same color.
          - The piece is a Prince and the target_piece is a Lion of the same color.
        Args:
            piece: The chess piece attempting to mount another piece.
            target_piece: The chess piece being mounted.
        Returns:
            bool: True if the mounting condition is met, False otherwise.
        """
        from game.piece import Wizard, Prince
        # Wizard mounting Dragon
        if (
            isinstance(piece, Wizard)
            and target_piece is not None
            and target_piece.name == "dragon"
            and target_piece.color == piece.color
        ):
            return True
        
        # Prince mounting Lion
        if (
            isinstance(piece, Prince)
            and target_piece is not None
            and target_piece.name == "lion"
            and target_piece.color == piece.color
        ):
            return True
        return False
    
    
    def mount(self, piece, target_piece):
        """
        Allows a piece to mount another piece if it has the appropriate ability.

        If the piece is a Wizard, it attempts to mount a dragon using its special ability.
        If the piece is a Prince, it attempts to mount a lion using its special ability.

        Args:
            piece: The piece attempting to mount another piece (expected to be a Wizard or Prince).
            target_piece: The piece to be mounted (e.g., a dragon or lion).

        Raises:
            AttributeError: If the piece does not have the required ability.
        """
        from game.piece import Wizard, Prince
        if isinstance(piece, Wizard):
            piece.use_ability("mount_dragon", self.board, target_piece)
        elif isinstance(piece, Prince):
            piece.use_ability("mount_lion", self.board, target_piece)
            
            
    def is_dismounting(self, piece):
        """
        Checks if the given piece is currently mounted.

        Args:
            piece: The chess piece object to check.

        Returns:
            bool: True if the piece has the attribute 'is_mounted' set to True, False otherwise.
        """
        return getattr(piece, "is_mounted", False)
    
    
    def dismount(self, piece):
        """
        Dismounts a mounted piece by invoking its specific unmount ability.

        If the given piece has a 'use_ability' method and is recognized as a mounted wizard or mounted prince,
        this method will call the appropriate unmount ability on the piece, passing the current board as an argument.

        Args:
            piece: The game piece to be dismounted. Must have a 'name' attribute and optionally a 'use_ability' method.

        """
        if hasattr(piece, "use_ability"):
            if piece.name == "mounted_wizard":
                piece.use_ability("unmount_dragon", self.board)
            elif piece.name == "mounted_prince":
                piece.use_ability("unmount_lion", self.board)
                
                
# ---------------------------------------------
# Swap Pieces
# ---------------------------------------------
                
    def swap(self, piece, swap_move, target_row, target_col):
        """
        Swaps the given piece with the piece at the target location using the SwapMove logic.
        """
        target_piece = self.board.grid[target_row][target_col]
        if type(target_piece).__name__ in ("Lion", "Dragon"):
            return  # Do not swap
        swap_move.execute_swap(piece, self.board, target_row, target_col)

# ---------------------------------------------
# Combime WhiteHat and BlackHat
# ---------------------------------------------

    def is_combining_hats(self, piece, target_piece):
        if piece is None or target_piece is None:
            return False
        names = {piece.name, target_piece.name}
        return names == {"white_hat", "black_hat"}
    
    def combine_hats(self, piece, target_piece):
        piece.use_ability("combine_hat", self.board, target_piece)

    def reset_game(self):
        """Reset the board and any manager state (turn, clocks, etc)."""
        # If you track turn/players/clock, reset them here as well.
        self.board.reset()

    def undo_move(self):
        """
        Ask the board to undo the last move. Update any manager state (turn switching).
        """
        undone = self.board.undo_last_move()
        if undone:
            # If you track turn, flip it back here (example):
            # self.current_player = 1 - self.current_player
            pass
        return undone