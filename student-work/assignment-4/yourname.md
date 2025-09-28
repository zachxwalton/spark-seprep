# Anson Zhu 

Hi, my name is Anson Zhu and my favorite programming language is Java because it's the first programming language that I was exposed to.

## Example code

'''

public class MultiplicationTable {
    public static void main(String[] args) {
        int limit = 10;
        for (int i = 1; i <= limit; i++) { // Outer loop for the first multiplier
            for (int j = 1; j <= limit; j++) { // Inner loop for the second multiplier
                System.out.printf("%4d", (i * j)); // Format for alignment
            }
            System.out.println();
        }
    }
}

'''

### Code explanation

This Java program prints a 10x10 multiplication table using nested loops. To run it, save the code to a file called MultiplicationTable.java, then compile it with javac MultiplicationTable.java and run it with java MultiplicationTable. You need to have Java installed on your system.
