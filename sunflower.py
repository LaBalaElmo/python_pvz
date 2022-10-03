from Iplant import IPlant
import pygame
from sun import Sun

class Sunflower(IPlant):
    def __init__(self, pos_x, pos_y, screen_width, screen_height, index_garden, move_image):
        super().__init__("./assets/plants/sunflower.png", pos_x, pos_y, 4, screen_width, screen_height, index_garden, move_image)

    def update(self, projectiles, plants, sprites, suns, zombies, reason, matrix_garden):
        if reason == "die":
            self.get_damage(plants, zombies, sprites, matrix_garden, 0)
        if reason == 'sun':
            projectile = Sun(self.pos_X, self.pos_y, "./assets/sun.png")
            suns.add(projectile)
            sprites.add(projectile)
        