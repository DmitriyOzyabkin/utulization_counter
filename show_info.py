from tkinter import *
from tkinter import ttk

def show_data(year_goal, total_labor_year, weeks, total_labor_week, current_week):
    label_year_goal = ttk.Label(text=f"Year goal: {year_goal} hours", padding=8)
    label_year_goal.place(relx=0.1, rely=0.1)

    label_year_hour = ttk.Label(text=f"Hours at current year: {total_labor_year} is {round(total_labor_year*100/year_goal, 2)}% of year goal", padding=8)
    label_year_hour.place(relx=0.1, rely=0.2)

    label_week_goal = ttk.Label(text=f" Current week ({current_week}/52) goal: {int(year_goal/weeks)} hours", padding=8)
    label_week_goal.place(relx=0.1, rely=0.3)

    label_week_hour = ttk.Label(text=f"Hours at current week: {total_labor_week} is {round(total_labor_week*100/(year_goal/weeks), 2)}% of week goal", padding=8)
    label_week_hour.place(relx=0.1, rely=0.4)