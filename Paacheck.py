import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    criteria = {
        "Length (8+)": len(password) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special Char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(criteria.values())
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, criteria

def on_check():
    pwd = entry.get()
    strength, criteria = check_password_strength(pwd)
    result_text = f"Password Strength: {strength}\n\nCriteria met:\n"
    for key, value in criteria.items():
        result_text += f" - {key}: {'Yes' if value else 'No'}\n"
    result_label.config(text=result_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 12))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()