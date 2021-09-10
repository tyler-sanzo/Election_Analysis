# Colorado Congressional Election Audit

## Project Overview

Tom, a Colorado Board of Elections employee, has provided us with tabulated data of a Colorado precinct's congressional election. Tom is tasked with auditing this election and has asked for help on generating the results of the election. Using the power of python scripting, we are able to generate a vote count report that can be used in the future for more efficient election auditing.

## Results

Below are the results of this election which can also be found in the analysis folder. [Analysis](https://github.com/tyler-sanzo/Election_Analysis/blob/main/analysis/election_analysis.txt)

* Total Votes: 369,711

* County Votes
   * Jefferson: 10.5% (38,855)
   * Denver: 82.8% (306,055)
   * Arapahoe: 6.7% (24,801)
</ul>

* Denver County had the largest voter outcome

* Candidate votes
   * Charles Casper Stockham: 23.0% (85,213)
   * Diana DeGette: 73.8% (272,892)
   * Raymon Anthony Doane: 3.1% (11,606)
</ul>

* Diana DeGette won this election with 272,892 votes, or 73.8% of the popular vote.

## Election Audit Summary

This script can be used for any general popular election so long as we have this same tabular data provided since it's essentially a simple loop that records data into local arrays. One addition that could be made to accommodate for something such as a primary election would be modifying the script to handle a political party column. This would be useful in order to separate each candidate by their party and conclude who won the popular vote within each candidates respective party. Below is a sample of code that could be used to handle classifying candidates by their parties.

Using a similar structure of looping through the rows and appending candidate options to a list, we can create a dictionary to store key-value pairs of candidates and their party.

First we initialize the empty dictionary outside of our loop next to the candidate and county arrays/dictionaries

    party_affiliations = {}

For this example lets assume the array storing the party is column 4 (index 3). Inside of the block written to loop through the csv file we can add to the second level block like this:

    for row in reader:

        candidate_name = row[2]

        candidate_party = row[3]

        if candidate_party not in party_affiliations:

            party_affiliations[candidate_party]=[candidate_name]

        else:
            party_affiliations[candidate_party].append(candidate_name)


This block of code will loop create dictionary items consisting of the party as a key and a list of candidates running in that party such that:

    party_affiliations = {party1 : [candidate1, candidate2, ...], party2 : [candidate1, candidate2, ...], ... }

From here we can create another script to display the results for each party using the party assorted lists stored in the dictionary.









