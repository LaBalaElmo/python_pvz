import pygame
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL

class Sun(Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.surf = pygame.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center=(pos_x, pos_y))

    def update(self, suns_amount):
        if self.is_clicked():
            self.kill()
            suns_amount[0] = 50
    
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

