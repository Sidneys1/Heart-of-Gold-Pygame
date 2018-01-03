import pygame

from os import listdir
from os.path import isfile, join

class BackgroundTile:
    def __init__(self, tile_size, tile, x, y):
        self._tile = tile
        self._tile_size = tile_size
        self.x = x
        self.y = y
        self.rect = tile.get_rect()
        self._rect_x = self.rect.x
        self._rect_y = self.rect.y

    def draw(self, screen, offset):
        self.rect.center = (self.x * self._tile_size[0] + offset[0],
                            self.y * self._tile_size[1] + offset[1])
        screen.blit(self._tile, self.rect)


class Background:
    def __init__(self, tile_location, tile_size):
        self._tile_size = tile_size
        self._tiles = {}
        tile_files = [
            f for f 
            in listdir(tile_location) 
            if isfile(join(tile_location, f))
        ]
        for tile in tile_files:
            x, y = [int(z) for z in tile.split('.')[0].split()]
            self._tiles[(x, y)] = BackgroundTile(tile_size, pygame.image.load(
                join(tile_location, tile)).convert(), x, y)
            print("Loaded {}: Tile {},{}".format(tile, x, y))

    def draw(self, screen, offset):
        for tile in self._tiles.values():
            tile.draw(screen, offset)
        
