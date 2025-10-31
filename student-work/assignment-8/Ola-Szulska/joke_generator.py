#!/usr/bin/env python3
import random

def get_random_joke():
    jokes = [
        "Why did the math book look so sad? Because it had too many problems!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why couldn't the bicycle stand up by itself? It was two tired!",
        "Why did the coffee file a police report? It got mugged!",
        "What do you call a cow with no legs? Ground beef!"
    ]
    return random.choice(jokes)

def main():
    print("Welcome to the Random Joke Generator")
    print("=" * 40)
    print(get_random_joke())
    print("=" * 40)

if __name__ == "__main__":
    main()
