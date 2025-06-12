
import pygame
from board import Board

from const import *

# (Class responsible for all the rendering methods)

class Game:
    def __init__(self):
        self.board = Board()

    # Show methods
    # Show background
    def show_bg(self, surface): # surface: self.screen
        for row in range(ROWS):
            for col in range(COLS):
                # Pattern of the chess board
                if row == 0 or row == ROWS - 1:
                    color = (255, 255, 255)  # White
                elif (row + col) % 2 != 0:
                    color = (234, 235, 200) # Light-green
                else:
                    color = (119, 154, 88) # Dark-green

                # Create pygame rectangle (4 parameters)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # Show rectangle on the screen
                # Parameters: surface, color, rectangle
                pygame.draw.rect(surface, color, rect)

    # Show pieces
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Check if square has piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
