import os
import csv

budget_data = os.path.join('..','Resources','budget_data.csv')

with open(budget_data,'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ",")

    csv_header= next(csv_file)
    print(f"Header:{csv_header}")

Date_Year=0
Revenue_Gains_Losses=0

for row in csv_reader:
    Date_Year.append(row[0])
    Revenue_Gains_Losses.append(int(row[1]))
Date_Total=sum(Date_Year)
