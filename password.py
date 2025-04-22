import tkinter as tk
from tkinter import font
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Length must be positive.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)

# Create main window
root = tk.Tk()
root.title("Stylish Password Generator")
root.geometry("500x300")
root.configure(bg="#2c3e50")

# Define a stylish font
title_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
result_font = font.Font(family="Courier", size=14, weight="bold")

# Top frame (North)
top_frame = tk.Frame(root, bg="#34495e", pady=10)
top_frame.pack(side="top", fill="x")
title_label = tk.Label(top_frame, text="Secure Password Generator", bg="#34495e", fg="white", font=title_font)
title_label.pack()

# Center frame (Center)
center_frame = tk.Frame(root, bg="#2c3e50")
center_frame.pack(expand=True)

length_label = tk.Label(center_frame, text="Enter password length:", bg="#2c3e50", fg="white", font=label_font)
length_label.pack(pady=10)

length_entry = tk.Entry(center_frame, width=10, font=label_font, justify='center')
length_entry.pack()

generate_button = tk.Button(center_frame, text="Generate Password", font=label_font, command=generate_password, bg="#1abc9c", fg="white", padx=10, pady=5)
generate_button.pack(pady=10)

result_label = tk.Label(center_frame, text="", bg="#2c3e50", fg="#f1c40f", font=result_font)
result_label.pack(pady=10)

# Bottom frame (South)
bottom_frame = tk.Frame(root, bg="#34495e", pady=10)
bottom_frame.pack(side="bottom", fill="x")
footer_label = tk.Label(bottom_frame, text="© 2025 SecureGen", bg="#34495e", fg="white", font=label_font)
footer_label.pack()

root.mainloop()
