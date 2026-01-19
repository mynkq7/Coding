// Syntax of c Program
#include <stdio.h> // Header file for standard input and output functions
#include <stdbool.h>

// Defining the main function - entry point of the program 
int main() { // The code is written inside these curly braces
// Displaying the output on the screen 
    printf("Hello, World!"); 
    return 0; // Ending the program inside main function with a success status 0. 
}

// Variables
#include <stdio.h>
int Variables(){
    // String
    char String[] = "Alphabet";
    // Number/Integer
    int Number = 10;
    // Floating Number
    float Decimal = 10.5;
    bool Boolean = true;
    // Boolean
    // Displaying the Values of variables
    printf("String: %s\n", String);
    printf("Integer: %d\n", Number);
    printf("Float: %f\n", Decimal);
    printf("Boolean: %d\n", Boolean);
    // Ending the variable function program with a success status 0.
    return 0; 
}
