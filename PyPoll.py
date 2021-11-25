#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


#Add our dependencies.
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize variable to count votes & get candidates
total_votes = 0
candidate_options = []

#Open the election results and read the file
with open(file_to_load) as election_data:

   #Read the file object with the reader function.
   file_reader = csv.reader(election_data)
   
   #Read the header row
   headers = next(file_reader)
   
   #Print each row in the CSV file
   for row in file_reader:
   
    #increase total votes by 1
    total_votes += 1

    #get candidate name
    candidate_name = row[2]

    #add candidate name to list if its not on the list
    if candidate_name not in candidate_options:
        
        candidate_options.append(candidate_name)

#Print the total votes
#print(total_votes)
#Print the Candidate List
print(candidate_options)

