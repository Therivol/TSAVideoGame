from game.component.Component import Component
from util.Time import Time


class RigidBody(Component):
    def __init__(self, owner):
        super().__init__(owner)

    def update(self):
        self.owner.transform.add_position_pos((0, Time.delta() * 200))
