import random

computer = ["rock", "paper", "scissors"]

player = input("Rock, paper, scissors shoot! ")

computer_choice = random.choice(computer)

print(computer_choice)
if player == computer_choice:
    print("its a draw!")

elif player == "rock" and computer_choice == "scissors":
    print("player wins!")

elif player == "scissors" and computer_choice == "paper":
    print("player wins!")

elif player == "paper" and computer_choice == "rock":
    print("player wins!")

else:
    print("Computer wins")
