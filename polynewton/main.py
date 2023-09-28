import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

# Custom modules
import polynewton_method as pm

# Numerical validation
def verify_int_input():
    is_integer = False

    while not is_integer:
        try:
            value = int(input())
            is_integer = True
            if value <= 0:
                is_integer = False
                print("Ingrese un valor numerico valido (entero mayor o igual a uno):")
        except ValueError:
            print("Ingrese un valor numerico valido (entero mayor o igual a uno):")
            is_integer = False
        
    return value

def verify_float_input():
    is_numeric = False

    while not is_numeric:
        try:
            value = float(input())
            is_numeric = True
        except ValueError:
            print("Ingrese un valor numerico valido:")
            is_numeric = False
        
    return value

# Fill vectors
def fill_vector(number_points):
    temp_vector = np.zeros(number_points)
    for i in range(number_points):
        temp_vector[i] = verify_float_input()

    return temp_vector

# Generate plot
def draw_plot(newton_poly):
    plt.figure(figsize = (9, 5))
    plt.plot(newton_poly.x_vector, newton_poly.y_vector, 'bo')
    plt.plot(newton_poly.x_values, newton_poly.evaluated_polynomial)
    plt.savefig("polynewton_plot")

# CLI menu
def menu():
    control = True

    while(control):
        os.system('cls||clear')

        print("===        Analisis Numerico: Proyecto III         ===")
        print("===  Interpolacion Polinomica de Newton en Python  ===")
        print("------------------------------------------------------")
        
        print("Ingrese el numero de nodos a interpolar:")
        nodes = verify_int_input()

        print("Ingrese el vector X (presione enter por cada elemento):")
        x_vector = fill_vector(nodes)
        
        print("Ingrese el vector Y:")
        y_vector = fill_vector(nodes)
        
        newton_poly = pm.PolyNewton(x_vector, y_vector, nodes)

        print("Las diferencias divididas son:")
        print(newton_poly.calculate_coefficients())

        print("Los puntos evaluados son:")
        print(newton_poly.evaluate_interpolation())

        print("Grafico creado satisfactoriamente en la carpeta raiz.")
        draw_plot(newton_poly)

        print("¿Desea ingresar otro conjunto de nodos? [S/N]:")
        opcion = input()
        if opcion.upper() == 'S':
            control = True
        elif opcion.upper() == 'N':
            control = False
        else:
            print("Opcion incorrecta. Ingrese una opcion valida.")
            input("Presione cualquier tecla para continuar...")

def main():
    menu()

if __name__ == '__main__':
    main()


