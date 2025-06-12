
import pygame
from game.constants import WIDTH, HEIGHT
from game.board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Royal Chess")
    
    board = Board()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        board.draw(screen)
        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()