from tkinter import *
from tkinter import ttk
from datetime import date


today = date.today()

window = Tk()
window.title("Hour calculation")
window.geometry('400x300')
window.option_add("*tearOff", FALSE)

# frame = Frame(window)
# frame.pack()

current_date = Label(
   text=f"Date : {today} "
)
current_date.pack(anchor=NE, padx=20, pady=20)

main_menu = Menu()
file_menu = Menu()
settings_menu = Menu()

file_menu.add_command(label="New")
file_menu.add_command(label="Save")
settings_menu.add_command(label="1")
settings_menu.add_command(label="2")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Settings", menu=settings_menu)
 
window.config(menu=main_menu)


window.mainloop()
