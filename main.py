from tkinter import *
from tkinter import ttk
from datetime import date


today = date.today()

window = Tk()
window.title("Hour calculation")
window.geometry('400x300')

# frame = Frame(window)
# frame.pack()

def open_settings_window():
   window_settings = Tk()
   window_settings.title("Settings")
   window_settings.geometry('250x200')

   btn_save_settings = ttk.Button(window_settings, text = 'Save')
   btn_save_settings.place(relx=0.1, rely=0.8)

   btn_exit_settings = ttk.Button(window_settings, text = 'Exit', command = lambda: window_settings.destroy())
   btn_exit_settings.place(relx=0.6, rely=0.8)

current_date = Label(
   text=f"Date : {today} "
)
current_date.pack(anchor=NE, padx=20, pady=20)

btn_settings = ttk.Button(text = 'Settings', command = open_settings_window)
btn_settings.place(relx=0.1, rely=0.87)

window.mainloop()
