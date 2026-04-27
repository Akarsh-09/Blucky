import tkinter as tk
from tkinter import messagebox
from pkg.calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Scientific Calc")
        
        # Minecraft-inspired Color Palette
        self.colors = {
            "bg": "#5a5a5a",          # Dark Stone
            "display_bg": "#000000",  # Black
            "display_text": "#00ff00", # Neon Green (Terminal style)
            "btn_num": "#7b7b7b",     # Stone
            "btn_op": "#a0a0a0",      # Light Stone
            "btn_sci": "#c0c0c0",     # Silver/Platinum
            "btn_eq": "#4caf50",      # Grass Green
            "btn_text": "#000000",    # Black
        }
        
        self.root.configure(bg=self.colors["bg"])
        self.calculator = Calculator()
        
        self.expression = ""
        self.display_var = tk.StringVar()
        self.history = []
        self.history_visible = False
        
        # Root layout: History Frame on the left, Main Frame on the right
        self.history_frame = tk.Frame(root, bg=self.colors["bg"], width=250)
        self.main_frame = tk.Frame(root, bg=self.colors["bg"])
        
        self.main_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        # self.history_frame is not packed yet
        
        # --- History Frame Content ---
        self.history_label = tk.Label(
            self.history_frame, 
            text="Calculation History", 
            font=("Courier New", 16, "bold"), 
            bg=self.colors["bg"], 
            fg=self.colors["display_text"]
        )
        self.history_label.pack(pady=10)
        
        self.history_listbox = tk.Listbox(
            self.history_frame, 
            font=("Courier New", 12), 
            bg=self.colors["display_bg"], 
            fg=self.colors["display_text"],
            borderwidth=0,
            highlightthickness=0
        )
        self.history_listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        
        self.clear_history_btn = tk.Button(
            self.history_frame, 
            text="Delete History", 
            font=("Courier New", 12, "bold"),
            bg=self.colors["btn_op"], 
            fg=self.colors["btn_text"],
            command=self.clear_history
        )
        self.clear_history_btn.pack(pady=10)

        # --- Main Frame Content ---
        # History Toggle Button
        self.history_btn = tk.Button(
            self.main_frame,
            text="History",
            font=("Courier New", 12, "bold"),
            bg=self.colors["btn_sci"],
            fg=self.colors["btn_text"],
            command=self.toggle_history
        )
        self.history_btn.grid(row=0, column=0, columnspan=5, pady=(10, 0), sticky="ew", padx=10)

        # Display
        self.display = tk.Entry(
            self.main_frame, 
            textvariable=self.display_var, 
            font=("Courier New", 24, "bold"), 
            borderwidth=5, 
            relief="sunken", 
            justify='right', 
            bg=self.colors["display_bg"], 
            fg=self.colors["display_text"],
            insertbackground=self.colors["display_text"]
        )
        self.display.grid(row=1, column=0, columnspan=5, padx=10, pady=20, sticky="nsew")
        
        # Button configuration
        # (text, row, col, columnspan, color, text_color)
        buttons = [
            ('AC', 3, 0, 1, self.colors["btn_op"], self.colors["btn_text"]),
            ('DEL', 3, 1, 1, self.colors["btn_op"], self.colors["btn_text"]),
            ('(', 3, 2, 1, self.colors["btn_op"], self.colors["btn_text"]),
            (')', 3, 3, 1, self.colors["btn_op"], self.colors["btn_text"]),
            ('/', 3, 4, 1, self.colors["btn_op"], self.colors["btn_text"]),
            
            ('sin', 2, 0, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('cos', 2, 1, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('tan', 2, 2, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('log', 2, 3, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('ln', 2, 4, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            
            ('sqrt', 4, 0, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('7', 4, 1, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('8', 4, 2, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('9', 4, 3, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('*', 4, 4, 1, self.colors["btn_op"], self.colors["btn_text"]),
            
            ('^', 5, 0, 1, self.colors["btn_sci"], self.colors["btn_text"]),
            ('4', 5, 1, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('5', 5, 2, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('6', 5, 3, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('-', 5, 4, 1, self.colors["btn_op"], self.colors["btn_text"]),
            
            ('.', 6, 0, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('1', 6, 1, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('2', 6, 2, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('3', 6, 3, 1, self.colors["btn_num"], self.colors["btn_text"]),
            ('+', 6, 4, 1, self.colors["btn_op"], self.colors["btn_text"]),
            
            ('0', 7, 0, 2, self.colors["btn_num"], self.colors["btn_text"]),
            ('=', 7, 2, 3, self.colors["btn_eq"], self.colors["btn_text"]),
        ]
        
        for (text, row, col, span, color, text_col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            btn = tk.Button(
                self.main_frame, 
                text=text, 
                width=5, 
                height=2, 
                font=("Courier New", 14, "bold"),
                bg=color, 
                fg=text_col,
                activebackground=color, 
                activeforeground=text_col,
                relief="raised",
                borderwidth=4,
                command=action
            )
            btn.grid(row=row, column=col, columnspan=span, padx=4, pady=4, sticky="nsew")
        
        # Configure grid weights so buttons resize
        for i in range(5):
            self.main_frame.grid_columnconfigure(i, weight=1)
        for i in range(1, 8):
            self.main_frame.grid_rowconfigure(i, weight=1)

    def toggle_history(self):
        if self.history_visible:
            self.history_frame.pack_forget()
            self.history_visible = False
        else:
            self.history_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.update_history_listbox()
            self.history_visible = True

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.history:
            self.history_listbox.insert(tk.END, item)

    def clear_history(self):
        self.history = []
        self.update_history_listbox()

    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""
            self.display_var.set("")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)
        elif char == '=':
            try:
                result = self.calculator.evaluate(self.expression)
                if result is not None:
                    # Format result to avoid long decimals if it's nearly an integer
                    if isinstance(result, float):
                        if abs(result - round(result)) < 1e-9:
                            result = round(result)
                        else:
                            result = round(result, 8)
                    
                    res_str = str(result)
                    # Store in history
                    self.history.append(f"{self.expression} = {res_str}")
                    
                    self.display_var.set(res_str)
                    self.expression = res_str
                else:
                    messagebox.showerror("Error", "Empty expression")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            if char in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt']:
                self.expression += char + " "
            else:
                self.expression += char
            
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
