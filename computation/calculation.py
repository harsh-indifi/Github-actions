
class Calculation:

    def __init__(self):
        self.relaxation = 0

    # Addition method
    def add(self, x, y):
        return x + y + self.relaxation

    # Subtract method
    def subtract(self, x, y):
        return x - y + self.relaxation
