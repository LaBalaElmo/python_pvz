import pygame
from pygame.sprite import Sprite

class Projectil(Sprite):
    def __init__(self, pos_x, pos_y, image, screen_width):
        super().__init__()
        self.surf = pygame.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center=(pos_x, pos_y))
        self.speed = 15
        self.screen_width = screen_width

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.centerx >= self.screen_width:
            self.kill()