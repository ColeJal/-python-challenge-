import os
import csv


budget_data = os.path.join("Resources","budget_data.csv")

Revenue = []
Date = []
Gains_Change = []
Change_Monthly = []
Gains_Change_row = []
Gains_Average = []

Date = 0
Gains_Totals = 0
previous_gains = 0 
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]



with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header= next(csvfile)
    print(f"Header:{csv_header}")

    for row in csvreader:
        Date = Date + 1
        
        Revenue.append(row[1])
        Gains_Totals = Gains_Totals + int(row[1])
           
        gains_change = int(row[1]) - previous_gains
        previous_gains = int(row[1])
        Gains_Change_row = Gains_Change_row +[Gains_Change]
        Change_Monthly = Change_Monthly + [row[0]]

        if (gains_change > greatest_increase[1]):
            greatest_increase[0] = row[1]
            greatest_increase[1] = gains_change

        if(gains_change < greatest_decrease[1]):
            greatest_decrease[0] = row[1]
            greatest_decrease[1] = gains_change





print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months:" +" "+ str(Date))
print(f"Total:" +" $"+ str(Gains_Totals))

print(f"Greatest Increase in Profits:" +"$"+str(greatest_increase[1])) 
print(f"Greatest Decrease in Profits:" +"$" +str(greatest_decrease[1]))

with open('financial_analysis.text', 'w') as text:
    text.write("Financial Analysis")
    text.write("-----------------------------------------")
    text.write(f"Total Months:" +" "+ str(Date))
    text.write(f"Total:" +" $"+ str(Gains_Totals))
    
    text.write(f"Greatest Increase in Profits:" +"$"+str(greatest_increase[1])) 
    text.write(f"Greatest Decrease in Profits:" +"$"+str(greatest_decrease[1]))

