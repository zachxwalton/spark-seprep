import time, os

snail = "🐌🐌🐌"
length = os.get_terminal_size().columns

for i in range(length * 2):
    print(" " * (i % length) + snail, end="\r")
    time.sleep(0.05)

