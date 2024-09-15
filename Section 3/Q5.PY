# A
import random

roll_dice = print(random.randint(1, 6))

# B

choice = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter rock, paper or scissors").lower()
computer_choice = random.choice(choice)
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