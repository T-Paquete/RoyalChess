
class Square:

    # Row and col define the positions of the square on the board
    # Can have 1 or 0 pieces (defaul: 0)
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None