#Add dependencies
import csv
import os

#Assign a variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file
file_to_save = os.path.join("Analysis", "election_results.txt")

#Initialize a total vote counter
total_votes = 0

#Create list of candidate options
candidate_options = []

#Declare dictionary of candidate votes
candidate_votes = {}

#Track winning candidtae, vote count, and percentage
#Declare variable for winning candidate
winning_candidate = ""
#Declare variable for winning count and set to zero
winning_count = 0
#Declare variable for sinning percentage and set to zero
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #Add each row to total votes
    for row in file_reader:
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the cnadidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add to list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0

        #Add the vote to the candidate vote count
        candidate_votes[candidate_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:
    #Print final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save final vote count to text file
    txt_file.write(election_results)

    #Determine percentage of votes for each candidate
    #Iterate through candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set new values
            winning_count = votes
            winning_percentage = vote_percentage
            #Set winning candidate
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentge: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary) 
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)