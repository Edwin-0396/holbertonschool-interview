#!/usr/bin/python3
"""
def pascal_triangle(n): returns a list of lists of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""

def pascal_triangle(n):
	"""
	Function that calculates a pascal triangle based on input 'n'
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
