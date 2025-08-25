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

    def can_combine(self, target):
        return False
    
    def use_ability(self, ability_name, board, *args, **kwargs):
        """
        Call the ability with the given name, passing any additional arguments.
        Returns the result of the ability's use() method, or None if not found.
        """
        for ability in self.ability:
            if getattr(ability, "name", None) == ability_name:
                return ability.use(self, board, *args, **kwargs)
        return None  # Ability not found
    
# ================== Starting Pieces ==================

class Pawn(Piece):
    def __init__(self, color, row, col, rank=None, moves=[PawnMove(), EnPassantMove()]):
        super().__init__("pawn", color, row, col, rank=rank, moves=moves)

class RoyalGuard(Piece):
    def __init__(self, color, row, col, rank=None, moves=[RoyalGuardMove(), EnPassantMove()]):
        super().__init__("royal_guard", color, row, col, rank=rank, moves=moves)

class Knight(Piece):
    def __init__(self, color, row, col, rank=None, moves=[KnightMove()]):
        super().__init__("knight", color, row, col, rank=rank, moves=moves)

class Counselor(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove()], ability=None):
        super().__init__("counselor", color, row, col, rank=rank, moves=moves, ability=ability)

class Rook(Piece):
    def __init__(self, color, row, col, rank=None, moves=[StraightMove()]):
        super().__init__("rook", color, row, col, rank=rank, moves=moves)

class Wizard(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove(), StraightMove(), SwapMove()], effects=None, ability=None):
        if moves is None:
            moves = [DiagonalMove(), StraightMove()]
        if ability is None:
            from game.abilities import MountDragonAbility, UnmountDragonAbility
            ability = [MountDragonAbility(), UnmountDragonAbility()]
        super().__init__("wizard", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability, max_steps=1)

    def can_combine(self, target):
        return (
            target is not None and
            getattr(target, "name", None) == "dragon" and
            getattr(target, "color", None) == self.color
        )
        
class Prince(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove(), StraightMove()], effects=None, ability=None):
        if moves is None:
            moves = [DiagonalMove(), StraightMove()]
        if ability is None:
            from game.abilities import MountLionAbility, UnmountLionAbility
            ability = [MountLionAbility(), UnmountLionAbility()]
        super().__init__("prince", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability, max_steps=1)

    def can_combine(self, target):
        return (
            target is not None and
            getattr(target, "name", None) == "lion" and
            getattr(target, "color", None) == self.color
        )
        
class Dragon(Piece):
    def __init__(self, color, row, col, rank=None, moves=[JumpOverDiagonalMove()]):
        super().__init__("dragon", color, row, col, rank=rank, moves=moves)

class Lion(Piece):
    def __init__(self, color, row, col, rank=None, moves=[JumpOverStraightMove()]):
        super().__init__("lion", color, row, col, rank=rank, moves=moves)

class King(Piece):
    def __init__(self, color, row, col, rank=None, moves=[DiagonalMove(), StraightMove()], effects=None):
        super().__init__("king", color, row, col, rank=rank, moves=moves, effects=effects, max_steps=1)

class Queen(Piece):
    def __init__(self, color, row, col, rank=None, moves=[StraightMove(), DiagonalMove()]):
        super().__init__("queen", color, row, col, rank=rank, moves=moves)

# ================== Out of board Pieces ==================

class Symbol(Piece):
    def __init__(self, color, row, col, rank=None, moves=[NonCapturingQueenMove()], effects=None):
        super().__init__("symbol", color, row, col, rank=rank, moves=moves, effects=effects, max_steps=1)

class WhiteHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        if moves is None:
            moves = [NonCapturingHatMove()]
        if ability is None:
            from game.abilities import CombineHatAbility
            ability = [CombineHatAbility()]
        super().__init__("white_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)
        
    def can_combine(self, target):
        return (target is not None and target.name == "black_hat")
        
class BlackHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        if moves is None:
            moves = [NonCapturingHatMove()]
        if ability is None:
            from game.abilities import CombineHatAbility
            ability = [CombineHatAbility()]
        super().__init__("black_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)

    def can_combine(self, target):
        return (target is not None and target.name == "white_hat")
# ================== Combined Pieces ==================

class MountedWizard(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, ability=None):
        moves = [CombinedMove([Wizard, Dragon])]
        super().__init__("mounted_wizard", color, row, col, rank=rank, moves=moves, ability=ability)

class MountedPrince(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, ability=None):
        moves = [CombinedMove([Prince, Lion])]
        super().__init__("mounted_prince", color, row, col, rank=rank, moves=moves, ability=ability)

class GreyHat(Piece):
    def __init__(self, color, row, col, rank=None, moves=None, effects=None, ability=None):
        moves = [CombinedMove([WhiteHat, BlackHat])]
        super().__init__("grey_hat", color, row, col, rank=rank, moves=moves, effects=effects, ability=ability)
