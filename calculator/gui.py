import tkinter as tk
from tkinter import messagebox
from pkg.calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calculator = Calculator()
        
        self.expression = ""
        self.display_var = tk.StringVar()
        
        # Display
        self.display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 20), borderwidth=5, relief="flat", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            '^'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
                      command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights so buttons resize
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            try:
                # Ensure spaces between tokens for the Calculator.evaluate method
                formatted_expression = self._format_expression(self.expression)
                result = self.calculator.evaluate(formatted_expression)
                if result is not None:
                    # Display result, formatted to remove trailing .0 if it's an integer
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    self.display_var.set(str(result))
                    self.expression = str(result)
                else:
                    messagebox.showerror("Error", "Empty expression")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            # Add space before operators to satisfy Calculator.evaluate requirement
            if char in '+-*/^':
                # If the expression ends with a space, don't add another one
                if self.expression.endswith(" "):
                    self.expression += f"{char} "
                else:
                    self.expression += f" {char} "
            else:
                # If the last char was a space, don't add another one before a digit
                if self.expression.endswith(" "):
                    self.expression += char
                else:
                    self.expression += char
            
            # Display the expression without the padding spaces for better UI
            self.display_var.set(self.expression.replace(" ", ""))

    def _format_expression(self, expr):
        # The Calculator.evaluate expects space-separated tokens.
        return expr

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
