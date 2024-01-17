# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:20:29 2024

@author: 14407
"""

# Importing modules important for the analysis
import os
import csv
# Set relative path for csv file

# Specify the file path
budget_csv = os.path.join('C:\\Users\\14407\\Documents\\Data Analytics_Boot Camp\\Module 3\\Starter_Code\\PyBank\\Resources', 'budget_data.csv')

# counter for total number of months
total_months = 0

# counter for the total profit and loss
total_profit_loss = 0

# counter for the output value of total profit and loss
value = 0

# counter for the output value of profit and loss changes
change = 0

# List to hold dates and profit/losses
dates = []
profits = []

# Open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read header row and start on first row
    csv_header = next(csvreader)
    first_row = next(csvreader)

    # add counters
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    
    # Read the rows after the header row
    for row in csvreader:

        # Get date
        dates.append(row[0])

        # Keep the the records of changes in rows
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        # Total the number of months
        total_months += 1

        # Calculate Net profit/ losses
        total_profit_loss = total_profit_loss + int(row[1])

        # Calculate the average changes in "Profit/Losses" over the entire period
        avg_change = sum(profits)/len(profits)
        
  # Calculate the greatest increase in profits
    greatest_increase = max(profits)
    greatest_inc_index = profits.index(greatest_increase)
    greatest__inc_date = dates[greatest_inc_index]

  #Calculate the greatest decrease in profits
    greatest_decrease = min(profits)
    greatest__dec_index = profits.index(greatest_decrease)
    greatest__dec_date = dates[greatest__dec_index]

#Print the analysis output
printoutput = (
    f"Analysis\n"
    f"-------------------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})\n")
print(printoutput)

# Export to text file

output_file = os.path.join('C:\\Users\\14407\\Documents\\Data Analytics_Boot Camp\\Module 3\\Starter_Code\\PyBank\\Analysis\\pyBank_output.txt')


pyBankoutput = open(output_file, "w")

line1 = "Analysis"
line2 = "------------------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})")
line7 = str(
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})")
pyBankoutput.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))
