# Jacky Lin
My favorite programming language right now is Python due to it's sheer versatility and how it was built with the idea of readability. The other programming language I like is Rust due to how unique it is and it's growing applications in industry (its a pain to code in this language however.)

```
import random
answers = ["Absolutely.", "Lol, no.", "Ask again after coffee.", "It depends™.", "Yes, but you'll regret it.", "404: answer not found."]
print("Roast-8-Ball: type "bye" to quit.")

while True:
    q = input("Ask a yes/no question:\n> ")
    if q.strip().lower() == "bye"
        print("👋 Bye.")
        break
    if not q.strip()
        print("Did you forget your question?")
        continue
    print("Sarcastic 8-Ball says:", random.choice(answers))

```

### Code Explanations
This script lets you repeatedly ask a yes/no question and get a random, sarcastic reply until you type bye to quit. 

It uses Python’s built-in random module so no extra installs needed.

To run from the terminal: copy the code into sarcastic_8ball.py file and run it with:

macOS/Linux: python3 roast_8ball.py

Windows: python roast_8ball.py

You need to have Python installed. See [install Python](https://www.python.org/downloads/)

[Python documentation](https://docs.python.org/3/)



You’ll see a prompt; type your question, press Enter, and keep going. Type bye to exit. 

You can rig the responses by editing the answers list in the file.

