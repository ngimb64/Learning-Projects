import math

if __name__ == '__main__':

	print('This program will help you understand pizza logistics!!!')

	try:
		# Prompts users to enter desired pizza 
		# diameter and what that size would cost #
		diameter = float(input('Enter a diameter: '))
		price = float(input('Enter a price: '))
		
		# Calculates the area for 
		# square and circle pizza #
		square_area = diameter**2
		round_area = (diameter//2)**2 * math.pi 

		print()
		print('If the pizza is sicilian then the area is',square_area)
		print('If the pizza is round then the area is',round_area)

		# Calculates the area difference between 
		# the square and circle pizzas #
		difference = square_area - round_area
		print()
		print('The difference of both areas is: ',difference)
		print()

		# Prints the cost for both 
		# pizza shapes #
		print('The cost in per square inch of each pizza: ')
		print('Square: ',price/square_area)
		print('Round: ',price/round_area)



	except ValueError as e:
		print()
		print('There was an error from your input')
		print('Please make sure you enter a number')