import pygame
import os
from game.constants import SQSIZE

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

    def draw_pieces(self, screen, board):
        for row in range(len(board.grid)): # 
            for col in range(len(board.grid[row])): #
                piece = board.grid[row][col]
                if piece:
                    image = self.load_piece_image(piece)
                    x = col * SQSIZE + (SQSIZE - image.get_width()) // 2
                    y = row * SQSIZE + (SQSIZE - image.get_height()) // 2
                    screen.blit(image, (x, y))