# Armaan Suden

I am a DS major and my favourite programming language is python because it is the simplest in my opinion. 

## Example Code
```python
import random

def roll_dice(n=2):
    rolls = [random.randint(1, 6) for _ in range(n)]
    return rolls, sum(rolls)

dice, total = roll_dice(2)
print(f"You rolled a {dice} → Total = {total}")
```
### Code Explanation:
This is a python code which rolls a dice, it uses the random function from python to do this.
