import pygame
import os
from game.constants import LIGHT_COLOR, DARK_COLOR, WHITE, SQSIZE, COLS, ROWS, DARK_RED, LIGHT_RED
from game.piece import Piece

from game.constants import SQSIZE

def _board_to_screen(col, row, board, flip: bool):
    """Return top-left pixel (x, y) for a square (col,row) respecting flip."""
    if not flip:
        screen_x = col * SQSIZE
        screen_y = row * SQSIZE
    else:
        screen_x = (board.cols - 1 - col) * SQSIZE
        screen_y = (board.rows - 1 - row) * SQSIZE
    return screen_x, screen_y

class Display:
    def __init__(self):
        self.piece_images = {}

    def load_piece_image(self, piece):
        key = (piece.color, piece.name)
        if key not in self.piece_images:
            base_path = os.path.dirname(os.path.abspath(__file__)) # Get the directory of this file
            image_path = os.path.join(
                base_path, "..", "ui", "assets", "pieces", f"{piece.color}_{piece.name}.png"
            )
            image_path = os.path.normpath(image_path) # Normalize the path to handle different OS path separators
            try:
                image = pygame.image.load(image_path).convert_alpha() # Load the image with alpha transparency
            except pygame.error as e:
                raise FileNotFoundError(f"Could not load image at {image_path}: {e}")
            scale_size = int(SQSIZE * 0.75) # Scale size to fit within the square
            image = pygame.transform.smoothscale(image, (scale_size, scale_size)) # Scale the image to fit the square size
            self.piece_images[key] = image
        return self.piece_images[key]


    def draw_pieces(self, screen, board, exclude_piece=None, flip=False):
        for row in range(len(board.grid)): # 
            for col in range(len(board.grid[row])): #
                piece = board.grid[row][col]
                if piece and piece != exclude_piece:
                    screen_x, screen_y = _board_to_screen(col, row, board, flip)
                    image = self.load_piece_image(piece)
                    x = screen_x + (SQSIZE - image.get_width()) // 2
                    y = screen_y + (SQSIZE - image.get_height()) // 2
                    screen.blit(image, (x, y))
    
    
    def render(self, screen, board, dragger):
        # Draw the board squares
        self.draw_board(screen)
        # Draw all pieces except the one being dragged
        self.draw_pieces(screen, board, exclude_piece=dragger.selected_piece if dragger.is_dragging() else None, flip=board.flip)
        # Optionally, highlight possible moves for the selected piece
        if dragger.is_dragging() and dragger.selected_piece:
            self.draw_possible_moves(screen, dragger.selected_piece, board, flip=board.flip)
            self.draw_dragged_piece(screen, dragger, flip=board.flip)
        # Update the display
        pygame.display.flip()


    def draw_dragged_piece(self, screen, dragger, flip=False):
        if dragger.is_dragging() and dragger.selected_piece:
            piece = dragger.selected_piece
            image = self.load_piece_image(piece)
            x = dragger.mouse_x - image.get_width() // 2
            y = dragger.mouse_y - image.get_height() // 2
            screen.blit(image, (x, y))

    def draw_board(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or row == ROWS - 1:
                    color = WHITE
                else:
                    color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(screen, color, rect)

    def draw_possible_moves(self, screen, piece, board, flip=False):
        if piece is None:
            return
        possible_moves = piece.get_possible_moves(board)
        for row, col in possible_moves:
            screen_x, screen_y = _board_to_screen(col, row, board, flip)
            is_light_square = (row + col) % 2 == 0
            color = LIGHT_RED if is_light_square else DARK_RED
            surface = pygame.Surface((SQSIZE, SQSIZE), pygame.SRCALPHA)
            pygame.draw.rect(surface, color, (0, 0, SQSIZE, SQSIZE))
            screen.blit(surface, (screen_x, screen_y))



