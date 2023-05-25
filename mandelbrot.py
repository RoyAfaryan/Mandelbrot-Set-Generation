# mandelbrot.py
from math import log

class Mandelbrot:

	#self.max_iterations = 0
	#self.escape_radius = 2.0

	# constructor
	def __init__(self, max_iterations):
		self.max_iterations = max_iterations
		
	# checks if value is part of mandelbrot set
	def inSet(self, c):
		return self.ratio(c) == 1

	# determines stability of the c value. The closer the value is to one, the more stable it is
	def ratio(self, c: complex):
		return self.escape_count(c)/self.max_iterations

	# finds escape count if c value diverges; otherwise returns max_iterations
	def escape_count(self, c: complex):
		z = 0
		for iteration in range(self.max_iterations):
			z = z ** 2 + c
			if abs(z) > 2:
				return iteration + 1 - log(log(abs(z))) / log(2)
		return self.max_iterations