# Dependencies
import csv 
import os

# set path to import and export csvs
filepath= os.path.join("Ressources","budget_data.csv")
output_file=os.path.join("analysis","analysis.txt")

# variables
total_months= 0
total_net= 0

month= []
change= []
max_increase= ["", 0]
max_decrease = ['',1000000000]


# read in csv
with open (filepath) as data:
    reader= csv.reader(data)

    # store the header

    header= next(reader)

    #Gather information from the first row
    first_row= next (reader)
    # total_months= total_months+1
    total_months+=1
    total_net= total_net+int(first_row[1])
    previous= int(first_row[1])

    # for loop to gather data
    for row in reader:
        total_months+=1
        total_net= total_net+int(row[1])
        net_change= int(row[1])- previous
        previous= int(row[1])
        change+=[net_change]
        month+=[row[0]]

        # Determine the month and value of maximum profit
        if net_change > max_increase[1]:
            max_increase[0]=row[0]
            max_increase[1]=net_change

        # Determine the month and value of maximum loss
        if net_change < max_decrease[1]:
            max_decrease[0]=row[0]
            max_decrease[1]= net_change



# print and export the requested deliverable
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

with open(output_file, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total_net}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change)/len(change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")