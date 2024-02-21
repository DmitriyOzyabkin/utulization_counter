from tkinter import *
from tkinter import messagebox
from datetime import date


today = date.today()

window = Tk()
window.title("Hour calculation")
window.geometry('800x600')

frame = Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 80, #Задаём отступ по горизонтали.
   pady = 60 #Задаём отступ по вертикали.
)
frame.pack()

current_date = Label(
   frame,
   text=f"Date : {today} "
)
current_date.grid(row=20, column=50)


window.mainloop()
