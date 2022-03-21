import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)
    # print(csv_header)

    # initialize variable to count the number of months in the dataset
    month_count = 0
    net_amount = 0

    # initialize empty lists
    profit_loss = []
    month_year = []

    for row in csvreader:
        profit_loss.append(float(row[1]))
        month_year.append(row[0])
        month_count = month_count + 1
        net_amount = net_amount + float(row[1])  


    # find greatest increase in list
    change_profit_loss = [0]
    greatest_increase = 0
    
    for x in range(len(profit_loss)-1):
        change = profit_loss[x+1] - profit_loss[x]
        change_profit_loss.append(change)

        if change_profit_loss[x+1] > greatest_increase:
            greatest_increase = change_profit_loss[x+1]

    # print(change_profit_loss)
    # print(greatest_increase)
    greatest_ind = change_profit_loss.index(greatest_increase)

robustness_month_count = len(month_year)
# print(profit_loss)
# print(month_year)
# print(f"Robustness month count: {robustness_month_count} ")
    # print results to the terminal
print("Financial Analysis ")
print("--------------------------- ")
print(f"Total Months: {month_count} ")
print(f"Total: {net_amount} ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: {month_year[greatest_ind]} {greatest_increase} ")
