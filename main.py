import json
import random
import os
from employee import employee
from employee import EmployeeEncoder


level = input("How deep is the org chart?\n")
while True:
    try:
        value = int(level)
        if value > 20 or value <1:
            level = input("Please input a number between 1-20\n")
        else:
            break
    except:
        level = input("Please input a number between 1-20\n")

#random generation 
mean = 5
sdtDev = 2

#create top level
ceo = employee()

orgChart = [ceo]

level = 1
while level < 6:
    level +=1
    for emp in orgChart:
        if emp.level == level-1:
            if emp.nrSub == 0:
                emp.nrSub=round(random.gauss(5, 2))
            
            for sub in range(emp.nrSub):
                orgChart.append(employee(emp))
            
    

# Define the file path
file_path = "orgChart.json"
# Check if the file exists
if os.path.exists(file_path):
    # If it exists, remove it
    os.remove(file_path)

# Write the data to the JSON file
with open(file_path, "w") as json_file:
    json.dump(orgChart, json_file, indent=4, cls=EmployeeEncoder)

print(f"JSON data has been written to {file_path}")