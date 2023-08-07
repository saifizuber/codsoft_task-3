import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(plen):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)
    password = ''.join(random.choices(s, k=plen))
    return password

def generate_password_callback():
    try:
        password_length = int(entry_password_length.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Invalid password length. Please provide a positive integer.")
            return

        password = generate_password(password_length)
        entry_generated_password.delete(0, tk.END)
        entry_generated_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

label_password_length = tk.Label(root, text="Password Length:")
label_password_length.grid(row=0, column=0, padx=10, pady=10)

entry_password_length = tk.Entry(root)
entry_password_length.grid(row=0, column=1, padx=10, pady=10)

btn_generate_password = tk.Button(root, text="Generate Password", command=generate_password_callback)
btn_generate_password.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_generated_password = tk.Label(root, text="Generated Password:")
label_generated_password.grid(row=2, column=0, padx=10, pady=10)

entry_generated_password = tk.Entry(root)
entry_generated_password.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
