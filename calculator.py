import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x600")  # Set a fixed size for the calculator
        master.minsize(400, 600)    # Set a minimum size to prevent shrinking

        self.result_var = tk.StringVar()
        self.history = []

        # Entry field for the result
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Text area for history
        self.history_text = tk.Text(master, height=10, width=30, font=("Arial", 12), bd=5, bg="#e0e0e0", state='disabled')
        self.history_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Create initial buttons
        self.create_buttons()

    def create_buttons(self):
        # Create normal calculator buttons
        self.create_buttons_normal()

    def create_buttons_normal(self):
        normal_buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
            ('C', 5, 4)
        ]

        for (text, row, col) in normal_buttons:
            button = tk.Button(self.master, text=text, padx=30, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configure row and column weights for better resizing
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.master.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                expression = self.result_var.get()
                # Evaluate the expression
                result = eval(expression)
                self.result_var.set(result)
                self.add_to_history(f"{expression} = {result}")
            except Exception as e:
                self.result_var.set("Invalid Input")
        else:
            current_text = self.result_var.get()
            new_text = current_text + str(char)
            self.result_var.set(new_text)

    def add_to_history(self, entry):
        self.history.append(entry)
        self.update_history_display()

    def update_history_display(self):
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)  # Clear existing text
        for item in self.history:
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()