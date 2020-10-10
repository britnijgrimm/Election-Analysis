# Election Analysis Audit 

## Overview
The scope of this analysis is to assist the Colorado Board of Elections in automating the election audit process. The board receives tabulated election results which have been collected and counted via mail-in voting ballots, punch cards, and direct recording electronic machines.

For one US Congressional precinct, we have analyzed and summarized the voting results to audit the total number of votes cast and the total number of votes for each candidate. Using these totals, our script will calculate the percentage of votes cast for each candidate and identify the winner of the election based on popular vote.

Finally, the script will generate a text file, summarizing the vote count to declare the election results.

## Resources
-	Data Source: election_results.csv
-	Software: Python 3.7.6, Visual Studio Code 1.49.2

## Election Audit Results
This audit of this election demonstrations that:
- The candidates were:
	- Diana DeGette
  - Raymon Anthony Doane
  - Charles Casper Stockham

- 369,711 total votes were cast in this congressional election.
  -Diana DeGette received 272,892 votes, or 73.8% of the total votes.
  -Charles Casper Stockham received 85,213 votes, or 23.0% of the total votes.
  -Raymon Anthony Doane received 11,606 votes, or 3.1% of the total votes.

- In Denver county:
  - 306,055 votes were cast, comprising 82.8% of the total votes.
- In Jefferson county:
  - 38,855 votes were cast, comprising 10.5% of the total votes.
- In Arapahoe county: 
  - 24,801 votes were cast, comprising 6.7% of the total votes.

- Denver had the highest voter turnout in the district.

### Which candidate won the election?
Diana DeGette won this election with 73.8% of the vote, or a total of 272,892 votes!

## Election Audit Summary
This script can be used to audit any election in a fashion similar to that used in this congressional election. Assuming the data provided in the election results CSV was not manipulated previously and/or future data would be presented in the same format, the script can be applied without any modifications. However, sometimes our data reporting changes, or we need to apply our analysis at a higher or lower level. The code itself could be modified as needed to specifically audit data at the state, postal code, or congressional district level. We could take it a step further and allow the user to input the type of location data to be audited. The script would accept this input and utilize it to label the audit output. This script can also be modified to accept user input to define the file path and file name, allowing for the Commission to easily audit other results without renaming or copying files.
