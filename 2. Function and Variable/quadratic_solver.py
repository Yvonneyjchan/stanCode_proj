"""
File: quadratic_solver.py
Name: Yvonne Chan
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program finds the roots of the quadratic equation
	among user inputs of the coefficient.
	"""
	print('stanCode Quadratic Solver!')
	print('Find the roots of the quadratic equation: ax^2 + bx + c = 0')
	"""
	:param a: int, the first coefficient of quadratic equation and cannot be zero.
	:param b: int, the second coefficient of quadratic equation.
	:param c: int, the third coefficient of quadratic equation.
	"""
	while True:
		a = int(input('Enter a: '))
		if a == 0:
			print('"a" cannot be zero.')
		else:
			break
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	d = b*b - 4*a*c   # discriminant

	if d < 0:
		print('No real roots')
	elif d == 0:
		sqrt = math.sqrt(d)
		x1 = (-b + sqrt) / (2 * a)
		print('One root: '+str(x1))
	else:
		sqrt = math.sqrt(d)
		x1 = (-b + sqrt) / (2 * a)
		x2 = (-b - sqrt) / (2 * a)
		print('Two roots: ' + str(x1) + ',' + str(x2))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
