import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        #sprite setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
    
    def create_map(self):
        for rowIndex, row in enumerate(WORLD_MAP):
            for colIndex, col in enumerate(WORLD_MAP):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites])
                    
    
    
    def run(self):
        
        #drawing level
        self.visible_sprites.draw(self.display_surface)
        