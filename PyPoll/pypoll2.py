import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_names = []
candidate_votes = {}


with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        candidate_names.append(candidate) 
        candidate_names.count(candidate)
   


    print("Elections Results")
    print("-------------------")
    print("Total Votes:", total_votes)
    print("-------------------")
print(candidate_names)

