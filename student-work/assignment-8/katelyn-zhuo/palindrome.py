#!/usr/bin/env python3

def palindrome(x):
    if x > 0 and x <= 2**31 - 1:
        return str(x) == str(x)[::-1]
    else:
        return False

if __name__ == "__main__":
    # Example input — you can change this number
    number = 121
    result = palindrome(number)

    if result:
        print(f"{number} is a palindrome!")
    else:
        print(f"{number} is NOT a palindrome.")
