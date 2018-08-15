from random import randint
player_wins = 0	
computer_wins = 0
winning_score = int(input("Enter the winning score... "))

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")	
	print("......ROCK......")
	print("......PAPER......")
	print("......SCISSORS......")

	player = input("(Enter your choice): ").lower()
	if player == "quit" or player == "q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}")	

	if player == computer:
		print("Its a TIE!")
	elif player == "rock":
		if computer == "scissors":
			print("PLAYER WINS!")
			player_wins += 1
		else:
			print("COMPUTER WINS!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("PLAYER WINS!")
			player_wins += 1
		else:
			print("COMPUTER WINS!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("PLAYER WINS!")
			player_wins += 1
		else:
			print("COMPUTER WINS!")
			computer_wins += 1
	else:
		print("Please enter a valid move!")
	  
if player_wins > computer_wins:
	print("CONGRATS, YOU WON!!!")
elif player_wins == computer_wins:
	print("IT'S A TIE!")
else:
	print("OH NO :( THE COMPUTER WON...")

