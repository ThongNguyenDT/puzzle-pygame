import pygame
from settings import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((BOXSIZE, BOXSIZE))
        self.x, self.y = x,y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != 'empty':
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, BLACK)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)
            draw_x = (BOXSIZE / 2) - self.font_size[0] / 2
            draw_y = (BOXSIZE / 2) - self.font_size[1] / 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill(BGCOLOUR)

    def update(self):
        self.rect.x = self.x * BOXSIZE
        self.rect.y = self.y * BOXSIZE

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom
