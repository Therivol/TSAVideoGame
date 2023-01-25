from util.Window import Window
import pygame as p
from util.Time import Time
from util.Settings import Settings


if __name__ == "__main__":
    Time.awake()
    Settings.load()

    window = Window()
    window.awake()
    window.start()

    while not window.shouldClose:
        window.calculate_dt()
        window.poll_events()
        window.early_update()
        window.update()
        window.late_update()
        window.draw()
