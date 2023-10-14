import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

total_months = 0 
total_net = 0
average_change = 0
maximum_profit = 0
decrease_profit = 0

# print(os.getcwd())
# print(__file__)

# print(os.getcwd())

with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    for row in csv_reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
       
        
    print("Financial Analysis")
    print("------------------------")
    print("Total Months:", total_months)
    print("Total:", "$",total_net)
    print("Average Change:", "$")
    print("Greatest Increase in Profits: ", maximum_profit)
    print("Greatest Decrease in Profits:", decrease_profit)
