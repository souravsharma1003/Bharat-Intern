import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(1.0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            screen.delete(1.0, tk.END)
            screen.insert(tk.END, "Error")

    elif text == "C":
        screen.delete(1.0, tk.END)

    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

# Create the input field (Entry)
screen = tk.Text(root, height=2, width=18, font=("Arial", 24))
screen.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", button_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
