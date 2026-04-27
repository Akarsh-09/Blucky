import tkinter as tk
from tkinter import messagebox
from pkg.calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.configure(bg="#2c3e50")
        self.calculator = Calculator()
        
        self.expression = ""
        self.display_var = tk.StringVar()
        
        # Colors
        self.colors = {
            "bg": "#2c3e50",
            "display_bg": "#ecf0f1",
            "text": "#2c3e50",
            "btn_num": "#34495e",
            "btn_op": "#e67e22",
            "btn_spec": "#e74c3c",
            "btn_eq": "#2ecc71",
            "btn_text": "black"
        }
        
        # Display
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 24), 
            borderwidth=0, 
            relief="flat", 
            justify='right', 
            bg=self.colors["display_bg"], 
            fg=self.colors["text"]
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        
        # Button configuration
        # (text, row, col, columnspan, color)
        buttons = [
            ('AC', 1, 0, 1, self.colors["btn_num"]),
            ('DEL', 1, 1, 1, self.colors["btn_num"]),
            ('^', 1, 2, 1, self.colors["btn_num"]),
            ('/', 1, 3, 1, self.colors["btn_op"]),
            
            ('7', 2, 0, 1, self.colors["btn_num"]),
            ('8', 2, 1, 1, self.colors["btn_num"]),
            ('9', 2, 2, 1, self.colors["btn_num"]),
            ('*', 2, 3, 1, self.colors["btn_op"]),
            
            ('4', 3, 0, 1, self.colors["btn_num"]),
            ('5', 3, 1, 1, self.colors["btn_num"]),
            ('6', 3, 2, 1, self.colors["btn_num"]),
            ('-', 3, 3, 1, self.colors["btn_op"]),
            
            ('1', 4, 0, 1, self.colors["btn_num"]),
            ('2', 4, 1, 1, self.colors["btn_num"]),
            ('3', 4, 2, 1, self.colors["btn_spec"]),
            ('+', 4, 3, 1, self.colors["btn_op"]),
            
            ('.', 5, 0, 1, self.colors["btn_spec"]),
            ('0', 5, 1, 1, self.colors["btn_eq"]),
            ('=', 5, 2, 2, self.colors["btn_op"]),
        ]
        
        for (text, row, col, span, color) in buttons:
            action = lambda x=text: self.on_button_click(x)
            btn = tk.Button(
                root, 
                text=text, 
                width=5, 
                height=2, 
                font=("Arial", 14, "bold"),
                bg=color, 
                fg=self.colors["btn_text"],
                activebackground=color, 
                activeforeground=self.colors["btn_text"],
                relief="flat",
                command=action
            )
            btn.grid(row=row, column=col, columnspan=span, padx=5, pady=5, sticky="nsew")
        
        # Configure grid weights so buttons resize
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""
            self.display_var.set("")
        elif char == 'DEL':
            if self.expression.endswith(" "):
                # Remove the space and the operator.
                self.expression = self.expression[:-2]
            else:
                # Remove the last character (digit or .)
                self.expression = self.expression[:-1]
            self.display_var.set(self.expression.replace(" ", ""))
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