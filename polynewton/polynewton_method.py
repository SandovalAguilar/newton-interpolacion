import numpy as np

class PolyNewton:

    def __init__(self, x_vector, y_vector, length):
        self.x_vector = x_vector
        self.y_vector = y_vector
        self.length = length
        self.x_values = self.calculate_x_values()
        self.coefficients = self.calculate_coefficients()
        self.evaluated_polynomial = self.evaluate_interpolation()

    def calculate_x_values(self):
        self.x_values = np.arange(min(self.x_vector), max(self.x_vector) + 0.1, 0.1)

        return self.x_values

    def calculate_coefficients(self):
        self.coefficients = np.zeros((self.length, self.length))
        self.coefficients[:, 0] = self.y_vector

        for j in range(1, self.length):
            for i in range(self.length - j):
                self.coefficients[i][j] = \
                    (self.coefficients[i + 1][j - 1] - self.coefficients[i]
                     [j - 1]) / (self.x_vector[i + j] - self.x_vector[i])

        return self.coefficients

    def evaluate_interpolation(self):
        self.coefficients = self.coefficients[0, :]
        self.evaluated_polynomial = self.coefficients[self.length - 1]

        for k in range(1, self.length - 1 + 1):
            self.evaluated_polynomial = self.coefficients[self.length - 1 - k] + (
                self.x_values - self.x_vector[self.length - 1 - k]) * self.evaluated_polynomial

        return self.evaluated_polynomial
