import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else 1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    # Image/url of the piece
    class Piece:
        def set_texture(self, size=80):
            base_path = os.path.dirname(os.path.abspath(__file__))  # path to piece.py
            image_path = os.path.join(base_path, "..", "assets", "images", f"images_{size}", f"{self.color}_{self.name}.png")
            self.texture = os.path.normpath(image_path)
        
    def add_moves(self, move):
        self.moves.append(move)


# ================== Starting Pieces ==================

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        # Parameters: name, color, value
        super().__init__("pawn", color, 1.0)


class Royal_guard(Piece):
    def __init__(self, color):
        super().__init__("royal_guard", color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("knight", color, 1.0)


class Counselor(Piece):
    def __init__(self, color):
        super().__init__("counselor", color, 1.0)


class Rook(Piece):
    def __init__(self, color):
        super().__init__("rook", color, 1.0)


class Wizard(Piece):
    def __init__(self, color):
        super().__init__("wizard", color, 1.0)


class Prince(Piece):
    def __init__(self, color):
        super().__init__("prince", color, 1.0)


class Dragon(Piece):
    def __init__(self, color):
        super().__init__("dragon", color, 1.0)


class Lion(Piece):
    def __init__(self, color):
        super().__init__("lion", color, 1.0)


class King(Piece):
    def __init__(self, color):
        super().__init__("king", color, 10000.0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__("queen", color, 1.0)


# ================== Out of board Pieces ==================

class Flag(Piece):
    def __init__(self, color):
        super().__init__("flag", color, 1.0)


class White_hat(Piece):
    def __init__(self, color):
        super().__init__("white_hat", color, 1.0)


class Black_hat(Piece):
    def __init__(self, color):
        super().__init__("black_hat", color, 1.0)



# ================== Combined Pieces ==================

class Mounted_wizard(Piece):
    def __init__(self, color):
        super().__init__("mounted_wizard", color, 1.0)


class Mounted_prince(Piece):
    def __init__(self, color):
        super().__init__("mounted_prince", color, 1.0)


class Hacker(Piece):
    def __init__(self, color):
        super().__init__("hacker", color, 1.0)
