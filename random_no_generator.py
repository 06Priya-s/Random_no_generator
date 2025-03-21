import random
import tkinter as tk
from tkinter import messagebox

# Generate random number
low, high = 1, 100
number = random.randint(low, high)
guesses = 0

# Check user guess
def check_guess():
    global guesses
    try:
        guess = int(entry.get())
        guesses += 1
        if guess < number:
            result_label.config(text=f"{guess} is too low! ⬇️")
        elif guess > number:
            result_label.config(text=f"{guess} is too high! ⬆️")
        else:
            messagebox.showinfo("Congratulations!", f"{guess} is correct! 🎉\nYou guessed it in {guesses} attempts!")
            root.destroy()
    except ValueError:
        result_label.config(text="Please enter a valid number! 🚫")

# Create GUI window
root = tk.Tk()
root.title("Number Guessing Game 🎯")
root.geometry("700x500")

# GUI Components
title_label = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=10)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess ✅", command=check_guess, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run GUI
root.mainloop()
