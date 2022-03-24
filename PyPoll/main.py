import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)

    # initialize empty list to hold every candidate name in the csv 
    # loop throw csv rows and store candidate names
    candidates_long = []
    for row in csvreader:
        candidates_long.append(row[2])

    # count the number of elements in cadidates_long
    # (analagous to number of votes cast)
    vote_count = len(candidates_long)

    # initialize empty list to retain each candidate's name once
    # use list comprehension to append unique candidate names to candidates_short
    candidates_short = []
    [candidates_short.append(cand) for cand in candidates_long if cand not in candidates_short]

    # initialize empty lists to store vote counts/percentages for each candidate
    cand_count = []
    cand_count_percent = []
    for cand in candidates_short:
        count = candidates_long.count(cand)
        cand_count.append(count)
        percent_count = candidates_long.count(cand)/vote_count
        cand_count_percent.append("{0:.3%}".format(percent_count))


# determine the greatest number of votes and the winning candidate
winner_votes = max(cand_count)
winner = candidates_short[cand_count.index(winner_votes)]

# initialize empty list to contain the different lines of output
output_list = []
output_list.append("Election Results ")
output_list.append("---------------------------- ")
output_list.append(f"Total Votes: {vote_count} ")

# loop through all the candidates and print their results
for x in range(len(candidates_short)):
    output_list.append(f"{candidates_short[x]}: {cand_count_percent[x]} ({cand_count[x]})")

output_list.append("---------------------------- ")
output_list.append(f"Winner: {winner} ")

# print output to terminal
for line in output_list:
    print(line)

# export results into a .txt file
output_path = os.path.join('Analysis','pypoll-results.txt')

with open(output_path, 'w') as txtout:
    txtout.write('\n'.join(output_list))

               