import pygame as p
from game.scene.Scene import Scene
from util.TileMap import TileMap
from util.Settings import Settings
from util.Assets import Assets
from util.Input import Input
from util.Scenes import Scenes
from game.system.Collisions import Collision

from game.object.Player import Player


class Level(Scene):
    def __init__(self):
        super().__init__("LEVEL")
        self.player = None

    def awake(self):
        self.player = Player()
        Collision.add(self.player)

    def set_level(self, level):
        TileMap.set_level(level)

    def update(self):
        self.player.update()

        Collision.update()

        if Input.get_key_down(p.K_ESCAPE):
            Scenes.set_scene("PAUSE")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/level.png"), (0, 0))
        TileMap.render(surf)
        self.player.sprite.draw(surf)

        return surf

    def exit(self):
        TileMap.clear()

