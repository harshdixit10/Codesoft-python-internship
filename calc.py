import tkinter as tk
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)
def clear_display():
    display.delete(0, tk.END)
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Simple Calculator")

display = tk.Entry(window, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0
for button_text in button_texts:
    if button_text == '=':
        tk.Button(window, text=button_text, command=calculate,
                height=2, width=5).grid(row=row, column=col)
    elif button_text == 'C':
        tk.Button(window, text=button_text, command=clear_display,
                height=2, width=5).grid(row=row, column=col)
    else:
        tk.Button(window, text=button_text, command=lambda b=button_text: button_click(
            b), height=2, width=5).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
window.mainloop()
