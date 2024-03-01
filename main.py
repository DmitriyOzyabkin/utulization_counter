from tkinter import *
from tkinter import ttk
from datetime import date
import json
import check_date

today = date.today()
current_week = today.isocalendar()[1]
check_date.check_date(today)


with open('data_file.json', 'r') as file:
   data = json.load(file)

last_entery_week = data['last_entry_week'] 
total_labor_week = data['total_labor_week']
total_labor_year = data['total_labor_year']
year_goal = data['year_goal']
weeks = data['weeks']


# data = {'last_entery_week': 0, 
#         'total_labor_week': 0, 
#         'total_labor_year': 0, 
#         'year_goal': 1005, 
#         'weeks':45
# }

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

def error_window(): # 
   window_error = Tk()
   window_error.title("ERROR")
   window_error.geometry('250x100')

   label_error = ttk.Label(window_error, text='Invalid time format')
   label_error.pack()
   btn_OK = ttk.Button(window_error, text = 'OK', command=lambda: window_error.destroy())
   btn_OK.pack(side='bottom')


# Enter hour feild functions
   
def clear():
   enter_hour.delete(0, END)   # удаление введенного текста
 
def click():
   global last_labor_hour
   global total_labor_week
   global total_labor_year
  
   entered_value = enter_hour.get()   # save entered hours to variable
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
  
      label_year_goal = ttk.Label(text=f"Year goal: {year_goal} hours", padding=8)
      label_year_goal.place(relx=0.1, rely=0.1)

      label_year_hour = ttk.Label(text=f"Hours at current year: {total_labor_year} is {round(total_labor_year*100/year_goal, 2)}% of year goal", padding=8)
      label_year_hour.place(relx=0.1, rely=0.2)

      label_week_goal = ttk.Label(text=f" Current week ({current_week}/52) goal: {int(year_goal/weeks)} hours", padding=8)
      label_week_goal.place(relx=0.1, rely=0.3)

      label_week_hour = ttk.Label(text=f"Hours at current week: {total_labor_week} is {round(total_labor_week*100/(year_goal/weeks), 2)}% of week goal", padding=8)
      label_week_hour.place(relx=0.1, rely=0.4)
   else:
      clear()
      error_window()
      
def check_valid_enter(string: str) -> bool:
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

enter_hour = ttk.Entry()
enter_hour.place(relx=0.6, rely=0.6)
  
btn_enter_hour = ttk.Button(text="Enter", command=click)
btn_enter_hour.place(relx=0.65, rely=0.7)

# Year and week hour information feild

label_year_goal = ttk.Label(text=f"Year goal: {year_goal} hours", padding=8)
label_year_goal.place(relx=0.1, rely=0.1)

label_year_hour = ttk.Label(text=f"Hours at current year: {total_labor_year} is {round(total_labor_year*100/year_goal, 2)}% of year goal", padding=8)
label_year_hour.place(relx=0.1, rely=0.2)

label_week_goal = ttk.Label(text=f" Current week ({current_week}/52) goal: {int(year_goal/weeks)} hours", padding=8)
label_week_goal.place(relx=0.1, rely=0.3)

label_week_hour = ttk.Label(text=f"Hours at current week: {total_labor_week} is {round(total_labor_week*100/(year_goal/weeks), 2)}% of week goal", padding=8)
label_week_hour.place(relx=0.1, rely=0.4)

window.mainloop()

