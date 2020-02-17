# Importing the os module allows us to create file paths across operating systems
import os
# The csv module is for reading CSV files
import csv
# Set the path for the file
csv_path = os.path.join("budget_data.csv")
# Open the CSV file
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    print("Financial Analysis")
    print("----------------------------")
# For loop through the CSV file to calculate the total number of months included in the dataset (using the next function to exclude the header)
    csv_header = next(csv_reader)
    total_number_of_months = []
    for month in csv_reader:
        total_number_of_months.append(month[0])
    print(f"Total Months: {len(total_number_of_months)}")