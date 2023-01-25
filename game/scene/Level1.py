import pygame as p
from game.scene.Scene import Scene
from util.TileMap import TileMap
from util.Settings import Settings
from util.Assets import Assets


class Level1(Scene):
    def __init__(self):
        super().__init__("LEVEL 1")
        self.tile_map = TileMap("1", 32)

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/level.png"), (0, 0))
        self.tile_map.render(surf)

        return surf

