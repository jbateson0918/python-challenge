import os
import csv

csvpath = os.path.join("python-challenge","PyBank", "Resources", "budget_data.csv")

total_rows = 0 
total = 0
average_profit = 0
maximum_profit = 0
decrease_profit = 0

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader, None)
    print("Financial Analysis")
    print("------------------------")

    
    for row in csv_reader:
        total_rows = total_rows + 1
        total = total + int(row[1])
        average_profit = (total / 86)
        maximum_profit = maximum_profit + int(max(row[1]))
        decrease_profit = decrease_profit + int(min(row[1]))

    print("Total Months:", total_rows)
    print("Total:", total)
    print("Average Change:", average_profit)
    print("Greatest Increase in Profits: ", maximum_profit)
    print("Greatest Decrease in Profits:", decrease_profit)
    
    


    

  




