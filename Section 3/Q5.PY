# A
import random

roll_dice = random.randint(1, 6)
print(roll_dice)

# B

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper or scissors: ").lower()
computer_choice = random.choice(choices)
print(f"Computer choice {computer_choice}")

if user_choice == computer_choice:
    print("It a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win")
else:
    print("You lose")