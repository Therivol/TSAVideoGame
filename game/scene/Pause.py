from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Assets import Assets
from game.scene.Scene import Scene
from game.scene.Level import Level
from game.scene.LevelSelect import LevelSelect
from gui.element.Button import Button
import pygame as p


class Pause(Scene):
    def __init__(self):
        super().__init__("PAUSE")

        self.shadow = None

        self.play_button = Button(p.Rect(384, 180, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

        self.quit_button = Button(p.Rect(384, 300, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.play_button.update():
            Scenes.set_scene("LEVEL")

        if self.quit_button.update():
            Scenes.set_scene("LEVEL SELECT")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))

        surf.blit(Scenes.get_surface("LEVEL"), (0, 0))

        surf.blit(self.shadow, (334, 130))

        self.play_button.draw(surf)
        self.quit_button.draw(surf)

        surf.blit(Assets.get_image("assets/ui/play.png", alpha=True), (384, 180))
        surf.blit(Assets.get_image("assets/ui/quit.png", alpha=True), (384, 300))

        return surf
