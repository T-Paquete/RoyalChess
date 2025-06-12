import pygame
import sys

from const import *
from game import Game

# Main class
class Main:

    # Method that is calle when creating an object
    def __init__(self):
        pygame.init() # Initializes the pygame module
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Creates the screen and saves it to self.screen
        pygame.display.set_caption('Royal_Chess') # Caption of the app
        self.game = Game() # Main reference to the game class

    def mainloop(self):
        screen = self.screen
        game = self.game

        # Set up the pygame
        while True:
            # Show background
            game.show_bg(screen) # Since show_bg has surface as parameter

            # Show pieces
            game.show_pieces(screen)


            # Loop through all pygame events
            # Check if user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




            # Update screen
            pygame.display.update()


# Instance of Main
main = Main()
main.mainloop()

