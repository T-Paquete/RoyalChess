import pygame
from game.board import Board
from ui.display import Display
from ui.dragger import Dragger
from ui.menu import Menu
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
    menu = Menu(game_manager)               # <-- new
    selected_piece = None
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Let menu consume clicks first
            if menu.handle_event(event):
                continue

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # map mouse -> board indices considering flip
                sq_x = mouse_x // SQSIZE
                sq_y = mouse_y // SQSIZE

                if game_manager.flipped:
                    board_col = (board.cols - 1) - sq_x
                    board_row = (board.rows - 1) - sq_y
                else:
                    board_row = sq_y
                    board_col = sq_x

                # avoid indexing when clicking the menu or outside board
                if 0 <= board_row < board.rows and 0 <= board_col < board.cols:
                    piece = board.grid[board_row][board_col]
                else:
                    piece = None

                if piece:
                    selected_piece = piece
                    dragger.start_drag(piece, board_row, board_col)
                    dragger.update_mouse((mouse_x, mouse_y))
                else:
                    selected_piece = None

            elif event.type == pygame.MOUSEMOTION:
                if dragger.is_dragging():
                    dragger.update_mouse(pygame.mouse.get_pos())

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragger.is_dragging():
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    sq_x = mouse_x // SQSIZE
                    sq_y = mouse_y // SQSIZE

                    if game_manager.flipped:
                        target_col = (board.cols - 1) - sq_x
                        target_row = (board.rows - 1) - sq_y
                    else:
                        target_row = sq_y
                        target_col = sq_x

                    if 0 <= target_row < board.rows and 0 <= target_col < board.cols:
                        piece = dragger.selected_piece
                        if piece:
                            game_manager.make_move(piece, target_row, target_col)
                    dragger.stop_drag()
                    selected_piece = None

        # Rendering (pass flip to display functions)
        display.draw_board(screen)  # board background doesn't need flip
        highlight_piece = dragger.selected_piece if dragger.is_dragging() else selected_piece
        display.draw_possible_moves(screen, highlight_piece, board, flip=game_manager.flipped)
        display.draw_pieces(screen, board, exclude_piece=dragger.selected_piece if dragger.is_dragging() else None, flip=game_manager.flipped)
        if dragger.is_dragging():
            display.draw_dragged_piece(screen, dragger, flip=game_manager.flipped)

        menu.draw(screen)   # <-- draw menu on top/right

        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()