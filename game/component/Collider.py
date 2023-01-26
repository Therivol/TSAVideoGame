from dataclasses import dataclass

import pygame as p
from pygame.math import Vector2
from game.component.Transform import Transform
from game.component.Component import Component
from util.Debug import Debug


@dataclass
class Manifold:
    colliding = False
    other = None


class Collider(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.layer = "DEFAULT"
        self.collide_layers = []
        self.is_trigger = False
        self.manifold = Manifold()

        self.rect = p.Rect((0, 0), (0, 0))
        self.offset = Vector2()

    def set_layer(self, layer):
        self.layer = layer

    def add_collide_layer(self, *args):
        for layer in args:
            self.collide_layers.append(layer)

    def intersects(self, other):

        if type(other) == Collider:
            rect_1 = self.get_rect()
            rect_2 = other.get_rect()

            if rect_1.colliderect(rect_2):
                self.manifold.colliding = True
                self.manifold.other = other

        else:
            Debug.log_error(f"{other} not of type BoxCollider")

        return self.manifold

    def resolve_overlap(self, manifold):
        transform = self.owner.get_component(Transform)
        if transform.is_static:
            return

        rect_1 = self.get_rect()
        rect_2 = manifold.other.get_rect()

        resolve = 0
        x_diff = rect_1.centerx - rect_2.centerx
        y_diff = rect_1.centery - rect_2.centery

        if abs(x_diff) > abs(y_diff):
            # colliding from right
            if x_diff > 0:
                resolve = rect_2.right - rect_1.left
            elif x_diff < 0:
                resolve = -(rect_1.right - rect_2.left)

            transform.add_position_pos((resolve, 0))

        else:
            if y_diff > 0:
                resolve = rect_2.bottom - rect_1.top
            elif y_diff < 0:
                resolve = -(rect_1.bottom - rect_2.top)

            transform.add_position_pos((0, resolve))

    def reset_manifold(self):
        self.manifold.colliding = False
        self.manifold.other = None

    def set_rect(self, rect, offset):
        self.rect = rect
        self.offset.update(offset)
        self.set_position()

    def get_rect(self):
        self.set_position()
        return self.rect

    def set_position(self):
        pos = self.owner.transform.get_position_xy()
        pos += self.offset
        self.rect.topleft = pos

    def update(self):
        self.set_position()
