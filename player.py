import pygame

pygame.init()

FONT = pygame.font.Font(None, 32)

class Player:
    def __init__(self, nickname, color):
        self.rect = pygame.rect.Rect(150, 150, 64, 64)
        self.color = color
        self.nickname = nickname

    def update(self):
        keys = pygame.key.get_pressed()

        self.rect.x += 6 * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        self.rect.y += 6 * (keys[pygame.K_DOWN] - keys[pygame.K_UP])

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        render = FONT.render(self.nickname, False, (0, 0, 0))
        window.blit(render, (self.rect.x, self.rect.y))


