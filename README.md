# Smart Calculator

Welcome to the Smart Calculator GitHub project! This Python program is designed to calculate basic mathematical operations while handling common input errors. It's a straightforward interpreter that can be extended or incorporated into larger projects requiring mathematical input processing.

## Features

- **Mathematical Operations**: Supports basic operations like addition, subtraction, multiplication, division, and parentheses for grouping.
- **Error Handling**: Provides feedback for common input errors such as invalid assignments, identifiers, expressions, and unknown variables.
- **Command Support**: Includes commands for help (`/help`) and program exit (`/exit`).

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/smart-calculator.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

Once started, you can input mathematical expressions directly. Below are some usage examples:

```
Input: 8 + 2
Output: 10

Input: 12 / (2 + 4)
Output: 2

Input: 2 ^ 3
Output: Invalid expression

Input: a = 5
Output: Invalid assignment

Input: /help
Output: The program calculates mathematical operations
```

To exit the program, type:

```
/exit
```

## How it Works

The interpreter processes the user input with the following steps:

1. **Input Processing**: Transforms certain symbols to maintain compatibility, like replacing `^` with `**` for exponentiation, which is not implemented and hence flagged as an invalid expression.
2. **Validation**: Before evaluating expressions, it checks for common mistakes such as invalid identifiers, assignments, and unsupported operations.
3. **Evaluation**: If the input passes validation, it's either attempted to be executed (in case of assignments) or evaluated (for expressions) using Python's built-in `exec` and `eval` functions.
4. **Output**: Displays the result of the expression or an error message, depending on the input's validity.

## License

This project is licensed under the [MIT License](LICENSE.txt).
