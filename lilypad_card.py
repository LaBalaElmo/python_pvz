from Iplant_card import IPlantCard
from lilypad import Lilypad

class LilypadCard(IPlantCard):
    def __init__(self, pos_x, pos_y):
        super().__init__("lilypad", pos_x, pos_y, 25)
    
    def add_plant(self, plants, sprites, position, screen_width, screen_height, index_garden):
        lilypad = Lilypad(position[0], position[1], screen_width, screen_height, index_garden, False)
        plants.add(lilypad)
        sprites.add(lilypad)