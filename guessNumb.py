import random

# Define # of allowed attempts and define secret 
# number with randint function #
attempts = 5
secret_number = random.randint(1,100)

print("You get 5 attempts to guess the number.")

# Prompts user to enter number. If incorrect value
# is entered the a the attempt loop loses 1 until
# the loop runs out of attempts to declare failure #
for attempt in range(attempts):
	try:
		print()
		print("Take a guess!!!")
		guess = int(input())
		if guess < secret_number:
			print("Try higher...")
		elif guess > secret_number:
			print("Try lower...")
		elif guess == secret_number:
			print()
			print("You guessed it! The numer was",secret_number)
			print("You guessed it in",attempts,"attempts")
			break
	
	# Handles error if letter or special character
	# is entered instead of required number format #	
	except ValueError:
		print("There was an error, please check your input")
		print("You keyed in a letter or special character", \
			"when a number value was expected")

# If the user fails to identify the selected
# random number this function notifies that
# the number was not accurately guessed #
if guess != secret_number:
	print()
	print("Sorry to inform you that you suck at this game.")
	print("The secret number was",secret_number)
	print("Better Luck next time!!!")