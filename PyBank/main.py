import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")
MONTH_IDX = 0
PROFIT_IDX = 1


os.chdir(os.path.dirname(os.path.realpath(__file__)))

total_months = 0 
total_profit = 0
total_change = 0
maximum_profit = {"month": "", "amount": 0}
decrease_profit = {"month": "", "amount": 0}
month_change = []
month = []
is_first_row = True


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
        
        #Prepare for next month
        prev_profit = curr_profit 

        if total_months > 1:
            month_list = row[MONTH_IDX]
            month_change.append(curr_change)
            month.append(month_list)
            #Find Greatest increase and decrease
            if curr_change > maximum_profit["amount"]:
                maximum_profit["month"] = month_list
                maximum_profit["amount"] = curr_change
            if curr_change < decrease_profit["amount"]:
                decrease_profit["month"] = month_list
                decrease_profit["amount"] = curr_change

    average_change = total_change / (total_months - 1) 
    rounded_average_change = round(average_change, 2)

        
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_months)
print("Total:", "$",total_profit)
print(f"Average Change:, ${rounded_average_change}")
print(f"Greatest Increase in Profits:,  {maximum_profit['month']} (${maximum_profit['amount']})")
print(f"Greatest Decrease in Profits:, {decrease_profit['month']} (${decrease_profit['amount']})")

