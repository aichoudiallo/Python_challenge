import csv
import os

filepath= os.path.join("Ressources","election.data.csv")
output_file=os.path.join("Analysis","Analysis.txt")

candidates=[]
all_candidates=[]
percent_list=[]
data={}
total=0

with open('election_data.csv', 'r') as file: 
    reader = csv.reader(file) 
    for row in reader: 
        total+=1 
        all_candidates.append(row[2]) 
        if row[2] in candidates: 
            continue
        else:
            candidates.append(row[2]) 
total-=1
for i in range(1,len(candidates)):
    count=0 
    for j in range(len(all_candidates)):
        if candidates[i]==all_candidates[j]:
            count+=1
    data[candidates[i]]=count 
candidates.remove(candidates[0])


print("Election Results")
print("____________________________\n")
print("Total Votes: %d"%total) #printing the total votes
print("____________________________\n")
for i in candidates:
    percentage=(data[i]/total)*100 #finding the percentage of each candidate
    percent_list.append(percentage) #appending the precentage to percent_list
    print("%s : %f(%d)"%(i,percentage,data[i]))
print("____________________________\n")
print("Winner:",candidates[percent_list.index(max(percent_list))]) #declaring the winner of the election
print("\t____________________________\n")