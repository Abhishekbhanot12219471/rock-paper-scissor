import random
print("Winning Rules of the Rock paper scissor game as follows: \n"
	+ "Rock vs paper->paper wins \n"
	+ "Rock vs scissor->Rock wins \n"
	+ "paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
	choice = input("User turn: ")
	while choice != "R" or choice != "P" or choice !="S":
		choice = input("enter valid input: ")

	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	comp_choice = random.randint(1, 3)
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'ROCK'
	elif comp_choice == 2:
		comp_choice_name = 'PAPER'
	else:
		comp_choice_name = 'SCISSOR'

	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name
	if choice == comp_choice:
		print("DRAW=> ", end="")
		result = Draw

		if((choice == 1 and comp_choice == 2) or
		(choice == 2 and comp_choice == 1)):
			print("PAPER  wins => ", end="")
			result = "paper"

		elif((choice == 1 and comp_choice == 3) or
				(choice == 3 and comp_choice == 1)):
			print("ROCK wins =>", end="")
			result = "Rock"
		else:
			print("SCISSOR wins =>", end="")
			result = "scissor"
      
	if result == Draw:
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== *********BOOM YOU WON********* ==>")
	else:
		print("<== YOU LOSE ): ==>")

	print("Do you want to play again? (Y/N)")
	ans = input().lower


	if ans == 'n':
		break

print("Thanks for playing"/n)
print("CREDITS : ABHISHEK BHANOT")

#tommorow i will chnge the program and will show 
#and print if user wins or computerr
