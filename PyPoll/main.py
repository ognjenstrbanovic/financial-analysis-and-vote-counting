# Importing the "os" module allows us to create file paths across different operating systems
import os
# Importing the "csv" module allows us to read CSV (comma-separated values) files
import csv
# Directly below, we are setting the path for the file
csv_path = os.path.join("election_data.csv")
# We are opening the file with the delimiter set to be the comma (we do this with a "with" statement so that we do not have to close the file)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Next, as per the instructions (and for readability), we print the following line to the terminal ("\n" inserts a newline after its placement)
    print("Election Results\n-------------------------")
    # Use "for" to loop through the file, and calculate: the total number of votes cast, the complete list of candidates who received votes, the percentage of votes that each candidate won, as well as the total number of votes that each candidate won (using the "next" function to exclude the header)
    csv_header = next(csv_reader)
    # Create two empty lists, and append items to them through row iteration; initialize each candidate's counter to 0
    total_number_votes_cast = []
    candidate_list = []
    Khan_counter = 0
    Correy_counter = 0
    Li_counter = 0
    fourth_candidate_counter = 0
    for row in csv_reader:
        # The first column of each row contains each of the votes cast
        total_number_votes_cast.append(row[0])
        # The candidates appear in the third column; if they are not in my newly-created list, "candidate_list", then append them to said list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        # If, for example, "Khan" appears in column 3, then add a vote to his name via "Khan_counter"
        if row[2] == "Khan":
            Khan_counter += 1
        if row[2] == "Correy":
            Correy_counter += 1
        if row[2] == "Li":
            Li_counter += 1
        if row[2] == "O'Tooley":
            fourth_candidate_counter += 1
        # We could potentially use a switch statement instead of all of these "if" statements that are above
    # Print to the terminal (using f-strings, which uses less syntax) to check if our calculations are correct
    print(f"Total Votes: {len(total_number_votes_cast)}""\n""-------------------------")
    # To get each candidate's percentage, we use the "format" function; then, we print for each
    Khan_unformatted = Khan_counter / len(total_number_votes_cast)
    Khan_percentage = format(Khan_unformatted, ".3%")
    print(f"{candidate_list[0]}: {Khan_percentage} ({Khan_counter:,})")
    Correy_unformatted = Correy_counter / len(total_number_votes_cast)
    Correy_percentage = format(Correy_unformatted, ".3%")
    print(f"{candidate_list[1]}: {Correy_percentage} ({Correy_counter:,})")
    Li_unformatted = Li_counter / len(total_number_votes_cast)
    Li_percentage = format(Li_unformatted, ".3%")
    print(f"{candidate_list[2]}: {Li_percentage} ({Li_counter:,})")
    fourth_candidate_unformatted = fourth_candidate_counter / len(total_number_votes_cast)
    fourth_candidate_percentage = format(fourth_candidate_unformatted, ".3%")
    print(f"{candidate_list[3]}: {fourth_candidate_percentage} ({fourth_candidate_counter:,})")
    print("-------------------------")
    # The results in terminal make it obvious to us who the winner is of the election
    print(f"Winner: {candidate_list[0]}")
    print("-------------------------")
# Specify the file to write to and open/export a text file with the results using "write" mode
output_path = os.path.join("PyPoll_results.txt")
with open(output_path, 'w', newline='') as txt_file:
    txt_file.write("Election Results\n-------------------------\n")
    txt_file.write(f"Total Votes: {len(total_number_votes_cast)}""\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{candidate_list[0]}: {Khan_percentage} ({Khan_counter:,})""\n")
    txt_file.write(f"{candidate_list[1]}: {Correy_percentage} ({Correy_counter:,})""\n")
    txt_file.write(f"{candidate_list[2]}: {Li_percentage} ({Li_counter:,})""\n")
    txt_file.write(f"{candidate_list[3]}: {fourth_candidate_percentage} ({fourth_candidate_counter:,})""\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {candidate_list[0]}""\n")
    txt_file.write("-------------------------")
