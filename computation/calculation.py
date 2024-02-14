
# Calculation Class
class Calculation:

    def __init__(self):
        self.relaxation = 0

    # Add method
    def add(self, x, y):
        return x + y + self.relaxation

    # Subtract method
    def subtract(self, x, y):
        return x - y + self.relaxation
