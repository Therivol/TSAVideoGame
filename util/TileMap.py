from util.Assets import Assets
from game.system.Collisions import Collision
import pygame as p


class TileMap:

    tile_size = 32
    map_data = []

    @staticmethod
    def clear():
        TileMap.map_data = []

    @staticmethod
    def set_level(level):
        with open(f"assets/levels/{level}.txt", "r") as file:
            for line in file:
                TileMap.map_data.append([tile for tile in line.split()])

        Collision.load_level(TileMap.map_data, TileMap.tile_size)

    @staticmethod
    def render(surface):
        for y, row in enumerate(TileMap.map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    continue
                tile = Assets.get_image(f"assets/tiles/{tile}.png")
                surface.blit(tile, (x * TileMap.tile_size, y * TileMap.tile_size))
