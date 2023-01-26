

class Component:
    def __init__(self, owner):
        self.owner = owner

    def awake(self):
        pass

    def start(self):
        pass

    def early_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass
