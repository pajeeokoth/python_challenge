import pandas as pd

# File to Load
poll_path = "Resources/election_data.csv"

# Read the modified Comic Books csv and store into Pandas DataFrame
poll_df = pd.read_csv(poll_path)

# total votes cast
votes = poll_df.shape[0]

#List of Candidates who got votes
candidate_name = poll_df['Candidate'].unique()

#votes garnered
votes_received = poll_df.groupby(['Candidate'])['Ballot ID'].count()

#percent votes garnered
percent_votes = round(votes_received/len(poll_df)*100, 2)


#election winner
winner = percent_votes.max()

#results tally
print(f' Election Results \n -------------------- \n Total Votes: {votes} \n -------------------- \n{percent_votes} ({votes_received})  \n  -------------------- \n Winner: {candidate_name[1]} \n ------------------------')

#print results to txt file
with open('poll.txt', 'a') as f:
    print(f' Election Results \n -------------------- \n Total Votes: {votes} \n -------------------- \n {percent_votes} ({votes_received})  \n  -------------------- \n Winner: {candidate_name[1]} \n ------------------------')
