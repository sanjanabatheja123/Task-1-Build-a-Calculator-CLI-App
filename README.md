# Simple Python Calculator

This is a simple command-line calculator program written in Python. It supports basic arithmetic operations like addition, subtraction, multiplication, and division.

---

## Features

- Addition (`add`)
- Subtraction (`sub`)
- Multiplication (`mul`)
- Division (`div`)
- Loop-based interface
- Input validation
- Graceful exit with `"exit"`

---

## Code Flow

1. Start the program.

2. Loop begins:
    a. Prompt user to enter an operation: add, sub, mul, div, or exit.

3. If user enters 'exit':
    → Exit the loop and end the program.

4. If operation is valid (add/sub/mul/div):
    a. Prompt user to input two numbers.
    b. Based on the selected operation:
        - Call the corresponding function (add, sub, mul, div).
        - Display the result using print().

5. If operation is invalid:
    → Show error message and prompt again.

6. Repeat the loop until user enters 'exit'.
