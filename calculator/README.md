# Minecraft Scientific Calculator

A scientific calculator application that provides basic arithmetic, exponentiation, and scientific operations through both a Command Line Interface (CLI) and a Minecraft-inspired Graphical User Interface (GUI).

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Power Operation**: Supports exponentiation (`^`).
- **Scientific Functions**: Includes trigonometric functions (`sin`, `cos`, `tan`), logarithms (`log` for base 10, `ln` for natural log), and square root (`sqrt`).
- **Operator Precedence**: Implements standard mathematical order of operations:
  - **Highest**: Unary operators (`sin`, `cos`, `tan`, `log`, `ln`, `sqrt`)
  - **High**: Exponentiation (`^`)
  - **Medium**: Multiplication (`*`) and Division (`/`)
  - **Low**: Addition (`+`) and Subtraction (`-`)
- **Dual Interfaces**:
  - **CLI**: Fast expression evaluation via the terminal with JSON formatted output.
  - **GUI**: A stylized Minecraft-inspired interface with a virtual keypad and a dedicated **Calculation History** feature.
- **Calculation History (GUI only)**:
  - View a log of all recent calculations in the current session.
  - Toggle the history panel to save screen space.
  - Clear the entire history with a single click.
- **Robust Error Handling**: Gracefully handles empty expressions, invalid tokens, and mismatched parentheses.

## Installation

This project is written in Python. Ensure you have Python 3.x installed.

No external dependencies are required; it uses standard Python libraries (`tkinter` for GUI, `json` for CLI output).

## Usage

### Command Line Interface (CLI)

Evaluate expressions by passing them as arguments to `main.py`.

```bash
python main.py "3 + 5 * 2"
python main.py "sin 90"
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

### Binary Operators
| Operator | Description | Precedence |
|----------|-------------|------------|
| `^`      | Exponentiation | High       |
| `*`      | Multiplication | Medium     |
| `/`      | Division       | Medium     |
| `+`      | Addition       | Low        |
| `-`      | Subtraction    | Low        |

### Unary Operators
| Operator | Description | Precedence |
|----------|-------------|------------|
| `sin`    | Sine (degrees) | Highest    |
| `cos`    | Cosine (degrees) | Highest    |
| `tan`    | Tangent (degrees) | Highest    |
| `log`    | Logarithm (base 10) | Highest    |
| `ln`     | Natural Logarithm | Highest    |
| `sqrt`   | Square Root | Highest    |

## Testing

Verify the calculator's logic by running the test suite:

```bash
python tests.py
```
