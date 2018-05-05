import os

# Module for reading CSV's
import csv

# user input of file to be used in Election Results
results = input(f'what csv file do you want to use? (include .csv) ')


# Open csvfile
with open(results, newline='') as csvfile:
     # hold contents of csvfile
    csvreader = csv.reader(csvfile)

    #removes header for calculations
    next(csvreader, None)

    #List
    total = []
    candidates = {}

    for row in csvreader:

        total.append([row[0]])
        item = row[2]


        if  item in candidates:
             candidates[item] +=1
        else :
            candidates[item] = 1


        # rows = zip([k for k in sorted(candidates)], [candidates[k] for k in sorted(candidates)])
    print(f'Election Results')
    print("------------------------------------")
    print(f'Total Votes: {len(total)}')
    print("------------------------------------")
    for row in candidates.items():
        candidate = row[0]
        votes = row[1]
        percent_votes = round((votes/len(total)) * 100, 2)
        print(f'{candidate}: {percent_votes}% ({str(votes)})')
    # Determine the winner
    winner = max(candidates, key=candidates.get)

    print("------------------------------------")
    print(f'Winner: {winner}')
    print("------------------------------------")


    #create output file text file
    output_file = open("Election_Results.txt", "w")

    # write financial analysis output
    output_file.write(f'Election Results\n')
    output_file.write(f'-------------------------------------\n')
    output_file.write(f'Total Votes {len(total)}\n')
    #write each candidate to file
    for row in candidates.items():
        candidate = row[0]
        votes = row[1]
        percent_votes = round((votes/len(total)) * 100, 2)
        output_file.write(f'{candidate}: {percent_votes}% ({str(votes)})\n')
    #write winner to file
    output_file.write(f'-------------------------------------\n')
    output_file.write(f'Winner: {winner}\n')
