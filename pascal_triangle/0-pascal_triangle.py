#!/usr/bin/python3
"""
def pascal_triangle(n): returns a list of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    triangulo = []

    for i in range(n):
        fila = []
        for j in range(i + 1):
            if j == 0 or j == i:
                fila.append(1)
            else:
                # Usamos la fórmula del coeficiente binomial
                coeficiente_binomial = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
                fila.append(coeficiente_binomial)
        triangulo.append(fila)

    return triangulo
