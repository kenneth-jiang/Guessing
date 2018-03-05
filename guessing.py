from random import randint

cont = "y"

while cont == "y":
	random_number = randint(1, 10)
	guess = int(input("Pick a number from 1-10: "))
	while random_number != guess:
		if guess > random_number:
			print("Your guess is too high!")
		elif guess < random_number:
			print("Your guess is too low!")
		guess = int(input("Try again: "))
	print(f"Correct the number was {guess}")
	cont = input("Do you want to play again?: y/n ")
	while ((cont != "y") and (cont != "n")):
		cont = input("Do you want to play again?: y/n ")
	if cont == "n":
		print("Goodbye!")
