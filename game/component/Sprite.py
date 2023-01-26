import pygame as p
from game.component.Component import Component
from game.component.Transform import Transform

from util.Assets import Assets


class Sprite(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.image = p.Surface((0, 0))
        self.draw_layer = "DEFAULT"

    def load_image(self, path, alpha=False):
        self.image = Assets.get_image(path, alpha)

    def set_surface(self, surf):
        self.image = surf

    def draw(self, surf):
        surf.blit(self.image, self.owner.transform.get_position_xy())
