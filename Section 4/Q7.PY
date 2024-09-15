import random

friends = input("Enter names of friends: ").split(",")

winner = random.choice(friends)

print(f"The winner is {winner}")