import random
import time

print("Welcome to the Ultimate Random Number Generator 3000")
print("Generating a super random number between 1 and 100...\n")

time.sleep(1)
for i in range(3, 0, -1):
    print(f"Calculating randomness in {i}...")
    time.sleep(1)

number = random.randint(1, 100)
print("\nThe random number is...")
time.sleep(1)
print(f"{number}")