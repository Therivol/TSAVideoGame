import sys

import pygame as p

from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets
from util.Window import Window

from game.scene.MainMenu import MainMenu
from game.scene.LevelSelect import LevelSelect
from game.scene.Level import Level
from game.scene.Pause import Pause


class Game:
    def __init__(self):
        p.init()
        Time.awake()
        Settings.load()

        self.should_close = False

    def start(self):
        Window.display = p.display.set_mode(Settings.get("RESOLUTION"), p.RESIZABLE)
        p.display.set_caption(Settings.get("TITLE"))
        p.display.set_icon(Assets.get_image("assets/tiles/1.png"))
        Window.resize(Settings.get("WINDOW SIZE"))

        Scenes.add_scene(MainMenu())
        Scenes.add_scene(LevelSelect())
        Scenes.add_scene(Level())
        Scenes.add_scene(Pause())

        Scenes.set_scene("MAIN MENU")

    def poll_events(self):
        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT or Window.should_close:
                self.quit()

            if ev.type == p.VIDEORESIZE:
                Window.resize((ev.w, ev.h))

        if Input.get_key_down(p.K_F11):
            Window.full_screen = not Window.full_screen
            if Window.full_screen:
                Window.display = p.display.set_mode(Window.monitor_size(), p.FULLSCREEN)
                Window.resize(Window.monitor_size())
            else:
                Window.display = p.display.set_mode(Settings.get("WINDOW SIZE"), p.RESIZABLE)

    @staticmethod
    def calculate_dt():
        Time.calculate_dt()

    def early_update(self):
        pass

    def update(self):
        Scenes.update_current()

    def late_update(self):
        pass

    def draw(self):
        Window.draw()

    def quit(self):
        Settings.save()

        self.should_close = True
        p.quit()
        sys.exit()
