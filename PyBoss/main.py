import os
import csv
from datetime import datetime
import us_state_abbrev
try:
    os.remove("export/all_employee_data.csv")
except OSError:
    pass
# Loop through all files in directory
for filename in os.listdir(os.getcwd()):
    if filename.find(".csv") != -1:
        # print(filename)

        employee_lists = os.path.join(".", filename)

        employee_data = []



        # Split Name into first and last name
        # format DOB into MM/DD/YYYY
        # Mask SSN
        # Add state abbreviations using state abbreviation dictionary
        with open(employee_lists) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                first = row["Name"].split()[0]
                last =  row["Name"].split()[1]
                dob = row["DOB"]
                old_dob = datetime.strptime(dob,'%Y-%m-%d')
                new_dob = old_dob.strftime('%m/%d/%Y')
                ssn = row["SSN"]
                new_ssn = ""
                for x in range(len(ssn)):
                    if x < 6:
                        new_ssn = new_ssn + "*"
                    if x == 3 or x == 6:
                        new_ssn = new_ssn + "-"
                    if x > 6:
                        new_ssn = new_ssn + ssn[x]
                state_abbr = us_state_abbrev.us_state_abbrev[row["State"]]
                # Add all data to new dictionary
                employee_data.append(
                    {
                        "Emp ID": row["Emp ID"], 
                        "First Name": first,
                        "Last Name": last,
                        "DOB": new_dob,
                        "SSN": new_ssn,
                        "State": state_abbr
                    }
                )
        # Write updated data to csv file
        csvpath = os.path.join("export", "all_employee_data.csv")
        with open(csvpath, "a") as csvfile:
            fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employee_data)


        

    