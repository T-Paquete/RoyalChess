import pygame
from game.board import Board
from ui.display import Display
from ui.dragger import Dragger
from game.constants import WIDTH, HEIGHT, SQSIZE
from game_controller.game_manager import GameManager 




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Royal Chess")
    
    board = Board()
    display = Display()
    dragger = Dragger()
    game_manager = GameManager(board)
    selected_piece = None
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col = mouse_y // SQSIZE, mouse_x // SQSIZE
                piece = board.grid[row][col]
                if piece:
                    selected_piece = piece
                    dragger.start_drag(piece, row, col)
                    dragger.update_mouse((mouse_x, mouse_y))
                else:
                    selected_piece = None

            elif event.type == pygame.MOUSEMOTION:
                if dragger.is_dragging():
                    dragger.update_mouse(pygame.mouse.get_pos())

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragger.is_dragging():
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    target_row, target_col = mouse_y // SQSIZE, mouse_x // SQSIZE
                    piece = dragger.selected_piece
                    if piece:
                        game_manager.make_move(piece, target_row, target_col)
                    dragger.stop_drag()
                    selected_piece = None  # Clear selection after drop

        # Rendering (all handled by display.py)
        display.draw_board(screen)
        # Highlight possible moves if a piece is selected or being dragged
        highlight_piece = dragger.selected_piece if dragger.is_dragging() else selected_piece
        display.draw_possible_moves(screen, highlight_piece, board)
        display.draw_pieces(screen, board, exclude_piece=dragger.selected_piece if dragger.is_dragging() else None)
        if dragger.is_dragging():
            display.draw_dragged_piece(screen, dragger)
        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()