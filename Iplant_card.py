import pygame
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL

class IPlantCard(Sprite):
    def __init__(self, image, pos_x, pos_y, price = 0):
        super().__init__()
        self.name = image
        self.surf = pygame.image.load(f"./assets/plants/{image}_card.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 150))
        self.rect = self.surf.get_rect(center=(pos_x, pos_y))
        self.is_selected = False
        self.price = price
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

