#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import datetime

def main():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens to you while you're busy making other plans. - John Lennon", 
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "The only impossible journey is the one you never begin. - Tony Robbins",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ]
    
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    
    reset_color = "\033[0m"
    
    print("< Random Quote Generator by Riki <")
    print("=" * 50)
    
    # Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Generated at: {current_time}")
    print()
    
    # Pick random quote and color
    selected_quote = random.choice(quotes)
    selected_color = random.choice(colors)
    
    # Display the quote with color
    print(f"{selected_color}{selected_quote}{reset_color}")
    print()
    
    # Random motivational message
    motivations = [
        "You've got this! =�",
        "Keep pushing forward! =�", 
        "Believe in yourself! P",
        "Today is your day! <",
        "Make it happen! ("
    ]
    
    print(f"=� {random.choice(motivations)}")
    print("=" * 50)

if __name__ == "__main__":
    main()