import pygame
from pygame.sprite import Sprite

class IPlant(Sprite):
    def __init__(self, image, pos_x, pos_y, hp, screen_width, screen_height, index_garden, move_image):
        super().__init__()
        self.pos_X = pos_x
        self.pos_y = pos_y
        self.surf = pygame.image.load(image)
        self.surf = pygame.transform.scale(self.surf, (round(screen_width*0.04729), round(screen_height * 0.1074))).convert_alpha()
        if move_image:
            self.rect = self.surf.get_rect(center=(pos_x, pos_y - round(screen_height * 0.0463)))
        else:
            self.rect = self.surf.get_rect(center=(pos_x, pos_y))
        self.hp = hp
        self.screen_width = screen_width
        self.index_garden = index_garden

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        pass

    def get_damage(self, plants, zombies, sprites, garden_matrix, value_garden):
        if pygame.sprite.spritecollideany(self, zombies):
            self.hp -=1
        if self.hp <= 0:
            sprites.remove(self)
            plants.remove(self)
            self.kill()
            if self.index_garden[1]>=2 and self.index_garden[1]<=3:
                garden_matrix[self.index_garden[1]][self.index_garden[0]] = 1
            else:
                garden_matrix[self.index_garden[1]][self.index_garden[0]] = value_garden