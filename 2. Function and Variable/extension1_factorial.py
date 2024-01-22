"""
File: extension1_factioral.py
Name: Yvonne Chan
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

# This number controls when to stop.
EXIT = -100     # Sentinel Value


def main():
	"""
	This programs will calculates the factorial result
	among user inputs.
	"""
	print('Welcome to stanCode factorial master!')
	"""
	:param: n: int.
	"""
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	if n == EXIT:
		print('------ See ya! ------')
	else:
		while True:
			factorial = 1
			if n == EXIT:
				print('------ See ya! ------')
				break
			else:
				for i in range(1, n + 1):
					factorial = factorial * i
				print('Answer: ' + str(factorial))
				n = int(input('Give me a number, and I will list the answer of factorial: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()