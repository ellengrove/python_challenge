import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)
    # print(csv_header)

    candidate_votes_all = []
    vote_count = 0
    for row in csvreader:
        vote_count = vote_count + 1
        candidate_votes_all.append(row[2])

    candidates = []
    # get list of all candidates
    # consider using list compression
    for candidate in candidate_votes_all:
        if candidate not in candidates:
            candidates.append(candidate)


    candidate_votes = []
    candidate_vote_percent = []
    tally = 0
    for candidate in candidates:
        for vote in candidate_votes_all:
            if vote == candidate:
                tally = tally + 1
        candidate_votes.append(tally)
        candidate_vote_percent.append("{0:.3%}".format((tally / vote_count)))
        tally = 0

winner_votes = max(candidate_votes)
winner = candidates[candidate_votes.index(winner_votes)]

# improve this 
output_list = ["Election Results ",
               "---------------------------- ",
               f"Total Votes: {vote_count} ",
               "---------------------------- ",
               f"{candidates[0]}: {candidate_vote_percent[0]} ({candidate_votes[0]})",
               f"{candidates[1]}: {candidate_vote_percent[1]} ({candidate_votes[1]})",
               f"{candidates[2]}: {candidate_vote_percent[2]} ({candidate_votes[2]})",
               "---------------------------- ",
               f"Winner: {winner}"]



for line in output_list:
    print(line)

               