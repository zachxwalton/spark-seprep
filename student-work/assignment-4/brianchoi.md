# Brian Choi
Hi, my name is Brian Choi, and my favorite programming language is C++ because it was the first programming language I learned.

## Example code
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    std::cout << "Hello, " << name << "!" << std::endl;
    std::cout << "Have a beep!\a" << std::endl;

    return 0;
}
```
### Code explanation
This basic C++ program asks the user for their name, then prints a greeting to standard output. It also tries to emit a beep by writing the `\a` (ASCII BEL character) to the console.

To run this program, save it to a file, compile it with a C++ compiler such as `g++` or `clang++`, and then execute the resulting binary. 
```bash
g++ helloBeep.cpp -o helloBeep
./helloBeep
```

