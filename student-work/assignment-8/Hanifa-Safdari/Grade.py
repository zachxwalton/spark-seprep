# Grade.py

# Ask user for input and convert to integer
grade = int(input("Enter your grade (0-100): "))

# Check the grade range and print message
if grade >= 90:
    print("Excellent! You got an A.")
elif grade >= 80:
    print("Great job! You got a B.")
elif grade >= 70:
    print("Good job! You got a C.")
elif grade >= 60:
    print("You passed with a D.")
else:
    print("You need to repeat the course. You got an F.")
