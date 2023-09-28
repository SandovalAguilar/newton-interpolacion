import numpy as np

class PolyNewton:

    def __init__(self, x_vector, y_vector, length, x_values):
        self.x_vector = x_vector
        self.y_vector = y_vector
        self.length = length
        self.x_values = x_values
        self.coefficients = self.calculate_coefficients()
        self.evaluated_polynomial = self.evaluate_interpolation()

    def calculate_coefficients(self):
        coefficients = np.zeros((self.length, self.length))
        coefficients[:, 0] = self.y_vector

        for j in range(1, self.length):
            for i in range(self.length - j):
                self.coefficients[i][j] = \
                    (self.coefficients[i + 1][j - 1] - self.coefficients[i]
                     [j - 1]) / (self.x_vector[i + j] - self.x[i])

        return coefficients

    def evaluate_interpolation(self):
        grade = self.length - 1 
        poly = self.coefficients[grade]
        
        for k in range(1, grade + 1):
            poly = self.coefficients[grade - k] + (self.x_values - self.x_vector[grade - k]) * poly

        return poly
