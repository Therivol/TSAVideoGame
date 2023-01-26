from game.component.Transform import Transform
from game.component.Instance_ID import InstanceID
from util.Debug import Debug


class Object:
    def __init__(self, name):
        self.name = name

        self.components = {}
        self.is_queued_for_removal = False

        self.transform = Transform(self)

        self.instance_ID = InstanceID(self)

        self.add_component(self.transform)
        self.add_component(self.instance_ID)

    def awake(self):
        for component in self.components.values():
            component.awake()

    def start(self):
        for component in self.components.values():
            component.start()

    def early_update(self):
        for component in self.components.values():
            component.early_update()

    def update(self):
        for component in self.components.values():
            component.update()

    def late_update(self):
        for component in self.components.values():
            component.late_update()

    def add_component(self, component):
        self.components[type(component)] = component

    def remove_component(self, component_type):
        if component_type in self.components:
            del self.components[component_type]
        else:
            Debug.log_error(f"Component{component_type} not found in {self.name}")
            return None

    def get_component(self, component_type):
        if component_type in self.components:
            return self.components[component_type]
        else:
            Debug.log_error(f"Component{component_type} not found in {self.name}")
            return None

    def queue_for_removal(self):
        self.should_be_removed = True

    def get_id(self):
        return self.instance_ID.get()
