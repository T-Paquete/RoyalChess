import pygame
import os
from game.constants import SQSIZE
from game.constants import LIGHT_COLOR, DARK_COLOR, WHITE, HEIGHT, WIDTH, SQSIZE, COLS, ROWS

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


    def draw_pieces(self, screen, board, exclude_piece=None):
        for row in range(len(board.grid)): # 
            for col in range(len(board.grid[row])): #
                piece = board.grid[row][col]
                if piece and piece != exclude_piece:
                    image = self.load_piece_image(piece)
                    x = col * SQSIZE + (SQSIZE - image.get_width()) // 2
                    y = row * SQSIZE + (SQSIZE - image.get_height()) // 2
                    screen.blit(image, (x, y))
    
    
    def render(self, screen, board, dragger):
        # Draw the board squares
        self.draw_board(screen)
        # Draw all pieces except the one being dragged
        self.draw_pieces(screen, board, exclude_piece=dragger.selected_piece if dragger.is_dragging() else None)
        # Optionally, highlight possible moves for the selected piece
        if dragger.is_dragging() and dragger.selected_piece:
            self.draw_possible_moves(screen, dragger.selected_piece, board)
            self.draw_dragged_piece(screen, dragger)
        # Update the display
        pygame.display.flip()


    def draw_dragged_piece(self, screen, dragger):
        if dragger.is_dragging() and dragger.selected_piece:
            image = self.load_piece_image(dragger.selected_piece)
            x = dragger.mouse_x - image.get_width() // 2
            y = dragger.mouse_y - image.get_height() // 2
            screen.blit(image, (x, y))

    def draw_board(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(screen, color, rect)

