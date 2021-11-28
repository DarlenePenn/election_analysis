# Election Analysis

## *Project Overview*

### A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## *Challenge Overview*
The Board of Elections employee has asked for some additional information regarding the election audit.
1. Get a list of counties that voted in the election.
2. Calculate the total number of votes for each county.
3. Calculate the percentage of votes cast in each county.
4. Determine which county had the largets voter turnout.

## *Resources*
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.62.3

## *Election Audit Results*
[Election Analysis](analysis/election_analysis.txt)

* There were 369,711 votes cast in this congressional election.
* The precinct is comprised of three counties: 
    - Jefferson County, which had 38,855 votes (or 10.5%)
    - Arapahoe County, which had 24,801 votes (or 6.7%)
    - Denver County, which had the highest voter turnout with 369,711 votes(or 82.8%)
* The election was between 3 candidates:
    - Charles Casper Stockham, who received 23.0 % of the votes, 85,213 total
    - Diana DeGette, who received 73.8% of the votes, 272,892 total
    - Raymon Anthony Doane, who received 3.1% of the the votes, 11,606 total
* The winner of the election was Diana DeGette with 272,892 votes, which was 73.8% of the total votes cast.

## *Election Audit Summary*
This script was successful at extracting the above data from the congressional election results.  It could be modified to assist with auditing any election.  Because many elections use multiple ballot types to capture votes, this script could be changed to calculate the total amount of votes for each method, and which ballot type was used the most.  For example, you could check between mail-in ballots vs electronic ballots by changing the script to search for and calculate each voting method, instead of (or in addition to) the county of the voter, totaling the percentage of each ballot type. The script could also be used in local elections with more candidates, like a school board election. The dictionary of candidate names would be longer, but the output would be the same for that relative campaign.
