import csv
import os

filepath= os.path.join("Ressources","election_data.csv")
output_file=os.path.join("Analysis","Analysis.txt")

candidates=[]
all_candidates=[]
candidate_votes={}
percent_list=[]
winning_count=0
winner=""
data={}
total=0

with open(filepath) as file: 
    reader = csv.reader(file) 
    header=next(reader)
    for row in reader: 
        total+=1 
        candidate_name=row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

       
with open (output_file,"w") as file:


    # print(candidates)
   
    output= f"""
Election Results
____________________________

Total Votes: {total:,}
____________________________\n"""

    print(output)
    file.write(output)




    for name in candidate_votes:
        votes=candidate_votes.get(name)
        percentage=votes/total*100

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



