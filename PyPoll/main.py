import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
file_txt  = os.path.join("Analysis", "output.txt")
file_txt  = os.path.join("Analysis", "output.txt")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    votes_count = 0
    candidates = []
    list_of_votes = []

    for row in csvreader:
        votes_count += 1
        list_of_votes.append(row[2])
        
        if row[2] not in candidates:
            candidates.append(row[2])
       
    
    votes={}
    most_votes = 0
    
    for person in candidates:
        counter = 0

        for i in list_of_votes:
            if i == person:
            
                counter += 1
        percentage = counter/votes_count
        votes[person] = [percentage, counter]
        
        if counter >= most_votes:
            most_votes = counter
            winner = person
        
       
   
with open(file_txt,"w") as f:
    print("\nElection Results \n----------------------------------------", file = f)
    print("\nTotal Votes: " , votes_count, file = f)
    print("\n----------------------------------------", file = f)
    for k, v in votes.items():
        print(f"{k:<10} {v[0]: .3%} ({v[1]})", file = f)
    print("\n----------------------------------------", file = f)
    print("\nWinner: " +  winner, file = f)
    print("\n----------------------------------------", file = f)
    print("\nElection Results \n----------------------------------------")
    print("\nTotal Votes: " , votes_count)
    print("\n----------------------------------------")
    for k, v in votes.items():
        print(f"{k:<10} {v[0]: .3%} ({v[1]})")
    print("\n----------------------------------------")
    print("\nWinner: " +  winner)
    print("\n----------------------------------------")
    
