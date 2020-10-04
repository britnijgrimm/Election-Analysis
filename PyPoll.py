#The data that needs to be retrieved
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#Imports
import csv
import os

#Assign a variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file
file_to_save = os.path.join("Analysis", "election_results.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)