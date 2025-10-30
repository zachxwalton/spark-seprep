import random

def main():
    quotes = [
        "Keep going, you're doing great!",
        "Every expert was once a beginner.",
        "Don't watch the clock; do what it does — keep moving.",
        "Dream big, work hard, stay humble.",
        "Small steps every day lead to big results."
    ]
    print("Motivational Quote")
    print(random.choice(quotes))

if __name__ == "__main__":
    main()