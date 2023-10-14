import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")
MONTH_IDX = 0
PROFIT_IDX = 1


os.chdir(os.path.dirname(os.path.realpath(__file__)))

total_months = 0 
total_profit = 0
total_change = 0
maximum_profit = 0
decrease_profit = 0
is_first_row = True
# print(os.getcwd())
# print(__file__)

# print(os.getcwd())

with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    for row in csv_reader:
        curr_profit = int(row[PROFIT_IDX])
        total_months += 1
        total_profit += curr_profit
        if is_first_row: 
            is_first_row = False
        else:
            curr_change = curr_profit - prev_profit
            total_change += curr_change
    
        # Prepare for next month
        prev_profit = curr_profit

average_change = total_change / (total_months - 1)
       
        
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_months)
print("Total:", "$",total_profit)
print("Average Change:", f"${average_change}")
print("Greatest Increase in Profits: ", maximum_profit)
print("Greatest Decrease in Profits:", decrease_profit)
