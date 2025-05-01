import numpy as np

class Calculator:
    def add(self, a, b):
        return np.add(a, b)

    def subtract(self, a, b):
        return np.subtract(a, b)

    def multiply(self, a, b):
        return np.multiply(a, b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return np.divide(a, b)
