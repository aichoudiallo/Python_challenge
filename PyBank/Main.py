import csv 
import os

filepath= os.path.join("Ressources","budget_data.csv")
output_file=os.path.join("analysis","analysis.txt")

total_months= 0
total_net= 0

month= []
change= []
max_increase= ["", 0]
max_decrease = ['',1000000000]

total_profit=[]
monthly_profit_change=[]
max_increase_month=[]
max_decrease_month=[]
max_increase_value=[]
max_decrease_value=[]

with open (filepath) as data:
    reader= csv.reader(data)
    header= next(reader)
    first_row= next (reader)
    # total_months= total_months+1
    total_months+=1
    total_net= total_net+int(first_row[1])
    previous= int(first_row[1])

    for row in reader:
        total_months+=1
        total_net= total_net+int(row[1])
        net_change= int(row[1])- previous
        previous= int(row[1])
        change+=[net_change]
        month+=[row[0]]

        if net_change > max_increase[1]:
            max_increase[0]=row[0]
            max_increase[1]=net_change

            ElIf net_change < max_decrease[1]:
        max_decrease[0]=row[0]
        max_decrease[1]= net_change


# calculate avg sum(change)/len(change)
    for i in range(len(change)-1):
      monthly_profit_change.append(total_profit[i+1]-total_profit[i])




out=(f"{total_months}")

print(out)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

with open(output_file, "w") as file:
    file.write(out)

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")