import pygame as p


class TileMap:
    def __init__(self, level, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        with open(f"assets/levels/{level}.txt", "r") as file:
            for line in file:
                self.map_data.append([int(x) for x in line.split()])

    def render(self, surface):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                rect = p.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                p.draw.rect(surface, (255, 255, 255), rect)
