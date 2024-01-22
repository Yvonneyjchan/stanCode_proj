"""
File: weather_master.py
Name: Yvonne Chan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This number controls when to stop.
EXIT = -100     # Sentinel Value


def main():
	"""
	This programs finds the highest, the lowest, the average and cold day
	among user inputs.
	"""
	print('stanCode "Weather Master 4.0"!')
	"""
	:param: data: int.
	"""
	data = int(input('Next Temperature: (or '+str(EXIT) +' to quit)? '))
	if data == EXIT:
		print('No temperature were entered.')
	else:
		maximum = data
		minimum = data
		counts = 1
		total = data
		average = total / counts
		cold = 0
		if data < 16:
			cold = cold + 1  # check the first input whether is the cold day.
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT) +' to quit)? '))
			if data == EXIT:
				break
			elif data > maximum:
				maximum = data
			elif data < minimum:
				minimum = data
			total = average * counts + data
			counts = counts + 1
			average = total / counts
			if data < 16:
				cold = cold + 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
