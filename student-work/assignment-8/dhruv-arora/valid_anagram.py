#!/usr/bin/env python3
import sys
import json
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def main():
    # Allow running either with two CLI args or a built-in demo
    if len(sys.argv) == 3:
        s, t = sys.argv[1], sys.argv[2]
        result = is_anagram(s, t)
        print(json.dumps({"s": s, "t": t, "is_anagram": result}))
        return

    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccac", False),
        ("", "", True),
    ]
    out = [{"s": s, "t": t, "is_anagram": is_anagram(s, t)} for s, t, _ in tests]
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()


