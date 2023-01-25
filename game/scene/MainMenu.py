from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Assets import Assets
from game.scene.Scene import Scene
from game.scene.Level1 import Level1
from game.scene.LevelSelect import LevelSelect
from gui.element.Button import Button
import pygame as p


class MainMenu(Scene):
    def __init__(self):
        super().__init__("MAIN MENU")

        self.shadow = None

        self.play_button = Button(p.Rect(384, 180, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

        self.quit_button = Button(p.Rect(384, 300, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

    def awake(self):
        self.shadow = p.Surface((232, 224))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(120)

    def update(self):
        if self.play_button.update():
            Scenes.set_scene("LEVEL SELECT")

        if self.quit_button.update():
            Scenes.should_quit = True

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/default.png"), (0, 0))

        surf.blit(self.shadow, (364, 160))

        self.play_button.draw(surf)
        self.quit_button.draw(surf)

        surf.blit(Assets.get_image("assets/ui/play.png", alpha=True), (384, 180))
        surf.blit(Assets.get_image("assets/ui/quit.png", alpha=True), (384, 300))

        return surf
