# Importing the os module allows us to create file paths across operating systems
import os
# The csv module is for reading CSV files
import csv
# Set the path for the file
csv_path = os.path.join("PyPoll", "election_data.csv")
# Open the CSV file (with the delimiter at the comma)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
# For readability, and per instructions, print the following to the terminal...
    print("Election Results")
    print("-------------------------")
    # For loop through the CSV file to calculate the total number of votes cast, the complete list of candidates who received who received votes, the percentage of votes that each candidate won, as well as the total number of votes each candidate won (using the next function to exclude the header)
    csv_header = next(csv_reader)
    total_number_votes_cast = []
    candidate_list = []
    Khan_counter = 0
    Correy_counter = 0
    Li_counter = 0
    fourth_candidate_counter = 0
    for row in csv_reader:
        total_number_votes_cast.append(row[0])
        # We could potentially use a switch statement for all of these if statements
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == "Khan":
            Khan_counter += 1
        if row[2] == "Correy":
            Correy_counter += 1
        if row[2] == "Li":
            Li_counter += 1
        if row[2] == "O'Tooley":
            fourth_candidate_counter += 1
    print(f"Total Votes: {len(total_number_votes_cast)}")
    print("-------------------------")
    Khan_unformatted = Khan_counter / len(total_number_votes_cast)
    Khan_percentage = format(Khan_unformatted, ".3%")
    print(f"{candidate_list[0]}: {Khan_percentage} ({Khan_counter})")
    Correy_unformatted = Correy_counter / len(total_number_votes_cast)
    Correy_percentage = format(Correy_unformatted, ".3%")
    print(f"{candidate_list[1]}: {Correy_percentage} ({Correy_counter})")
    Li_unformatted = Li_counter / len(total_number_votes_cast)
    Li_percentage = format(Li_unformatted, ".3%")
    print(f"{candidate_list[2]}: {Li_percentage} ({Li_counter})")
    fourth_candidate_unformatted = fourth_candidate_counter / len(total_number_votes_cast)
    fourth_candidate_percentage = format(fourth_candidate_unformatted, ".3%")
    print(f"{candidate_list[3]}: {fourth_candidate_percentage} ({fourth_candidate_counter})")
    print("-------------------------")
    print(f"Winner: {candidate_list[0]}")
    print("-------------------------")
# Specify the file to write to and open a file using "write" mode in order to export a text file with the results
output_path = os.path.join("PyPoll_results.txt")
with open(output_path, 'w', newline='') as txt_file:
    txt_file.write("Election Results\n-------------------------\n")
    txt_file.write(f"Total Votes: {len(total_number_votes_cast)}""\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{candidate_list[0]}: {Khan_percentage} ({Khan_counter})""\n")
    txt_file.write(f"{candidate_list[1]}: {Correy_percentage} ({Correy_counter}""\n")
    txt_file.write(f"{candidate_list[2]}: {Li_percentage} ({Li_counter})""\n")
    txt_file.write(f"{candidate_list[3]}: {fourth_candidate_percentage} ({fourth_candidate_counter})""\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {candidate_list[0]}""\n")
    txt_file.write("-------------------------")