import pygame
from button import Button
from screeninfo import get_monitors
from pygame.locals import K_ESCAPE, KEYDOWN
from common_zombie import CommonZombie
from random import randrange
from lilypad_card import LilypadCard
from nut_card import NutCard
from peashooter_card import PeashooterCard

from sunflower_card import SunflowerCard

class App():
    def __init__(self, screen_width, screen_height):
        super().__init__()
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.is_running = False
        self.is_game_paused = False
        self.bg = pygame.image.load("./assets/garden.png")
        self.bg = pygame.transform.scale(self.bg, (screen_width, screen_height))
        self.half_rows, self.row_dimension = self.get_garden_position_rows(screen_height)
        self.half_columns, self.column_dimension = self.get_garden_position_columns(screen_width)

        self.sun_panel = pygame.Surface((127, 160))
        self.sun_panel.fill((66, 40, 14))
        self.sun_panel_rect = self.sun_panel.get_rect()
        self.sun_image = pygame.image.load("./assets/sun.png").convert_alpha()

        self.sun_counter = 500
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.sun_counter), True, (255, 255, 255))
        self.textRect = self.text.get_rect(center=(60, 130))

        self.card_panel = pygame.Surface((700, 160))
        self.card_panel.fill((66, 40, 14))
        self.card_panel_rect = self.card_panel.get_rect(center=(500, 80))
        self.plant_cards = self.set_card_images()
        self.zombie_amount = 10

        self.sprites = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.plants = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.suns = pygame.sprite.Group()
        self.ADD_ZOMBIE_EVENT = pygame.USEREVENT + 1
        self.ADD_PROJECTILE_EVENT = pygame.USEREVENT + 2
        self.ZOMBIE_ATACK = pygame.USEREVENT + 3
        self.SUN_EMIT = pygame.USEREVENT + 4
        self.win = False
        self.lose = False
        self.has_init = False

        self.font_win = pygame.font.Font('freesansbold.ttf', 120)
        self.text_win = self.font_win.render("YOU WIN", True, (0, 0, 0))
        self.textRect_win = self.text_win.get_rect(center=(self.screen_width//2, self.screen_height//3))

        self.font_lose = pygame.font.Font('freesansbold.ttf', 120)
        self.text_lose = self.font_lose.render("YOU LOSE", True, (0, 0, 0))
        self.textRect_lose = self.text_lose.get_rect(center=(self.screen_width//2, self.screen_height//3))
        self.init_screen = pygame.image.load("./assets/init_menu.png")
        self.init_screen = pygame.transform.scale(self.init_screen, (screen_width, screen_height))

        self.garden_matrix = [[0]*10]*2 + [[1]*10]*2 + [[0]*10]*2

    def get_garden_position_rows(self, screen_height):
        position_list = []
        row_dimensions = []
        percentage_rows = [0.153, 0.2878, 0.4541, 0.6122, 0.7286, 0.8673, 1]
        for index in range(6):
            position_list.append(((percentage_rows[index + 1] * screen_height) - (percentage_rows[index] * screen_height))//
            2 + round(screen_height * percentage_rows[index]))
            row_dimensions.append((round(percentage_rows[index] * screen_height), round(percentage_rows[index + 1] * screen_height)))
        return position_list, row_dimensions

    def get_garden_position_columns(self, screen_width):
        position_list = []
        column_dimensions = []
        percentage_colums = [0.25, 0.3315, 0.4074, 0.4889, 0.5679, 0.6451, 0.7296, 0.7981, 0.8756, 0.9556]
        for index in range(9):
            position_list.append(round((percentage_colums[index + 1] * screen_width) - (percentage_colums[index] * screen_width))//
            2 + round(screen_width * percentage_colums[index]))
            column_dimensions.append((round(percentage_colums[index] * screen_width), round(percentage_colums[index + 1] * screen_width)))
        return position_list, column_dimensions

    def set_card_images(self):
        card_plants = [
            SunflowerCard(220, 80),
            PeashooterCard(340, 80),
            LilypadCard(460, 80),
            NutCard(580, 80)
        ]
        return card_plants

    def add_zombie(self, zombie):
        self.zombies.add(zombie)
        self.sprites.add(zombie)
        self.zombie_amount -= 1
        
    def update(self): 
        self.screen.blit(self.sun_panel, self.sun_panel_rect)
        self.screen.blit(self.sun_image, (0,0))
        self.screen.blit(self.font.render(str(self.sun_counter), True, (255, 255, 255)), self.textRect)
        self.screen.blit(self.card_panel, self.card_panel_rect)
        self.zombies.update(self.projectiles, self.zombies, self.sprites, self.plants)
        self.projectiles.update()
        amount = [0]
        self.suns.update(amount)
        self.sun_counter += amount[0]
        for sprite in self.sprites:
            self.screen.blit(sprite.surf, sprite.rect)
        for card in self.plant_cards:
            card.draw(self.screen)

    def run(self):
        self.is_running = True
        pygame.time.set_timer(self.ADD_ZOMBIE_EVENT, 11000)
        pygame.time.set_timer(self.ADD_PROJECTILE_EVENT, 2000)
        pygame.time.set_timer(self.ZOMBIE_ATACK, 1500)
        pygame.time.set_timer(self.SUN_EMIT, 8000)
        resume_button = Button("./assets/resume_button.png", self.screen_width//2, self.screen_height//3)
        quit_button = Button("./assets/exit_button.png", self.screen_width//2, self.screen_height*2//3)

        win_button = Button("./assets/exit_button.png", self.screen_width//2, self.screen_height*2//3)

        lose_button = Button("./assets/exit_button.png", self.screen_width//2, self.screen_height*2//3)

        play_button = Button("./assets/play_button.png", self.screen_width//2, self.screen_height*2//3)
            
        while self.is_running:
            self.screen.blit(self.bg, (0, 0))
            if self.is_game_paused:
                resume_button.draw(self.screen)
                quit_button.draw(self.screen)
                if quit_button.is_clicked():
                    self.is_running = False
                if resume_button.is_clicked():
                    self.is_game_paused = False
            elif self.win:
                win_button.draw(self.screen)
                self.screen.blit(self.text_win, self.textRect_win)
                if win_button.is_clicked():
                    self.is_running = False
            elif self.lose:
                lose_button.draw(self.screen)
                self.screen.blit(self.text_lose, self.textRect_lose)
                if lose_button.is_clicked():
                    self.is_running = False
            elif not self.has_init:
                self.screen.blit(self.init_screen, (0,0))
                play_button.draw(self.screen)
                if play_button.is_clicked():
                    self.has_init = True
            else :
                self.update()
                
            for zombie in self.zombies.sprites():
                if zombie.rect.centerx == 0:
                    self.lose = True
                
            # keys = pygame.mouse.get_pressed()
            # print(self.half_columns, self.column_dimension, pygame.mouse.get_pos())
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.is_game_paused = True
                if event.type == self.ADD_PROJECTILE_EVENT and not self.is_game_paused:
                    self.plants.update(self.projectiles, self.plants, self.sprites, self.suns, self.zombies, "shoot", self.garden_matrix)
                if event.type == self.ZOMBIE_ATACK and not self.is_game_paused:
                    self.plants.update(self.projectiles, self.plants, self.sprites, self.suns, self.zombies, "die", self.garden_matrix)
                if event.type == self.SUN_EMIT and not self.is_game_paused:
                    self.plants.update(self.projectiles, self.plants, self.sprites, self.suns, self.zombies, "sun", self.garden_matrix)
                if event.type == pygame.MOUSEBUTTONDOWN and not self.is_game_paused:
                    for card in self.plant_cards:
                        if card.is_selected:
                            mouse_position = pygame.mouse.get_pos()
                            position_x = 0
                            position_y = 0
                            index_x = 0
                            index_y = 0
                            for column in self.column_dimension:
                                if mouse_position[0] >= column[0] and mouse_position[0] <= column[1]:
                                    position_x = self.half_columns[self.column_dimension.index(column)]
                                    index_x = self.column_dimension.index(column)
                                    break
                            for row in self.row_dimension:
                                if mouse_position[1] >= row[0] and mouse_position[1] <= row[1]:
                                    position_y = self.half_rows[self.row_dimension.index(row)]
                                    index_y = self.row_dimension.index(row)
                                    break
                            if position_x != 0 and position_y != 0 and self.sun_counter >= card.price and self.garden_matrix[index_y][index_x] != 1 and card.name != "lilypad":
                                zero, pos_aux_y = False, 0
                                if index_y == 0 and self.garden_matrix[index_y+1][index_x] == 0:
                                    zero = True
                                    pos_aux_y = index_y + 1
                                if index_y == 1 and self.garden_matrix[index_y-1][index_x] == 0:
                                    zero = True
                                    pos_aux_y = index_y - 1
                                if index_y == 5 and self.garden_matrix[index_y-1][index_x] == 0:
                                    zero = True
                                    pos_aux_y = index_y - 1
                                if index_y == 4 and self.garden_matrix[index_y+1][index_x] == 0:
                                    zero = True
                                    pos_aux_y = index_y + 1
                                self.garden_matrix[index_y][index_x] = 1
                                if zero:
                                    self.garden_matrix[pos_aux_y][index_x] = 0
                                card.add_plant(self.plants, self.sprites, (position_x, position_y), self.screen_width, self.screen_height, (index_x, index_y))
                                self.sun_counter -= card.price
                            elif position_x != 0 and position_y != 0 and self.sun_counter >= card.price and self.garden_matrix[index_y][index_x] == 1 and card.name == "lilypad" and (index_y >=2 or index_y <=3):
                                self.garden_matrix[index_y][index_x] = 2
                                card.add_plant(self.plants, self.sprites, (position_x, position_y), self.screen_width, self.screen_height, (index_x, index_y))
                                self.sun_counter -= card.price
                            card.is_selected = False
                        if card.is_clicked():
                            card.is_selected = True
                        else:
                            card.is_selected = False

                elif event.type == self.ADD_ZOMBIE_EVENT and not self.is_game_paused:
                    random_position = randrange(self.screen_height - round(self.screen_height * 0.153)) + round(self.screen_height * 0.153)
                    row_to_generate_in = 0
                    zombie_image = ""
                    for row in self.row_dimension:
                        if(random_position >= row[0] and random_position <= row[1]):
                            row_to_generate_in = self.row_dimension.index(row)
                            if(row_to_generate_in == 2 or row_to_generate_in == 3):
                                zombie_image = "./assets/zombies/pool_zombie.png"
                            else:
                                zombie_image = "./assets/zombies/common_zombie.png"
                            break
                    if self.zombie_amount == 0:
                        if len(self.zombies.sprites()) == 0:
                            self.win = True
                    else:
                        self.add_zombie(CommonZombie(zombie_image, self.screen_width, self.half_rows[row_to_generate_in], 2, 5, self.screen_width, self.screen_height))

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__':
    app = App(get_monitors()[0].width-300, get_monitors()[0].height-300)
    app.run()