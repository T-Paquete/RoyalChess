from game.move import *

class Piece:
    def __init__(self, name, color, row, col, rank=None, moves=None, effects=None, ability=None, max_steps=None):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.rank = rank if rank is not None else 0
        self.direction = None
        self.effects = effects if effects is not None else []
        self.moves = moves if moves else []
        self.max_steps = max_steps
        self.ability = ability if ability is not None else []

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.moved = True 

    def get_possible_moves(self, board):
        all_moves = []
        for move_obj in self.moves:
            all_moves.extend(move_obj.get_possible_moves(self, board))
        return all_moves


# ================== Starting Pieces ==================

class Pawn(Piece):
    def __init__(self, color, row, col, rank=None, moves=[PawnMove()]):
        super().__init__("pawn", color, row, col, rank=rank, moves=moves)

class RoyalGuard(Piece):
    def __init__(self, color, row, col, rank=None, moves=[PawnMove()]):
        super().__init__("royal_guard", color, row, col, rank=rank, moves=moves)

class Knight(Piece):
    def __init__(self, color, row, col, rank=None, moves=[KnightMove()]):
        if moves is None:
            moves = [KnightMove()]
        super().__init__("knight", color, row, col, rank=rank, moves=moves)

class Counselor(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove()], ability=None):
        super().__init__("counselor", color, row, col, rank=rank, moves=moves, ability=ability)

class Rook(Piece):
    def __init__(self, color, row, col, rank=None, moves=[StraightMove()]):
        super().__init__("rook", color, row, col, rank=rank, moves=moves)

class Wizard(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        super().__init__("wizard", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)

class Prince(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        super().__init__("prince", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)

class Dragon(Piece):
    def __init__(self, color, row, col, rank=None, moves=None):
        super().__init__("dragon", color, row, col, rank=rank, moves=moves)

class Lion(Piece):
    def __init__(self, color, row, col, rank=None, moves=None):
        super().__init__("lion", color, row, col, rank=rank, moves=moves)

class King(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove(), StraightMove()], effects=None):
        super().__init__("king", color, row, col, rank=rank, moves=moves, effects=effects, max_steps=1)

class Queen(Piece):
    def __init__(self, color, row, col, rank=None, moves=[StraightMove(), DiagonalMove()]):
        super().__init__("queen", color, row, col, rank=rank, moves=moves)

# ================== Out of board Pieces ==================

class Symbol(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None):
        super().__init__("symbol", color, row, col, rank=rank, moves=moves, effects=effects)

class WhiteHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        super().__init__("white_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)

class BlackHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        super().__init__("black_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)

# ================== Combined Pieces ==================

class MountedWizard(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, ability=None):
        super().__init__("mounted_wizard", color, row, col, rank=rank, moves=moves, ability=ability)

class MountedPrince(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, ability=None):
        super().__init__("mounted_prince", color, row, col, rank=rank, moves=moves, ability=ability)

class GreyHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        super().__init__("grey_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)
