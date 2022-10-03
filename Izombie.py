import pygame
from pygame.sprite import Sprite

class IZombie(Sprite):
    def __init__(self, image, pos_x, pos_y, speed, hp, screen_width, screen_height):
        super().__init__()
        self.surf = pygame.image.load(image)
        self.surf = pygame.transform.scale(self.surf, (round(screen_width*0.05729), round(screen_height * 0.1574))).convert_alpha()
        self.rect = self.surf.get_rect(center=(pos_x, pos_y - round(screen_height * 0.0463)))
        self.speed = speed
        self.hp = hp

    def update(self, projectiles, zombies, sprites, plants):
        pass
    
    def get_damage(self, projectiles, zombies, sprites):
        if pygame.sprite.spritecollideany(self, projectiles):
            self.hp -=1
        pygame.sprite.groupcollide(
            projectiles,    # primer sprite group
            zombies,               # segundo sprite group
            True,                       # True = invocar kill() si sprites del grupo 1 colisionan
            False                        # igual que arriba pero para el 2do grupo
            )
        if self.hp <= 0:
            sprites.remove(self)
            zombies.remove(self)
            self.kill()