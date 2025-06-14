import os
import pygame
class Piece:
    def __init__(self, name, color, row, col, move=None, effects=None):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.effects = effects if effects is not None else []
        self.move = move  

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.moved = True


# ================== Starting Pieces ==================

class Pawn(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("pawn", color, row, col, effects)

class Royal_guard(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("royal_guard", color, row, col, effects)

class Knight(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("knight", color, row, col, effects)

class Counselor(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("counselor", color, row, col, effects)

class Rook(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("rook", color, row, col, effects)

class Wizard(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("wizard", color, row, col, effects)

class Prince(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("prince", color, row, col, effects)

class Dragon(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("dragon", color, row, col, effects)

class Lion(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("lion", color, row, col, effects)

class King(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("king", color, row, col, effects)

class Queen(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("queen", color, row, col, effects)

# ================== Out of board Pieces ==================

class Symbol(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("symbol", color, row, col, effects)

class White_hat(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("white_hat", color, row, col, effects)

class Black_hat(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("black_hat", color, row, col, effects)

# ================== Combined Pieces ==================

class Mounted_wizard(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("mounted_wizard", color, row, col, effects)

class Mounted_prince(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("mounted_prince", color, row, col, effects)

class Grey_hat(Piece):
    def __init__(self, color, row, col, effects=None):
        super().__init__("grey_hat", color, row, col, effects)
