import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to clear the entire calculation
def clear_all():
    entry.delete(0, tk.END)
    result.set("")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the calculation
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button widgets for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=39, pady=20, command=calculate).grid(row=row_num, column=col_num)
    elif button == '0':
        tk.Button(root, text=button, padx=87, pady=20, command=lambda: entry.insert(tk.END, button)).grid(row=row_num, column=col_num, columnspan=2)
        col_num += 1
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda btn=button: entry.insert(tk.END, btn)).grid(row=row_num, column=col_num)

    col_num += 1

    if col_num > 3:
        col_num = 0
        row_num += 1

# Result variable
result = tk.StringVar()
result.set("")

# Label widget to display the result
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=row_num, column=0, columnspan=4, padx=10, pady=10)

# Button widget to clear the entry field
clear_entry_button = tk.Button(root, text="CE", padx=20, pady=20, command=clear_entry)
clear_entry_button.grid(row=row_num + 1, column=0)

# Button widget to clear the entire calculation
clear_all_button = tk.Button(root, text="C", padx=20, pady=20, command=clear_all)
clear_all_button.grid(row=row_num + 1, column=1)

root.mainloop()