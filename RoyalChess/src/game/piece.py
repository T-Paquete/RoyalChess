import os
import pygame
from game.constants import SQSIZE

class Piece:
    def __init__(self, name, color, row, col, texture=None, effects=None):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.effects = effects if effects is not None else []
        self.moved = False

        if texture is None:
            base_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(
                base_path, "..", "..", "ui", "assets", "pieces", f"{self.color}_{self.name}.png"
            )
            image_path = os.path.normpath(image_path)
            self.texture = pygame.image.load(image_path).convert_alpha()
        else:
            self.texture = texture
    
    def draw(self, screen):
        x = self.col * SQSIZE
        y = self.row * SQSIZE
        screen.blit(self.texture, (x, y))
        
    def move(self, new_row, new_col):
        self.new_row = new_row
        self.new_col = new_col
        self.moved = True
        
        