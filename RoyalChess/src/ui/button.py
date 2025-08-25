import pygame

class Button:
    def __init__(self, rect, label, callback, font=None, bg_color=(50,50,50), fg_color=(255,255,255)):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.callback = callback
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font = font or pygame.font.SysFont(None, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, (0,0,0), self.rect, 2)
        text_surf = self.font.render(self.label, True, self.fg_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if callable(self.callback):
                    self.callback()
                return True
        return False