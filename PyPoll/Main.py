# Dependencies
import csv
import os

# set path to import and export csvs
filepath= os.path.join("Ressources","election_data.csv")
output_file=os.path.join("Analysis","Analysis.txt")

# variables
candidates=[]
candidate_votes={}
winning_count=0
winner=""
total=0

# read in csv
with open(filepath) as file: 
    reader = csv.reader(file) 
    
    # store the header
    header=next(reader)

    # for loop to gather data
    for row in reader: 
        total+=1 
        candidate_name=row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

# print and export the requested deliverable
with open (output_file,"w") as file:

   
    output= f"""
Election Results
____________________________

Total Votes: {total:,}
____________________________\n"""

    print(output)
    file.write(output)



    # calculate candidate vote count and percentage
    for name in candidate_votes:
        votes=candidate_votes.get(name)
        percentage=votes/total*100

        # determine the winner
        if votes> winning_count:
            winning_count=votes
            winner=name

        candidate_output=f"{name}: {percentage:.2f}% ({votes:,})\n"
        print(candidate_output)
        file.write(candidate_output)

    
    winning_candidate=f"""
____________________________

Winner: {winner}
____________________________

    """
    print(winning_candidate)
    file.write(winning_candidate)


