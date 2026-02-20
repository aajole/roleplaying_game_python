from config import *
from ui import UIElement


class Tile:
    def __init__(self,name, x, y, walkable):
        self.name = name
        self.tileset = tileset1
        self.walkable = walkable
        self.image = tileset1.subsurface([x * 32, y * 32,32,32])


class Map:
    def __init__(self, map_file):

        file = open(map_file, "r")
        mapdata = file.read()
        file.close()

        self.tile_types = [
            Tile("grass", 0, 0, True), 
            Tile("grass2", 0, 1, True), 
            Tile("forest", 1, 4, False), 
            Tile("water", 8, 1, False),
            Tile("rock", 3, 3, False),
            Tile("desert_mountain", 3, 1, False)            
        ]

        self.tiles = []

        for line in mapdata.split("\n"):
            row = []
            for tile in line:
                row.append(int(tile))
            self.tiles.append(row)

        self.tile_size = 32

    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_types[tile].image
                screen.blit(image, location)

