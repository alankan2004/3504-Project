# Spreadsheet Data (CSE 3504 Project)
A Python Script that takes data (26 survey questions from 1400 users) out of spreadsheet and calculate probabilities and statistics to plot graphs using Python Libaries, then make comparision and analysis on the result.


#### Note:
This is an old Python Project I did in my CSE 3504 Probabilistic Performance Analysis of Computer Systems class in Spring 2018.

### Note: Documentation and clean up are still not done yet.

The project was split into two parts.

Part 1 is calcuating probability, mean, variance and entropy of each users answers to the 26 survey questions, and lastly calculating the Hellinger distance between each possible pair of questions.

Part 2 is plotting the distributions for male and female respondents in bar graphs and find the similar distribution questions, showing the list of 26 Hellinger distances of each question, lastly performing the Hypothesis Testing.


## Prerequisites

### Python

For Mac OS X Users: https://www.python.org/downloads/mac-osx/

For Windows Users: https://www.python.org/downloads/windows/

### Libaries

Go to your Terminal or CommandPrompt

```
pip install pandas
```

If the above command doesn't work and asks for authorization, then use...

```
sudo pip install pandas
```
#### And we repeat this step for the other libaries.

### The excel-sheet I used for the data
mini-project1-data.xlsx



## What I used and learned
* Extracting data from spreadsheet using Python.
* Python Libaries: Pandas, NumPy, matplotlib, math, statistics.


