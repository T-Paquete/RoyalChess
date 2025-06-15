
import pygame
from game.constants import WIDTH, HEIGHT
from game.board import Board
from ui.display import Display




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Royal Chess")
    
    board = Board()
    display = Display()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        board.draw(screen)
        display.draw_pieces(screen, board)
        pygame.display.flip() # Update the display

    pygame.quit()
    
if __name__ == "__main__":
    main()