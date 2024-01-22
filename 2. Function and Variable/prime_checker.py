"""
File: prime_checker.py
Name: Yvonne Chan
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

# This number controls when to stop.
EXIT = -100     # Sentinel Value


def main():
	"""
	This program checks the prime number.
	"""
	print('Welcome to the prime checker!')
	"""
	:param: data: int.
	"""
	data = int(input('n: '))
	if data == EXIT:
		print('Have a good one!')
	else:
		while True:
			if data == EXIT:
				print('Have a good one!')
				break
			else:
				for i in range(2, data):
					if data % i == 0:
						print(str(data) + ' is not a prime number.')
						break
					else:
						print(str(data) + ' is a prime number.')
			data = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
