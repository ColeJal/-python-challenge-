import os
import csv

election_data = os.path.join("resources","election_data.csv")

Votes = []
Runners_Votes = []


Victor_Runner = ""
Victor_talley = 0
Available_runners= []

Votes = 0


with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ",")

    csv_header= next(csv_file)
    print(f"Header:{csv_header}")

    for row in csv_reader:
        Votes = Votes + 1

        candidate_running = row[2]

        if candidate_running not in Runners_Votes:

            Runners_Votes.append(row[2])



            

    

   










print("Election Results")
print("----------------------------------------")
print(f"Total Votes:" + " "+ str(Votes))
print("----------------------------------------")

with open('Election_Results.text', 'w') as text:
    text.write("Election Results")
    text.write("----------------------------------------")
    text.write(f"Total Votes:" + " "+ str(Votes))
    text.write("----------------------------------------")