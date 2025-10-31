import random

foods = ['apple', 'banana', 'yogurt', 'rice', 'bread', 'nothing']

random_choice = random.choice(foods)
print("What should I eat for breakfast today?")

if random_choice == "nothing":
    print(" Maybe skip breakfast today!")
else:
    print(f"{random_choice.capitalize()} sounds good!")

