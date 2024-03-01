from tkinter import *
from tkinter import ttk
from datetime import date
import json
import check_date
import show_info

today = date.today()                 # current date and check week begining for zerorize week goal
current_week = today.isocalendar()[1]
check_date.check_date(today)


with open('data_file.json', 'r') as file:    # load statistics from json file
   data = json.load(file)

last_entery_week = data['last_entry_week'] 
total_labor_week = data['total_labor_week']
total_labor_year = data['total_labor_year']
year_goal = data['year_goal']
weeks = data['weeks']

window = Tk()                       #Main window
window.title("Hour calculation")
window.geometry('400x300')


def open_settings_window():         # window for enter goals and correct data
   window_settings = Tk()
   window_settings.title("Settings")
   window_settings.geometry('250x200')

   btn_save_settings = ttk.Button(window_settings, text = 'Save')
   btn_save_settings.place(relx=0.1, rely=0.8)

   btn_exit_settings = ttk.Button(window_settings, text = 'Exit', 
                                  command = lambda: window_settings.destroy())
   btn_exit_settings.place(relx=0.6, rely=0.8)

def error_window():                  # window shows that hours enterd not in valide format
   window_error = Tk()
   window_error.title("ERROR")
   window_error.geometry('250x100')

   label_error = ttk.Label(window_error, text='Invalid time format')
   label_error.pack()
   btn_OK = ttk.Button(window_error, text = 'OK', command=lambda: window_error.destroy())
   btn_OK.pack(side='bottom')


def clear():
   enter_hour.delete(0, END)         # clean eneter field
 
def click():                         # summarize labor hours and save entered hours to json
   global last_labor_hour
   global total_labor_week
   global total_labor_year
  
   entered_value = enter_hour.get()   
   if check_valid_enter(entered_value) is True:
      last_labor_hour = float(entered_value)
      total_labor_week += last_labor_hour
      total_labor_year += last_labor_hour

      with open('data_file.json', 'w') as file:
         data = {'last_entry_week': current_week, 
         'total_labor_week': round(total_labor_week, 2), 
         'total_labor_year': round(total_labor_year, 2), 
         'year_goal': 1005, 
         'weeks':52}
         
         json.dump(data, file)
      clear()
  
      show_info.show_data(year_goal, total_labor_year, weeks, total_labor_week, current_week)

   else:
      clear()
      error_window()
      
def check_valid_enter(string: str) -> bool:  # check entered value of hours for valide format
   for symbol in string:
      if symbol not in '-0123456789.':
         return False
      else:
         continue
   return True

# Current Date lable
   
current_date = Label(
   text=f"Date : {today} "
)
current_date.pack(anchor=NE, padx=20, pady=20)

# Settings button

btn_settings = ttk.Button(text = 'Settings', command = open_settings_window)
btn_settings.place(relx=0.1, rely=0.87)

# Enter hour field and button

label_valide_enter = ttk.Label(text='Enter hours in format XX or X.XX')
label_valide_enter.place(relx=0.55, rely=0.63)                              

enter_hour = ttk.Entry()
enter_hour.place(relx=0.6, rely=0.7)
  
btn_enter_hour = ttk.Button(text="Enter", command=click)
btn_enter_hour.place(relx=0.65, rely=0.8)

# Year and week hour information feild at start

show_info.show_data(year_goal, total_labor_year, weeks, total_labor_week, current_week)

window.mainloop()

