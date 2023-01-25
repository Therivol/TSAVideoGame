from util.Assets import Assets
import pygame as p


class TileMap:
    def __init__(self, level, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        with open(f"assets/levels/{level}.txt", "r") as file:
            for line in file:
                self.map_data.append([x for x in line.split()])

    def render(self, surface):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    continue
                tile = Assets.get_image(f"assets/tiles/{tile}.png")
                surface.blit(tile, (x * self.tile_size, y * self.tile_size))
