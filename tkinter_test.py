from tkinter import *
from tkinter import ttk
 
def click_button():
    value = clicks.get()    # получаем значение
    clicks.set(value + 1)
    print(type(value))   # устанавливаем новое значение
 
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")
 
clicks = IntVar(value=0)    # значение по умолчанию
 
btn = ttk.Button(textvariable=clicks, command=click_button)
btn.pack(anchor=CENTER, expand=1)
 
root.mainloop()

