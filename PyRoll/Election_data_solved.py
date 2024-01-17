# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:54:45 2024

@author: 14407
"""



# Import modules 
import os
import csv

# Specifiy the file path

election_csv = os.path.join('C:\\Users\\14407\\Documents\\Data Analytics_Boot Camp\\Module 3\\Starter_Code\\PyPoll\\Resources', 'election_data.csv')

# Create lists to store data

num_votes = 0
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV 

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

    for row in csvreader:
        
        # Count the total number of votes
        num_votes = num_votes + 1
        
        # Add candidate names to a candidate list
        candidates.append(row[2])
        
        # Create list for unique candidate names
    for x in set(candidates):
        unique_candidate.append(x)
        
        # y is the total number of votes per candidate
        y = candidates.count(x)
        vote_count.append(y)
        
        # z is the percent of total votes per candidate
        z = (y/num_votes)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    

# Print the analysis output
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(num_votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Export to text file

output_file = os.path.join('C:\\Users\\14407\\Documents\\Data Analytics_Boot Camp\\Module 3\\Starter_Code\\PyPoll\\Resources', 'election_data.csv')