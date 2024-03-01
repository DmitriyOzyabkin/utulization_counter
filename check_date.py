from datetime import date
import json

# 0 - monday
# 1 - tuesday 
# 2 - wensday
# 3 - thursday
# 4 - friday
# 5 - surtoday
# 6 - sunday 

def check_date(today):
    with open('data_file.json', 'r') as file:
        data = json.load(file)
    if today.isocalendar()[1] != data['last_entry_week']:
        data['last_entry_week'] = today.isocalendar()[1]
        data["total_labor_week"] = 0

        with open('data_file.json', 'w') as file:
            json.dump(data, file)

