# Calculator

A simple calculator application that provides basic arithmetic and bitwise XOR operations through both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Bitwise Operation**: Supports the XOR (`^`) operation.
- **Operator Precedence**: Correctly handles the order of operations:
  - Multiplication (`*`) and Division (`/`) have the highest precedence.
  - Addition (`+`) and Subtraction (`-`) have medium precedence.
  - XOR (`^`) has the lowest precedence.
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
| `*`      | Multiplication | High       |
| `/`      | Division       | High       |
| `+`      | Addition       | Medium     |
| `-`      | Subtraction    | Medium     |
| `^`      | Bitwise XOR    | Low        |

## Testing

To verify the functionality of the calculator, you can run the provided test suite:

```bash
python tests.py
```
