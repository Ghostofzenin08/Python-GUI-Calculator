import math
import tkinter as tk
from tkinter import END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial



def get_input(entry, argu):
    entry.insert(END, argu)


def get_function(entry, func_name):
    entry.insert(END, f"{func_name}(")


def backspace(entry):
    input_len = len(entry.get())
    if input_len:
        entry.delete(input_len - 1, END)


def clear(entry):
    entry.delete(0, END)


def evaluate(entry):
    """Evaluate a calculator expression without exposing Python builtins."""
    functions = {
        "sin": lambda value: math.sin(math.radians(value)),
        "cos": lambda value: math.cos(math.radians(value)),
        "tan": lambda value: math.tan(math.radians(value)),
        "asin": lambda value: math.degrees(math.asin(value)),
        "acos": lambda value: math.degrees(math.acos(value)),
        "atan": lambda value: math.degrees(math.atan(value)),
        "sqrt": math.sqrt,
        "pi": math.pi,
    }
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression, {"__builtins__": {}}, functions)
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError, NameError, OverflowError):
        entry.delete(0, END)
        entry.insert(0, "Error")
        return

    entry.delete(0, END)
    entry.insert(0, str(result))


def popupmsg(message):
    popup = tk.Tk()
    popup.resizable(0, 0)
    popup.geometry("180x100")
    popup.title("Alert")
    label = Label(popup, text=message)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def cal():
    root = tk.Tk()
    root.title("calculator")
    root.resizable(0,0)

    entry_font = font.Font(size=20)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, 
               sticky=N + W + S + E, padx=5, pady=5)

    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    text_fg = '#FFFFFF'
    button_active_bg = '#c0c0c0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg, 
                         padx=10, pady=3, activebackground=button_active_bg)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg, 
                         padx=10, pady=3, activebackground=button_active_bg)

    button7 = num_button(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=2, column=3, pady=5)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5)

    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=4, column=3, pady=5)

    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5)

    decimal = num_button(text='.', command=lambda: get_input(entry, '.'))
    decimal.grid(row=5, column=1, pady=5)

    equals = cal_button(text='=', command=lambda: evaluate(entry))
    equals.grid(row=5, column=2, pady=5)

    divide = cal_button(text='/', command=lambda: get_input(entry, '/'))
    divide.grid(row=5, column=3, pady=5)

    left_parenthesis = num_button(text='(', command=lambda: get_input(entry, '('))
    left_parenthesis.grid(row=6, column=0, pady=5)

    right_parenthesis = num_button(text=')', command=lambda: get_input(entry, ')'))
    right_parenthesis.grid(row=6, column=1, pady=5)

    power = cal_button(text='^', command=lambda: get_input(entry, '^'))
    power.grid(row=6, column=2, pady=5)

    pi = num_button(text='π', command=lambda: get_input(entry, 'pi'))
    pi.grid(row=6, column=3, pady=5)

    clear_button = Button(root, text='Clear', command=lambda: clear(entry), height=1, width=7)
    clear_button.grid(row=7, column=0, pady=5)

    backspace_button = Button(root, text='⌫', command=lambda: backspace(entry), height=1, width=7)
    backspace_button.grid(row=7, column=1, pady=5)

    exit_button = Button(root, text='Quit', fg='white', bg='black', command=root.destroy, height=1, width=7)
    exit_button.grid(row=7, column=2, columnspan=2, pady=5)



    # Trigonometric functions use degrees for input and output.
    sin_button = num_button(text='sin', command=lambda: get_function(entry, 'sin'))
    sin_button.grid(row=8, column=0, pady=5)

    cos_button = num_button(text='cos', command=lambda: get_function(entry, 'cos'))
    cos_button.grid(row=8, column=1, pady=5)

    tan_button = num_button(text='tan', command=lambda: get_function(entry, 'tan'))
    tan_button.grid(row=8, column=2, pady=5)

    sqrt_button = num_button(text='sqrt', command=lambda: get_function(entry, 'sqrt'))
    sqrt_button.grid(row=8, column=3, pady=5)

    asin_button = num_button(text='asin', command=lambda: get_function(entry, 'asin'))
    asin_button.grid(row=9, column=0, pady=5)

    acos_button = num_button(text='acos', command=lambda: get_function(entry, 'acos'))
    acos_button.grid(row=9, column=1, pady=5)

    atan_button = num_button(text='atan', command=lambda: get_function(entry, 'atan'))
    atan_button.grid(row=9, column=2, pady=5)


    root.mainloop()

if __name__ == "__main__":
    cal()
