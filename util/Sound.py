import pygame as p


class sounds:
    @staticmethod
    def soundEx(Effect):
        effect = p.mixer.Sound(Effect)
        p.mixer.Sound.play(effect)
        p.mixer.stop


