import numpy as np

def calculate_differences(x_vector, y_vector):
    size = y_vector.size
    coefficients = np.zeros((size, size))


def generate_interpolation(coefficients, x_vector, x):
    pass

def polynewton_method(x_vector, y_vector, x):
    coefficients = calculate_differences(x_vector, y_vector)
    p_result = generate_interpolation(coefficients, x_vector, x)

    return p_result
    