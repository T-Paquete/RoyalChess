import pygame
from ui.button import Button
from game.constants import WIDTH, HEIGHT

class Menu:
    def __init__(self, game_manager, panel_width=180, padding=12):
        self.game_manager = game_manager
        self.panel_width = panel_width
        self.padding = padding
        # place menu at right side
        self.rect = pygame.Rect(WIDTH - panel_width, 0, panel_width, HEIGHT)
        self.font = pygame.font.SysFont(None, 22)
        # buttons stacked with spacing
        btn_w = panel_width - padding * 2
        btn_h = 36
        x = self.rect.x + padding
        y = padding + 40
        self.buttons = [
            Button((x, y, btn_w, btn_h), "Reset game", self._on_reset, font=self.font),
            Button((x, y + btn_h + 10, btn_w, btn_h), "Undo move", self._on_undo, font=self.font)
        ]

    def _on_reset(self):
        try:
            self.game_manager.reset_game()
        except Exception:
            # keep UI resilient; real app should log
            pass

    def _on_undo(self):
        try:
            self.game_manager.undo_move()
        except Exception:
            pass

    def draw(self, surface):
        # background panel
        pygame.draw.rect(surface, (30,30,30), self.rect)
        # title
        title = self.font.render("Menu", True, (255,255,255))
        surface.blit(title, (self.rect.x + self.padding, self.padding + 8))
        # buttons
        for btn in self.buttons:
            btn.draw(surface)

    def handle_event(self, event):
        # route to buttons; return True if handled
        for btn in self.buttons:
            if btn.handle_event(event):
                return True
        return False