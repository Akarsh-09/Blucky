# Calculator

A simple calculator application that provides basic arithmetic and exponentiation operations through both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Power Operation**: Supports the exponentiation (`^`) operation.
- **Operator Precedence**: Correctly handles the order of operations:
  - Exponentiation (`^`) has the highest precedence.
  - Multiplication (`*`) and Division (`/`) have medium-high precedence.
  - Addition (`+`) and Subtraction (`-`) have medium-low precedence.
- **Dual Interfaces**:
  - **CLI**: Quickly evaluate expressions from the terminal with JSON output.
  - **GUI**: An intuitive window-based interface for interactive calculations.
- **Robust Error Handling**: Handles empty expressions, invalid tokens, and insufficient operands.

## Installation

This project is written in Python. Ensure you have Python 3.x installed on your system.

No external dependencies are required as it uses standard Python libraries (`tkinter` for GUI, `json` for output).

## Usage

### Command Line Interface (CLI)

Run the calculator by passing an expression as a string argument to `main.py`.

```bash
python main.py "3 + 5 * 2"
```

**Example Output:**
```json
{
  "expression": "3 + 5 * 2",
  "result": 13
}
```

### Graphical User Interface (GUI)

Launch the interactive GUI by running `gui.py`.

```bash
python gui.py
```

## Supported Operators

| Operator | Description | Precedence |
|----------|-------------|------------|
| `^`      | Exponentiation | High       |
| `*`      | Multiplication | Medium     |
| `/`      | Division       | Medium     |
| `+`      | Addition       | Low        |
| `-`      | Subtraction    | Low        |

## Testing

To verify the functionality of the calculator, you can run the provided test suite:

```bash
python tests.py
```
