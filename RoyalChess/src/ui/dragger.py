
from game.constants import SQSIZE

class Dragger:
    def __init__(self):
        self.dragging = False
        self.selected_piece = None
        self.start_row = None
        self.start_col = None
        self.mouse_x = 0
        self.mouse_y = 0

    def update_mouse(self, pos):
        self.mouse_x, self.mouse_y = pos

    def get_board_pos(self):
        row = self.mouse_y // SQSIZE
        col = self.mouse_x // SQSIZE
        return row, col

    def start_drag(self, piece, row, col):
        self.dragging = True
        self.selected_piece = piece
        self.start_row = row
        self.start_col = col

    def stop_drag(self):
        self.dragging = False
        self.selected_piece = None
        self.start_row = None
        self.start_col = None

    def is_dragging(self):
        return self.dragging

