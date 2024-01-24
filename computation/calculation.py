
class Calculation:

    def __init__(self):
        self.relaxation = 0

    def add(self, x, y):
        return x + y + self.relaxation

    def subtract(self, x, y):
        return x - y + self.relaxation
