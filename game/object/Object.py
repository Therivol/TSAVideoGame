from util.Debug import Debug


class Object:
    def __init__(self, name):
        self.name = name
        self.components = {}
        self.should_be_removed = False

    def awake(self):
        pass

    def start(self):
        pass

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
