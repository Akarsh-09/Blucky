# Blucky - Personal Agentic AI

Blucky is a personal Agentic AI designed to interact with a local file system. It can perform tasks such as listing directories, reading files, writing to files, and executing Python scripts, all guided by a Large Language Model (LLM).

## 🚀 Features

- **File System Interaction**:
    - List files and directories.
    - Read file contents (with truncation for large files).
    - Create or update files.
    - Execute Python files with optional arguments.
- **Agentic Workflow**: Uses a loop to plan and execute function calls to achieve a user's goal.
- **LLM Integration**: Powered by Google's Gemini models via the `google-genai` SDK.
- **Integrated Example**: Includes a fully functional `calculator` sub-project to demonstrate the agent's ability to run and test code.

## 📁 Project Structure

```text
.
├── main.py              # Entry point: manages the LLM loop and tool configuration
├── call_function.py     # Dispatcher: maps LLM tool calls to Python functions
├── prompts.py           # System instructions for the AI agent
├── config.py            # Global configuration (e.g., character limits, iteration limits)
├── pyproject.toml       # Project dependencies and metadata
├── tests.py             # Tests for the agent's core tools
├── functions/           # Implementation of agent tools
│   ├── get_file_info.py
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/          # An example project for the agent to interact with
    ├── main.py          # CLI interface for the calculator
    ├── gui.py           # GUI interface for the calculator
    ├── tests.py         # Unit tests for the calculator
    └── pkg/             # Calculator core logic
        ├── calculator.py
        └── render.py
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Akarsh-09/Blucky
   cd Blucky
   ```

2. **Install dependencies**:
   ```bash
   pip install google-genai python-dotenv
   ```

3. **Environment Setup**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## 💻 Usage

Run the agent using `main.py` and provide a prompt:

```bash
python main.py "List the files in the project and tell me what the calculator does."
```

To see more detailed logs of the tool calls, use the `--verbose` flag:

```bash
python main.py --verbose "Run the calculator tests and report the results."
```

## 🧮 Included Example: Calculator

The `calculator/` directory contains a standalone calculator app that the Blucky agent can manage. It supports:
- **Basic Arithmetic**: `+`, `-`, `*`, `/`
- **Exponentiation**: `^`
- **Operator Precedence**: Correctly handles order of operations.
- **Interfaces**: Both CLI (`calculator/main.py`) and GUI (`calculator/gui.py`).

## ⚙️ Configuration

You can adjust the agent's behavior in `config.py`:
- `MAX_CHARS`: Limits the amount of text read from a file to avoid overloading the LLM context.
- `MAX_ITERS`: Prevents infinite loops by limiting the number of tool-call iterations per request.
