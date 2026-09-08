import tkinter as tk
from tkinter import messagebox


def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = combo_operator.get()

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        result = num1 / num2

    label_result.config(text="Result = " + str(result))


root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x300")


# First Number
tk.Label(root, text="Enter First Number").pack(pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack()


# Operator
tk.Label(root, text="Select Operator").pack(pady=5)

combo_operator = tk.Entry(root)
combo_operator.pack()
combo_operator.insert(0, "+")


# Second Number
tk.Label(root, text="Enter Second Number").pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack()


# Calculate Button
tk.Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=20)

# Result
label_result = tk.Label(root, text="Result")
label_result.pack()

root.mainloop()