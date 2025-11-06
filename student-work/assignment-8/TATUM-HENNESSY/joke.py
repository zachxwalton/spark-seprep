import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "What's a programmer's favorite hangout place? Foo Bar.",
    "Why did the programmer quit his job? Because he didn't get arrays."
]

print("\nHere's a random programming joke:\n")
print(jokes[random.randint(0, len(jokes)-1)])
print()
