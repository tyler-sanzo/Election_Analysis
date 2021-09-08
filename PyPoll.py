### data needed
# total number of votes cast
# names of each candidate
# votes for each candidate
# vote percentage each candidate won
# winner based on popular vote
import os
import csv
# Assign a variable for the file to load and the path.
#file_to_load = 'Election Results\Resources\election_results.csv'
file_to_load = os.path.join("Python - Pypoll", "Resources", "election_results.csv")

with open(file_to_load) as election_data:
    
    #To do: Perform Analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file that will be used to write into.
file_to_save = os.path.join("Python - Pypoll", "analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.

# Method 1
'''
#create writable variable
outfile = open(file_to_save, 'w')
#write something into the file
outfile.write('HeLLo wORld')
#close
outfile.close()
'''


# Method 2: cleaner
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Hello World')


#adding multiple lines
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Arapahoe\nJefferson\nDenver')


#adding header and dashed line above text
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Counties in the Election\n-----------------\nArapahoe\nJefferson\nDenver')


#vote counter
total_votes = 0
#candidate list
candidate_options = []
#declare empty dictionary to store candidate votes
candidate_votes = {}
#open election results and read the file 

#Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:

    #read and analyze data here
    file_reader = csv.reader(election_data)

    #read and print header row
    #using next skips a single row starting from the top
    headers = next(file_reader)
    print(headers)
    
    
    for row in file_reader:
        #total vote counter
        total_votes+=1

        #read candidate name from each row
        candidate_name = row[2]

        #append name to candidate list
        #only add unique names to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking candidate votes
            candidate_votes[candidate_name] = 0 

        #tally candidate votes
        candidate_votes[candidate_name]+=1

#iterating through candidate list to find num of votes for each candidate
for candidate_name in candidate_options:

    #vote count for each candidate
    votes = candidate_votes[candidate_name]

    #calculate vote percentage
    vote_percentage = float(votes)/float(total_votes) * 100

    #print each candidate and their vote percentage
    #formatted to print 1 decimal of vote percentage
    print(f'{candidate_name} recieved {vote_percentage:.1f}% of the votes')

    #declaring winning values
    if votes > winning_count and vote_percentage > winning_percentage :
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name


#print(candidate_options)

#print(total_votes)

#print(candidate_votes)

#winning candidate summary
winner_summary = (
    f'---------------------\n'
    f'Winner : {winning_candidate}\n'
    f'Winning Vote Count : {winning_count:,}\n'
    f'Vote Percentage : {winning_percentage:.1f}%\n'
    f'---------------------\n'
)

print(winner_summary)

with open(file_to_save,'w') as output:
    output.write(winner_summary)
