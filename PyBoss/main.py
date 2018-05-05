import os
import csv
from datetime import datetime

filepath = os.path.join(".", "employee_data1.csv")

employee_data = {}

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first = row["Name"].split()[0]
        last =  row["Name"].split()[1]
        dob = row["DOB"]
        old_dob = datetime.strptime(dob,'%Y-%m-%d')
        new_dob = old_dob.strftime('%m/%d/%Y')
        print(new_dob)
        print(first)
    