import os
import csv

election_data = os.path.join("..","resources","election_data.csv")

with open(election_data,'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ",")

    csv_header= next(csv_file)
    print(f"Header:{csv_header}")