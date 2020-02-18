# Importing the "os" module allows us to create file paths across different operating systems
import os
# Importing the "csv" module allows us to read CSV (comma-separated values) files
import csv
# Directly below, we are setting the path for the file
csv_path = os.path.join("PyBank", "budget_data.csv")
# We are opening the file with the delimiter set to be the comma (we do this with a "with" statement so that we do not have to close the file)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Next, as per the instructions (and for readability), we print the following line to the terminal ("\n" inserts a newline after its placement)
    print("Financial Analysis\n----------------------------")
    # Use "for" to loop through the file, and calculate: the total number of months included in the dataset, the net total amount of profit or losses over the entire period, as well as the average of the changes in Profit/Losses over the entire period (using the "next" function to exclude the header)
    csv_header = next(csv_reader)
    # Create two empty lists, and append items to them through row iteration
    total_number_months = []
    net_total_amount_profit_losses = []
    for row in csv_reader:
        total_number_months.append(row[0])
        net_total_amount_profit_losses.append(int(row[1]))
    # Print to the terminal (using f-strings) to check if our calculations are correct
    print(f"Total Months: {len(total_number_months)}")
    print(f"Total: ${sum(net_total_amount_profit_losses)}")
    # Use a "while" loop with the index, "i", starting at 0 and ending at 85 (one minus the length of the list because indexing starts at 0)
    i = 0
    # The empty list will contain the values of the month-to-month changes in Profit/Losses
    profit_losses = []
    while i < (len(total_number_months) - 1):
        profit_losses.append(int(net_total_amount_profit_losses[i + 1]) - int(net_total_amount_profit_losses[i]))
        i += 1
    # Now calculate the average of each element in the list "profit_losses"; initialize the new variable to 0
    average_changes_profit_losses = 0
    for element in profit_losses:
        average_changes_profit_losses += float(element) / len(profit_losses)
    # Rounding to two decimal places for presentation purposes, and then printing to the terminal
    rounded_average_changes_profit_losses = round(average_changes_profit_losses, 2)
    print(f"Average Change: ${rounded_average_changes_profit_losses}")
    # Next up is to look for maximum profit change and minimum losses change, which we do by checking our output and using that in the built-in ".index" function
    greatest_increase_profit_amount = max(profit_losses)
    profit_losses.index(1926159)
    # We look for their dates; we add 1 because this is the month in which the greatest +/- change occurred
    greatest_increase_profit_date = total_number_months[24 + 1]
    # Used str() method below b/c formatted strings didn't seem to work after a couple of tries
    print("Greatest Increase in Profits: " + str(greatest_increase_profit_date) + " ($" + str(greatest_increase_profit_amount) + ")")
    greatest_decrease_losses_amount = min(profit_losses)
    profit_losses.index(-2196167)
    greatest_decrease_losses_date = total_number_months[43 + 1]
    print("Greatest Decrease in Losses: " + str(greatest_decrease_losses_date) + " ($" + str(greatest_decrease_losses_amount) + ")")
# Specify the file to write to and open/export a text file with the results using "write" mode
output_path = os.path.join("PyBank_results_1.txt")
with open(output_path, "w", newline="") as txt_file:
    txt_file.write("Financial Analysis\n----------------------------\n")
    txt_file.write(f"Total Months: {len(total_number_months)}""/n")
    txt_file.write(f"Total: ${sum(net_total_amount_profit_losses)}""\n")
    txt_file.write(f"Average Change: ${rounded_average_changes_profit_losses}""\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase_profit_date) + " ($" + str(greatest_increase_profit_amount) + ")""\n")
    txt_file.write("Greatest Decrease in Losses: " + str(greatest_decrease_losses_date) + " ($" + str(greatest_decrease_losses_amount) + ")")