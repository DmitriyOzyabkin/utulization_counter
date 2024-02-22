from tkinter import *
from tkinter import ttk
from datetime import date
last_labor_hour = 0
total_labor = 0

today = date.today()

window = Tk()  #Main window
window.title("Hour calculation")
window.geometry('400x300')

# Settings window

def open_settings_window(): # 
   window_settings = Tk()
   window_settings.title("Settings")
   window_settings.geometry('250x200')

   btn_save_settings = ttk.Button(window_settings, text = 'Save')
   btn_save_settings.place(relx=0.1, rely=0.8)

   btn_exit_settings = ttk.Button(window_settings, text = 'Exit', 
                                  command = lambda: window_settings.destroy())
   btn_exit_settings.place(relx=0.6, rely=0.8)

# Enter hour feild functions
   
def clear():
   enter_hour.delete(0, END)   # удаление введенного текста
 
def get_last_labor_hour():
   global last_labor_hour
   global total_labor
   value = 0
   value = enter_hour.get()     # save entered hours to variable
   if value.isdigit():
      last_labor_hour = int(value)
      total_labor += last_labor_hour
      clear()
   else:
      label = ttk.Label(text='Not digit!!!')
      label.place(relx=0.7, rely=0.2)
      clear()



# Current Date lable
   
current_date = Label(
   text=f"Date : {today} "
)
current_date.pack(anchor=NE, padx=20, pady=20)

# Settings button

btn_settings = ttk.Button(text = 'Settings', 
                          command = open_settings_window)
btn_settings.place(relx=0.1, rely=0.87)

# Enter hour field and button

enter_hour = ttk.Entry()
enter_hour.place(relx=0.6, rely=0.3)
  
btn_enter_hour = ttk.Button(text="Enter", command=get_last_labor_hour)
btn_enter_hour.place(relx=0.65, rely=0.4)





window.mainloop()


print(total_labor)