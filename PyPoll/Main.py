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

        # all_candidates.append(row[2]) 
        # if row[2] in candidates: 
        #     continue
        # else:
        #     candidates.append(row[2]) 
# total-=1
# for i in range(1,len(candidates)):
#     count=0 
#     for j in range(len(all_candidates)):
#         if candidates[i]==all_candidates[j]:
#             count+=1
#     data[candidates[i]]=count 
# candidates.remove(candidates[0])

with open (output_file,"w") as file:


    # print(candidates)
   
    output= f"""
Election Results
____________________________

Total Votes: {total:,}
____________________________\n"""

    print(output)
    file.write(output)


    # print("Election Results")
    # print("____________________________\n")
    # print("Total Votes: %d"%total) #printing the total votes
    # print("____________________________\n")

    for name in candidate_votes:
        votes=candidate_votes.get(name)
        percentage=votes/total*100

        if votes> winning_count:
            winning_count=votes
            winner=name

        candidate_output=f"{name}: {percentage:.2f}% ({votes:,})\n"
        print(candidate_output)
        file.write(candidate_output)
    # for i in candidates:
    #     percentage=(data[i]/total)*100 #finding the percentage of each candidate
    #     percent_list.append(percentage) #appending the precentage to percent_list
    #     # print("%s : %f(%d)"%(i,percentage,data[i]))
    #     # candidate_output= f"{i,percentage,data[i]}"
    #     candidate_output= f"{i,percentage,data[i]}"
        
    
    winning_candidate=f"""
____________________________

Winner: {winner}
____________________________

    """
    print(winning_candidate)

#     print("____________________________\n")
#     print("Winner:",candidates[percent_list.index(max(percent_list))]) #declaring the winner of the election
#     print("____________________________\n")

    # file.write(output)
    # file.write(candidate_output)
    file.write(winning_candidate)


