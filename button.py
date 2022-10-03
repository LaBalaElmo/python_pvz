import pygame
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL

class Button(Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(pos_x, pos_y))
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

