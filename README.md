# Election Analysis

## *Overview of Election Results*

### The purpose of this audit analysis was to count the number of votes per candidate, determining a winner by percentage of votes, and also totaling the votes per county to determine which had the largest voter turnout.


## *Election Audit Results*

![Election Analysis](analysis/election_analysis.txt)
* There were 369,711 votes cast in this congressional election.
* The precinct is comprised of three counties: 
    - Jefferson County, which had 38,855 votes (or 10.5%)
    - Arapahoe County, which had 24,801 votes (or 6.7%)
    - Denver County, which had the highest voter turnout with 369,711 (or 82.8%)

### Stock Performance
Stocks performed much better in 2017 than the following year. While FSLR would have been a great pick in 2017 with high trading volumes and significant return yields, it did not fare so well in 2018. ENPH performed consistently for both years, with an increased volume in 2018 over 2017, and returns upwards of 80% both years

### Results of Re-factoring 2017 Code
Refactored 2017
![image](https://user-images.githubusercontent.com/93684851/143087895-9aa261c8-f787-4a56-b604-6d70010c3f08.png)

![VBA_Challenge_2017](Resources/VBA_Challenge_2017.PNG)

![Green_Stocks_2017](Resources/Green_Stocks_2017.PNG)

### Results of Re-factoring 2018 Code
![VBA_Challenge_2018](Resources/VBA_Challenge_2018.PNG)

![Green Stocks_2018](Resources/Green_Stocks_2018.PNG)

## Summary

Refactoring code allows a developer to begin with an existing code and make modifications or edits to either clean it up or improve. You can condense or rearrange lines without changing the functionality of the code. One disadvantage is that if the code is large, you have to be careful that any changes made are consistent so that the code does not break.

This particular script was functional at the end of the module.  When I began refactoring the code, I started getting errors because of different lines I had changed. I had to track those changes and make adjustments in order to restore the code to working order. Creating an index of the tickers allowed the code to loop through once and gather the requested data from each element in the array, instead of looping through each named element to gather the information, one at a time for 12 rounds.  The resulting code was much faster!
