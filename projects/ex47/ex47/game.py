class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
#        return  direction if direction in self.paths else None

    def add_paths(self, paths):
        self.paths.update(paths)
