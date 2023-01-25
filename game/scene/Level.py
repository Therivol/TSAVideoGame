import pygame as p
from game.scene.Scene import Scene
from util.TileMap import TileMap
from util.Settings import Settings
from util.Assets import Assets
from util.Input import Input
from util.Scenes import Scenes


class Level(Scene):
    def __init__(self):
        super().__init__("LEVEL")
        self.tile_map = TileMap("1", 32)

    def set_level(self, level):
        self.tile_map = TileMap(str(level), 32)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE):
            Scenes.set_scene("PAUSE")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/level.png"), (0, 0))
        self.tile_map.render(surf)
        surf.blit(Assets.get_image("assets/sprites/player.png", alpha=True), (400, 400))

        return surf

