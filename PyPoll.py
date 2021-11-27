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

#Initialize variable to count votes & get candidates & votes
total_votes = 0
candidate_options = []
candidate_votes = {}
 #initialize variables to hold winning candidate and counts
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#save the results to text file
with open(file_to_save, "w") as txt_file:
            
    #Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")
    #Save final vote count to the text file.
    txt_file.write(election_results) 

    #Determine the % of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage =  float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        #4. Print the candidate name and percentage of votes.
        print(candidate_results)
        #save the candidate results to text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's results to text file
    txt_file.write(winning_candidate_summary)