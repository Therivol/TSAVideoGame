import Component


class InstanceID(Component):
    count = 0

    def __init__(self, owner):
        super().__init__(owner)

        self.id = self.count
        InstanceID.count += 1

    def get(self):
        return self.id