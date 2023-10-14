import os
import csv

csvpath = os.path.join("python-challenge","PyPoll", "Resources", "election_data.csv")

total_votes = 0

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    next(csv_reader, None)
    print("Elections Results")
    print("-------------------")

    for row in csv_reader:
        total_votes = total_votes + 1
        print("Total Votes:", total_votes)