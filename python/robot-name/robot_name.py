import random


class Robot:
    def __init__(self):
        self.name = self.robot_name()
        self.used_names = []

    def robot_name(self):
        name = ""
        while len(name) < 5:
            while len(name) < 2:
                name = self.add_let(name)
            name = self.add_num(name)
            if len(name) == 5:
                if name in self.used_names:
                    name = ""
        self.used_names.append(name)
        return name

    def add_let(self, name):
        name += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return name

    def add_num(self, name):
        name += str(random.randint(0, 9))
        return name
