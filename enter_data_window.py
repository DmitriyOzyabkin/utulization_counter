from tkinter import *
from tkinter import ttk


count = 0 

def get_value():
   return int(enter.get())    # save entered hours to variable

def clear():
   enter.delete(0, END)   # delet number in entery place

def click():
   global count
   value = int(enter.get())
   count += value
   clear()

window = Tk()  #Main window
window.title("window")
window.geometry('400x300')


enter= ttk.Entry()
enter.place(relx=0.6, rely=0.3)
  
btn_enter_num = ttk.Button(text="Enter", command=click)
btn_enter_num.place(relx=0.65, rely=0.4)

label_sum = ttk.Label(text=f"Summary: {count}", background="#FFCDD2", foreground="#B71C1C", padding=8)
label_sum.place(relx=0.1, rely=0.1)



window.mainloop()