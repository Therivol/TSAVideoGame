import pygame as p
from game.object.Object import Object

from game.component.Collider import Collider
from game.component.Sprite import Sprite
from game.component.RigidBody import RigidBody


class Player(Object):
    def __init__(self):
        super().__init__("Player")

        self.sprite = Sprite(self)
        self.sprite.load_image("assets/sprites/player.png", alpha=True)

        self.collider = Collider(self)
        self.collider.set_rect(p.Rect(0, 0, 32, 64), (15, 0))
        self.collider.add_collide_layer("TERRAIN")

        self.rigid_body = RigidBody(self)

        self.transform.set_position((100, 50))

        self.add_component(self.sprite)
        self.add_component(self.collider)
        self.add_component(self.rigid_body)
