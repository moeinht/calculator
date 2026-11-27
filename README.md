# Python Modular Calculator

A command-line calculator built with Python. This project supports basic mathematical operations, previous calculation results, calculation history, and history management commands.

## Features

- Basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Exponentiation (`**`)
  - Modulo (`%`)
- Use `ans` to reference the previous calculation result.
- View calculation history.
- Clear calculation history.
- Undo the last calculation.
- Error handling for invalid operations and division by zero.
- Modular project structure.

## Project Structure

```text
calculator/
│
├── main.py
├── operations.py
├── calculator.py
├── input_handler.py
└── history.py
```

| File               | Description                                        |
| ------------------ | -------------------------------------------------- |
| `main.py`          | Main program loop and application state management |
| `operations.py`    | Defines supported mathematical operations          |
| `calculator.py`    | Handles calculation logic and `ans` parsing        |
| `input_handler.py` | Receives and validates user input                  |
| `history.py`       | Displays calculation history                       |

## Requirements

- Python 3.8 or newer
- No external dependencies

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd calculator
```

Run the program:

```bash
python main.py
```

## Usage

Enter two numbers and an operation when prompted.

Example:

```text
Enter first number exit / history / clear / undo: 10
Enter operation (+, -, /, *, %, **): +
Enter second number: 5

15.0
```

### Using `ans`

Use `ans` to reference the result of your previous calculation.

```text
10 + 5 = 15

ans * 2 = 30
```

### Available Commands

| Command   | Description                    |
| --------- | ------------------------------ |
| `history` | Displays previous calculations |
| `clear`   | Clears calculation history     |
| `undo`    | Removes the last calculation   |
| `exit`    | Exits the program              |

## Example

```text
10 + 5 = 15
20 * 2 = 40
ans + 10 = 50

history

1. 10 + 5 = 15.0
2. 20 * 2 = 40.0
3. ans + 10 = 50.0

undo

Last calculation undone!
```

## Error Handling

The calculator handles common errors, including:

- Invalid mathematical operators
- Missing input values
- Using `ans` before a calculation has been performed
- Division by zero

## Concepts Practiced

This project was built to practice Python programming concepts:

- Functions
- Dictionaries
- Lambda functions
- Conditional statements
- Loops
- Exception handling
- Modules and imports
- Lists and dictionaries
- State management
- Code refactoring

## Future Improvements

- Persistent history using JSON files
- Unit testing
- More mathematical operations
- Improved input validation
- A graphical user interface

---

_Built as a Python learning project._
