import Convert
import tkinter as tk
from tkinter import ttk


def convert(event):
    inp = uinput.get()
    b1 = int(options.get())
    b2 = int(options1.get())
    if b1 != 10 and b2 == 10:
        a = Convert.btoten(inp, b1)
        uoutput.delete(0, 'end')
        uoutput.insert(0, a)
    elif b1 == 10 and b2 != 10:
        a = Convert.tentob(inp, b2)
        uoutput.delete(0, 'end')
        uoutput.insert(0, a)
    else:
        a1 = Convert.btoten(inp, b1)
        a = Convert.tentob(a1, b2)
        uoutput.delete(0, 'end')
        uoutput.insert(0, a)


def clearinput(event):
    uinput.delete(0, 'end')

window = tk.Tk()
window.title("Base converter")
n = tk.StringVar()
m = tk.StringVar()

Credit = tk.Label(window, text="Converter Pro max", font=20)
Credit.grid(column=0, row=0)
frame1 = tk.Frame(window)
I_text = tk.Label(frame1, text="Input base:")
I_text.grid(column=0, row=1)
options = ttk.Combobox(frame1, textvariable=n)
options['values'] = ('2', '8', '10', '16')
options.grid(column=1, row=1)
frame1.grid(column=0, row=1)
uinput = tk.Entry(window, width=30, font=20)
uinput.grid(column=0, row=2)

frame2 = tk.Frame(window)
O_text = tk.Label(frame2, text="Output base:")
O_text.grid(column=0, row=1)
options1 = ttk.Combobox(frame2, textvariable=m)
options1['values'] = ('2', '8', '10', '16')
options1.grid(column=1, row=1)
frame2.grid(column=0, row=3)
uoutput = tk.Entry(window, width=30, font=20)
uoutput.grid(column=0, row=4)

frame3 = tk.Frame(window)
button = tk.Button(frame3, text='convert')
button.bind('<Button-1>', convert)
button.grid(column=0, row=0)
button1 = tk.Button(frame3, text='clear input')
button1.bind('<Button-2>', clearinput)
button1.grid(column=1, row=0)
frame3.grid(column=0, row=5)
window.bind('<Return>', convert)
window.bind('<Delete>', clearinput)

window.mainloop()
