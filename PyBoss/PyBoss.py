import os
import csv
csv_path = os.path.join("PyBoss", "employee_data.csv")
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    full_names = []
    for row in csv_reader:
        full_names.append(row[1])
    first_names = []
    last_names = []
    for full_name in full_names:
        full_name.split(" ")
        print(full_name)