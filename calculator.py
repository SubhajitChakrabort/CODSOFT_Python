import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("400x500")
        
        self.expression = ""
        self.input_text = tk.StringVar()

      
        input_frame = tk.Frame(self, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

      
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10) 

        
        btns_frame = tk.Frame(self, width=400, height=450, bg="grey")
        btns_frame.pack()

       
        self.create_button(btns_frame, "C", 1, 0, lambda: self.clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        self.create_button(btns_frame, "/", 1, 3).grid(row=0, column=3, padx=1, pady=1)

        
        self.create_button(btns_frame, "7", 1, 4).grid(row=1, column=0, padx=1, pady=1)
        self.create_button(btns_frame, "8", 1, 5).grid(row=1, column=1, padx=1, pady=1)
        self.create_button(btns_frame, "9", 1, 6).grid(row=1, column=2, padx=1, pady=1)
        self.create_button(btns_frame, "*", 1, 7).grid(row=1, column=3, padx=1, pady=1)

        
        self.create_button(btns_frame, "4", 1, 8).grid(row=2, column=0, padx=1, pady=1)
        self.create_button(btns_frame, "5", 1, 9).grid(row=2, column=1, padx=1, pady=1)
        self.create_button(btns_frame, "6", 1, 10).grid(row=2, column=2, padx=1, pady=1)
        self.create_button(btns_frame, "-", 1, 11).grid(row=2, column=3, padx=1, pady=1)

       
        self.create_button(btns_frame, "1", 1, 12).grid(row=3, column=0, padx=1, pady=1)
        self.create_button(btns_frame, "2", 1, 13).grid(row=3, column=1, padx=1, pady=1)
        self.create_button(btns_frame, "3", 1, 14).grid(row=3, column=2, padx=1, pady=1)
        self.create_button(btns_frame, "+", 1, 15).grid(row=3, column=3, padx=1, pady=1)

        
        self.create_button(btns_frame, "0", 1, 16, lambda: self.click("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        self.create_button(btns_frame, ".", 1, 18, lambda: self.click(".")).grid(row=4, column=2, padx=1, pady=1)
        self.create_button(btns_frame, "=", 1, 19, lambda: self.equals()).grid(row=4, column=3, padx=1, pady=1)

    def create_button(self, frame, text, row, col, command=None):
        if command is None:
            command = lambda: self.click(text)
        return tk.Button(frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=command)

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equals(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
