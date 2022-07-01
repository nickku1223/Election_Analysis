# Election_Analysis

## Overview of election audit:
To analysis the election audit with Python based on the data provided (election_result.csv). 

## Election-audit results
- How many votes were cast in this congressional election?

    The total votes casted were : 369,711

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

    **Jefferson** has **38,855** votes which is **10.5%** of the total votes.
    
    **Denver** has **306,055** votes which is **82.8%** of the total votes.
    
    **Aparahoe** has **24,801** votes which is **6.7%** of the total votes.


- Which county had the largest number of votes?

    **Denver** has the largest number of votes.
    
    
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    **Charles Casper Stockham** received **85,213** votes (23% of the total votes).
    
    **Diana DeGette** received **272,892** votes (73.8% of the total votes).
    
    **Raymond Anthony Doane** received **11,606** votes (3.1% of the total votes).

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    **Diana DeGette** was the winner of this election!
    The candidate received 272,892 votes out of total 369,711 of votes, which is 82.8% of the total votes.


## Electio-audit summary
    
The script used in this analysis will be good for running other election as well. If the source data is the same format (.csv files) and has three columns for the data (Ballot ID, County, Candidate), we could edit the path of the file, as well as the output analysis text file. 

> file_to_load = os.path.join("Resources", "election_results.csv")

This line of code will direct the path to the data source file, we can save the file in the "Resources" folder and replace the "election_results.csv" to the name of the data source file in order for this script to run.

> file_to_save = os.path.join("analysis", "election_analysis.txt")

This line of code will save the output of the analysis for the election, we can replace the "election_analysis.txt" with desired file name for the new analysis.
