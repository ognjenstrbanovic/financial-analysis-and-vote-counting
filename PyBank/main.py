# Importing the os module allows us to create file paths across operating systems
import os
# The csv module is for reading CSV files
import csv
# Set the path for the file
csv_path = os.path.join("PyBank", "budget_data.csv")
# Open the CSV file (with the delimiter at the comma)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # For readability, print the following to the terminal...
    print("Financial Analysis")
    print("----------------------------")
    # For loop through the CSV file to calculate the total number of months included in the dataset, the net total amount of profit or losses over the entire period, as well as the average of the changes in Profit/Losses over the entire period (using the next function to exclude the header)
    csv_header = next(csv_reader)
    # Create two empty lists and append items to them through iteration
    total_number_of_months = []
    net_total_amount_of_profit_or_losses = []
    for row in csv_reader:
        total_number_of_months.append(row[0])
        net_total_amount_of_profit_or_losses.append(int(row[1]))
    # Print to the terminal using f-strings
    print(f"Total Months: {len(total_number_of_months)}")
    print(f"Total: ${sum(net_total_amount_of_profit_or_losses)}")
    index = 0
    profit_or_loss = []
    while index < (len(total_number_of_months) - 1):
        profit_or_loss.append(int(net_total_amount_of_profit_or_losses[index + 1]) - int(net_total_amount_of_profit_or_losses[index]))
        index += 1
    average_of_changes_in_profit_or_losses = 0
    for element in profit_or_loss:
        average_of_changes_in_profit_or_losses += float(element) / len(profit_or_loss)
    # Rounding to 2 decimal places...
    rounded_average_of_changes_in_profit_or_losses = round(average_of_changes_in_profit_or_losses, 2)
    print(f"Average Change: ${rounded_average_of_changes_in_profit_or_losses}")
    greatest_increase_profits_amount = max(profit_or_loss)
    profit_or_loss.index(1926159)
    greatest_increase_profits_date = total_number_of_months[24 + 1]
    # Formatted strings didn't seem to work at first, so I used the str() method
    print("Greatest Increase in Profits: " + str(greatest_increase_profits_date) + " ($" + str(greatest_increase_profits_amount) + ")")
    greatest_decrease_losses_amount = min(profit_or_loss)
    profit_or_loss.index(-2196167)
    greatest_decrease_losses_date = total_number_of_months[43 + 1]
    print("Greatest Decrease in Losses: " + str(greatest_decrease_losses_date) + " ($" + str(greatest_decrease_losses_amount) + ")")
# Specify the file to write to and open a file using "write" mode in order to export a text file with the results
output_path = os.path.join("PyBank_results.txt")
with open(output_path, 'w', newline='') as txt_file:
    # \n means newline
    txt_file.write("Financial Analysis\n-------------------------\n")
    txt_file.write(f"Total Months: {len(total_number_of_months)}""\n")
    txt_file.write(f"Total: ${sum(net_total_amount_of_profit_or_losses)}""\n")
    txt_file.write(f"Average Change: ${rounded_average_of_changes_in_profit_or_losses}""\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase_profits_date) + " ($" + str(greatest_increase_profits_amount) + ")""\n")
    txt_file.write("Greatest Decrease in Losses: " + str(greatest_decrease_losses_date) + " ($" + str(greatest_decrease_losses_amount) + ")")