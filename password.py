import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return ""
    
   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
   
    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")


app = tk.Tk()
app.title("Password Generator")
app.geometry("300x200")


tk.Label(app, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)


generate_button = tk.Button(app, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)


password_var = tk.StringVar()
tk.Label(app, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(app, textvariable=password_var, state='readonly')
password_entry.pack(pady=5)


app.mainloop()
