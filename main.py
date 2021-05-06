# import libraries
from tkinter import *
from tkinter.ttk import *

from time import strftime

# UI Desgin
root = Tk()
root.title("Clock")

# Time function
def time():
    string = strftime("%H:%M:%S $p") # 24 hour mode. Change %H to %I for digital mode.
    label.config(text=string)
    label.after(1000, time)

label = Label(root, background="Black", foreground="Green")
label.pack(anchor="center")
time()

mainloop()