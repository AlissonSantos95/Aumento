from tkinter import *
from tkinter import ttk

window = Tk()

entry_1 = Entry(window, width=45)
entry_1.grid(column = 0, row = 0)

# appends current content of l_one with the new pressed key value
def callback(event):
    l_one.config(text=entry_1.get() + event.char)

# binds callback to every keypress

l_one = Label(window)
l_one.grid(column = 0, row = 1)

window.mainloop()