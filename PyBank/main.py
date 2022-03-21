import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)

    # initialize variable to count the number of months and net profit in the dataset
    month_count = 0
    net_amount = 0

    # initialize empty lists to hold monthly profit/losses and dates, respectively
    profit_loss = []
    month_year = []

    # read through rows of csv and generate profit_loss and month_year lists
    for row in csvreader:
        profit_loss.append(float(row[1]))
        month_year.append(row[0])

        # get the total number of months and the net profit
        month_count = month_count + 1
        net_amount = net_amount + float(row[1])  


    # find greatest increase in list
    change_profit_loss = [0]
    greatest_increase = 0
    greatest_decrease = 0
    
    # calculate the month-to-month change in profit and add value to list change_in_profit
    for x in range(len(profit_loss)-1):
        change = profit_loss[x+1] - profit_loss[x]
        change_profit_loss.append(change)

        # look for greatest increase/decrease in profit respectively 
        if change_profit_loss[x+1] > greatest_increase:
            greatest_increase = change_profit_loss[x+1]
        if change_profit_loss[x+1] < greatest_decrease:
            greatest_decrease = change_profit_loss[x+1]

    # assign variables that hold the index of the greatest increase/decrease in profit respectively from list change_profit_loss
    increase_ind = change_profit_loss.index(greatest_increase)
    decrease_ind = change_profit_loss.index(greatest_decrease)

    # calculate the total month-to-month changes in profit
    sum_change = 0
    for x in range(1,len(change_profit_loss)):
        sum_change = sum_change + change_profit_loss[x]
    
    # divide total month-to-month changes in profit by the number of months (minus Jan-10 since that's the starting value)
    average_change = sum_change / (len(change_profit_loss) - 1)

# format dollar amounts as currency
net_amount = "${:,.2f}".format(net_amount)
average_change = "${:,.2f}".format(average_change)
greatest_increase = "${:,.2f}".format(greatest_increase)
greatest_decrease = "${:,.2f}".format(greatest_decrease)

# generate list that summarizes each line of output
output_list =  ["Financial Analysis ",
                "--------------------------- ",
                f"Total Months: {month_count} ",
                f"Total: {net_amount} ",
                f"Average Change: {average_change} ",
                f"Greatest Increase in Profits: {month_year[increase_ind]} ({greatest_increase}) ",
                f"Greatest Decrease in Profits: {month_year[decrease_ind]} ({greatest_decrease}) "]


# loop through lines of output and print to terminal
for line in output_list:
    print(line)


# export results into a .txt file
output_path = os.path.join('Analysis','pybank-results.txt')

with open(output_path, 'w') as txtout:
    txtout.write('\n'.join(output_list))


