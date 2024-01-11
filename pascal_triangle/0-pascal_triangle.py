#!/usr/bin/python3
""" Module for calculating Pascal Triangle """

def pascal_triangle(n):
	"""
	Function for creating a pascal triangle as a list of lists
    n: number of rows
    returns empty list if n <= 0
    """

	triangulo = []

	if n <= 0:
		return triangulo

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
