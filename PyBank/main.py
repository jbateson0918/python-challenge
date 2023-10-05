import os
import csv

csvpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader, None)
    print("Financial Analysis")
    print("------------------------")
