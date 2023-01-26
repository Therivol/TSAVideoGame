from pygame.math import Vector2
from game.component.Component import Component


class Transform(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.position = Vector2()
        self.last_position = Vector2()
        self.is_static = False

    def early_update(self):
        self.last_position.update(self.position)

    def set_static(self, static):
        self.is_static = static

    def set_position(self, pos):
        self.position.update(pos)

    def add_position_pos(self, pos):
        self.position += pos

    def set_x(self, x):
        self.position.x = x

    def set_y(self, y):
        self.position.y = y

    def add_x(self, x):
        self.position.x += x

    def add_y(self, y):
        self.position.y += y

    def get_position_xy(self):
        return self.position.x, self.position.y
