import random

print("Choose one: rock / paper / scissors")

choices = ["rock", "paper", "scissors"]
player = input("Your choice: ").lower()
computer = random.choice(choices)

print(f"The computer chose: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
elif player in choices:
    print("You lose!")
else:
    print("Invalid choice. Please type rock, paper, or scissors next time.")