import random


class Robot:
    used_name = set()
    name = ''

    def __init__(self):
        self.reset()

    def robot_name(self):
        while len(self.name) < 5:
            while len(self.name) < 2:
                self.name += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            self.name += str(random.randint(0, 9))
            if len(self.name) == 5 and len(self.used_name) > 0:
                if self.name in self.used_name:
                    self.name = ''
        self.used_name.add(self.name)
        return self.name

    def reset(self):
        self.name = ''
        self.robot_name()
        return
