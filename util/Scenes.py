import pygame as p

from util.Debug import Debug
from util.Settings import Settings
from game.scene.Scene import Scene


class Scenes:
    # Dictionary to hold the scenes
    scenes = {}
    # Current scene
    current_scene = None
    # Default scene

    @staticmethod
    def add_scene(scene):
        Scenes.scenes[scene.name] = scene

    @staticmethod
    def set_scene(name):
        Scenes.current_scene = Scenes.scenes[name.upper()]
        Debug.log(f"{name.upper()}")

    @staticmethod
    def get_scene(name):
        return Scenes.scenes[name.upper()]

    @staticmethod
    def update_current():
        if Scenes.current_scene:
            Scenes.current_scene.update()

    @staticmethod
    def get_surface(scene=None):
        if scene:
            return Scenes.scenes[scene.upper()].get_surface()
        elif Scenes.current_scene:
            return Scenes.current_scene.get_surface()
        else:
            surf = p.Surface((Settings.get("RESOLUTION")))
            surf.fill((255, 0, 0))
            return surf
