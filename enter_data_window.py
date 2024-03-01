from tkinter import *
from tkinter import ttk
import json



def click():
   global total_labor_week

   value = int(enter.get())
   total_labor_week += value

   with open('data_file.json', 'w') as file:
      data = {'last_labor_hour': 0, 
        'total_labor_week': total_labor_week, 
        'total_labor_year': 0, 
        'year_goal': 1005, 
        'weeks':45}
      
      json.dump(data, file)
   
   clear()
   print(total_labor_week)
   label_sum = ttk.Label(text= f"Summary: {total_labor_week}", background="#FFCDD2", foreground="#B71C1C", padding=8)
   label_sum.place(relx=0.1, rely=0.1)
   


def clear():
   enter.delete(0, END)   # удаление введенного текста



# data = {'last_labor_hour': 0, 
#         'total_labor_week': 0, 
#         'total_labor_year': 0, 
#         'year_goal': 1005, 
#         'weeks':45
# }

with open('data_file.json', 'r') as file:
   data = json.load(file)

last_labor_hour = data['last_labor_hour'] 
total_labor_week = data['total_labor_week']
total_labor_year = data['total_labor_year']
year_goal = data['year_goal']
weeks = data['weeks']




window = Tk()  #Main window
window.title("window")
window.geometry('400x300')

enter= ttk.Entry()
enter.place(relx=0.6, rely=0.3)
  
btn_enter_num = ttk.Button(text="Enter", command=click)
btn_enter_num.place(relx=0.65, rely=0.4)

label_sum = ttk.Label(text= f"Summary: {total_labor_week}", background="#FFCDD2", foreground="#B71C1C", padding=8)
label_sum.place(relx=0.1, rely=0.1)



window.mainloop()