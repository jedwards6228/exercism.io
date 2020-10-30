import random


class Robot:

    used_name = []
    name = ''

    def __init__(self):
        self.

    def robot_name(self):
        while len(self.name) < 5:
            while len(self.name) < 2:
                self.name += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            self.name += str(random.randint(0, 9))
            if len(self.name) == 5:
                if self.name in self.used_name:
                    self.name = ''
        self.used_name.append(self.name)
        return self.name
