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
         

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_names.append(candidate) 
            candidate_votes[candidate] = 1 
        
    percentage = {candidate: (votes / total_votes) * 100\
                   for candidate, votes in candidate_votes.items()}

    winning_candidate = max(candidate_votes)

print("Elections Results")
print("-------------------")
print("Total Votes:", total_votes)
print("-------------------")

for candidate in candidate_votes:
    print(f"{candidate}: {percentage[candidate]:.2f}%\
        ({candidate_votes[candidate]})")

print("-------------------------")
print("Winner:", {winning_candidate})
print("--------------------------")