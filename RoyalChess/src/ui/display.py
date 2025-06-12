import pygame
import os
from game.constants import SQSIZE

class PieceDisplay:
    def __init__(self, piece):
        self.piece = piece
        scale_size = int(SQSIZE * 0.75)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(
            base_path, "..", "ui", "assets", "pieces", f"{piece.color}_{piece.name}.png"
        )
        image_path = os.path.normpath(image_path)
        try:
            image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            raise FileNotFoundError(f"Could not load image at {image_path}: {e}")
        self.texture = pygame.transform.smoothscale(image, (scale_size, scale_size))
        self.scale_size = scale_size

    def draw(self, screen):
        x = self.piece.col * SQSIZE + (SQSIZE - self.scale_size) // 2
        y = self.piece.row * SQSIZE + (SQSIZE - self.scale_size) // 2
        screen.blit(self.texture, (x, y))