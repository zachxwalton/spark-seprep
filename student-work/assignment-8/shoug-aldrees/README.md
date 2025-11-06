# Assignment 8 - Containerized Motivation Script
**Name:** Shoug Aldrees  
**Course:** CS 351 — Software Engineering Practicum  
**Boston University**

This project includes a simple Python script (`motivation.py`) and a `Containerfile` that builds and runs the script inside a lightweight Python container.

When executed, the script prints a motivational quote to the terminal.

---

## How to Build and Run + Expected Output

To build and run the container using Podman, and see the expected output:

```bash
podman build -t shoug-motivation .
podman run shoug-motivation
```

---

## Expected Output

✨ Here's your motivational quote of the day ✨
Keep going. Everything you need will come to you at the perfect time.
