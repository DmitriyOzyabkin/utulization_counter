from tkinter import *
from tkinter import ttk
from datetime import date


today = date.today()

window = Tk()
window.title("Hour calculation")
window.geometry('800x600')

# frame = Frame(window)
# frame.pack()

current_date = Label(
   text=f"Date : {today} "
)
current_date.pack(anchor=NE, padx=20, pady=20)


window.mainloop()
