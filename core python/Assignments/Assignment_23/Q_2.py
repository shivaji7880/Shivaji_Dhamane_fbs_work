import tkinter as tk
from tkinter import ttk


def convert():
    amount = float(entry_amount.get())

    from_currency = combo_from.get()
    to_currency = combo_to.get()

    rates = {
        "USD": 1,
        "INR": 83,
        "EUR": 0.92,
        "GBP": 0.79
    }

    usd_amount = amount / rates[from_currency]
    result = usd_amount * rates[to_currency]

    label_result.config(text=f"{result:.2f} {to_currency}")


root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")


# Amount
tk.Label(root, text="Enter Amount").pack(pady=10)

entry_amount = tk.Entry(root)
entry_amount.pack()


# From Currency
tk.Label(root, text="From Currency").pack(pady=10)

combo_from = ttk.Combobox(
    root,
    values=["USD", "INR", "EUR", "GBP"],
    state="readonly"
)
combo_from.pack()
combo_from.set("USD")


# To Currency
tk.Label(root, text="To Currency").pack(pady=10)

combo_to = ttk.Combobox(
    root,
    values=["USD", "INR", "EUR", "GBP"],
    state="readonly"
)
combo_to.pack()
combo_to.set("INR")


# Convert Button
tk.Button(
    root,
    text="Convert",
    command=convert
).pack(pady=20)


# Result
label_result = tk.Label(
    root,
    text="Result",
    font=("Arial", 14)
)
label_result.pack()


root.mainloop()