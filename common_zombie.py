from Izombie import IZombie
import pygame

class CommonZombie(IZombie):
    def __init__(self, image, pos_x, pos_y, speed=1, hp = 5, screen_width = 0, screen_height = 0):
        super().__init__(image, pos_x, pos_y, speed, hp, screen_width, screen_height)
        self.original_speed = speed

    def update(self, projectiles, zombies, sprites, plants):
        self.get_damage(projectiles, zombies, sprites)
        self.rect.move_ip(-self.speed, 0)
        if pygame.sprite.spritecollideany(self, plants):
            self.speed = 0
        else:
            self.speed = self.original_speed