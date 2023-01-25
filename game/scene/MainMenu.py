from util.Settings import Settings
from game.scene.Scene import Scene
import pygame as p


class MainMenu(Scene):
    def __init__(self):
        super().__init__("MAIN MENU")

    def update(self):
        pass

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill((255, 255, 255))
        return surf
