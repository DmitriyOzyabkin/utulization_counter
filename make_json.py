import json


data = {'last_entry_week': 9, 
        'total_labor_week': 0, 
        'total_labor_year': 0, 
        'year_goal': 1005, 
        'weeks':52
}




with open('data_file.json', 'w') as file:
    json.dump(data, file)
    

