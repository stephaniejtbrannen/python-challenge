import os

# Module for reading CSV's
import csv

#user input of file to be used in Financial Analysis
budget1 = input(f'what csv file do you want to use? (include .csv) ')

#Function to average values in a list
def average(lst):
    return sum(lst)/(len(lst))

# Open csvfile
with open(budget1, newline='') as csvfile:

    # hold contents of csvfile
    csvreader = csv.reader(csvfile)

    #removes header for calculations
    next(csvreader, None)

    #list variables
    months = []
    revenue = []
    change_list = []

    # defaults month1 value to 0 
    month1 = 0
    firstline = True


    #  Each row is read as a row
    for row in csvreader:
        
        # append month value index 0 of row to month list
        months.append(row[0])
        # changed revenue value (index 1 of row) to an integer
        rev = int(row[1])

        # appends the integer value of revenue (index 1 of row) to revenue list
        revenue.append(rev)
        
        # set month2 value to revenue value of row
        month2 = int(row[1])
        
        # calculate revenue change for this value and previous value
        #skip first row because there is no change.
        if firstline:
            firstline = False
        else:
            change = month2 - month1

            # append change value to change_lists
            change_list.append(change)
        
        #Set month 1 value to revenue value of row
        month1 = int(row[1])


 #combine original csv file with change list        
cleaned_csv = zip(months, change_list)

# find row  with max revenue change from change list
increase = max(cleaned_csv, key=lambda item:item[1])

#reset zip list
cleaned_csv = zip(months, change_list)
#find row with min revenue cahnge from change list
decrease = min(cleaned_csv, key=lambda item:item[1])



#print output in terminal
print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total Month: {len(months)}')
print(f'Total Revenue ${sum(revenue)}')
print(f'Average Revenue ${round(average(change_list))}')
print(f'Greatest Increase in Revenue: {increase[0]} (${increase[1]})')
print(f'Greatest Decrease in Revenue: {decrease[0]} (${decrease[1]})')

#create output file text file
output_file = open("Revenue_Summary.txt", "w")

# write financial analysis output
output_file.write( f"""
Financial Analysis
-------------------------------------
Total Month: {len(months)}
Total Revenue ${sum(revenue)}
Average Revenue ${round(average(change_list))}
Greatest Increase in Revenue: {increase[0]} (${increase[1]})
Greatest Decrease in Revenue: {decrease[0]} (${decrease[1]})
"""
)


