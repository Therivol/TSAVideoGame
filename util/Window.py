import pygame as p
import sys

from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets

from game.scene.MainMenu import MainMenu
from game.scene.LevelSelect import LevelSelect
from game.scene.Level import Level
from game.scene.Pause import Pause


class Window:
    p.init()

    shouldClose = False
    display = None
    view = None
    view_destination = (0, 0)
    fullscreen = False
    monitor_size = [p.display.Info().current_w, p.display.Info().current_h]
    
    @staticmethod
    def awake():
        Window.display = p.display.set_mode(Settings.get("RESOLUTION"), p.RESIZABLE)
        p.display.set_caption(Settings.get("TITLE"))
        p.display.set_icon(Assets.get_image("assets/tiles/1.png"))
        Window.resize(Settings.get("WINDOW SIZE"))

        Scenes.add_scene(MainMenu())
        Scenes.add_scene(LevelSelect())
        Scenes.add_scene(Level())
        Scenes.add_scene(Pause())

    @staticmethod
    def start():
        Scenes.set_scene("MAIN MENU")

    @staticmethod
    def poll_events():
        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT:
                Window.quit()

            if ev.type == p.VIDEORESIZE:
                Window.resize((ev.w, ev.h))

        if Input.get_key_down(p.K_F11):
            Window.fullscreen = not Window.fullscreen
            if Window.fullscreen:
                Window.display = p.display.set_mode(Window.monitor_size, p.FULLSCREEN)
                Window.resize(Window.monitor_size)
            else:
                Window.display = p.display.set_mode(Settings.get("WINDOW SIZE"), p.RESIZABLE)

    @staticmethod
    def early_update():
        pass

    @staticmethod
    def update():
        Scenes.update_current()

    @staticmethod
    def late_update():
        pass

    @staticmethod
    def draw():

        Window.view.blit(p.transform.scale(Scenes.get_surface(), Window.view.get_size()), (0, 0))

        Window.display.blit(Window.view, Window.view_destination)

        p.display.update()

    @staticmethod
    def quit():
        Settings.save()

        Window.shouldClose = True
        p.quit()
        sys.exit()

    @staticmethod
    def resize(size):
        aspect = Settings.get("ASPECT RATIO")
        if size[1] * aspect > size[0]:
            Window.view = p.Surface((size[0], size[0] / aspect))
        else:
            Window.view = p.Surface((size[1] * aspect, size[1]))

        Window.view_destination = (Window.display.get_width() / 2 - Window.view.get_width() / 2,
                                 Window.display.get_height() / 2 - Window.view.get_height() / 2)

    @staticmethod
    def calculate_dt():
        Time.calculate_dt()
