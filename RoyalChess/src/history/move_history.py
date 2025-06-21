

class MoveHistory:
    def __init__(self):
        self.moves = []          # list of all moves
        self.current_index = -1  # pointer to the current move (for undo/redo)

    def add_move(self, move):
        """
        Add a new move to the history, discarding any 'future' moves
        if we've undone moves previously.
        """
        self.moves = self.moves[:self.current_index + 1]
        self.moves.append(move)
        self.current_index += 1


    def undo(self):
        """Undo the last move, if possible, and return that move."""
        if self.current_index >= 0:
            move = self.moves[self.current_index]
            self.current_index -= 1
            return move
        return None

    def redo(self):
        """Redo the next move, if any, and return that move."""
        if self.current_index + 1 < len(self.moves):
            self.current_index += 1
            return self.moves[self.current_index]
        return None

    def get_current_state(self):
        """
        Return a list of moves reflecting the current state
        (up to current_index).
        """
        return self.moves[:self.current_index + 1]

