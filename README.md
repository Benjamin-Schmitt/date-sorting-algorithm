# date sorting algorithm
This script checks your .pdf or .txt or .docx file for dates and creates an orderly sheet with all dates. It is aimed at lawyers who oftentimes have to deal with huge amount of dates in order to keep track of deadlines with high risk of liability. Structuring all dates from a file can be time consuming labor.

# Important
This was one of my first scripts ever. Check for variable names and conventions at your own peril.

# Why is there no actualy legal file included?
Data Protections laws prevent me to add an actual file to the repository.

# How do I get an actual file to test this?
Search google for "Urteil Amtsgericht Berlin", then copy paste it into a txt file and give it a go.

# imports
- regex module

# Problem Solving Process
TASK: order the dates
- what does ordering mean.
- ordering means to find the number, which is smallest
- finding the number which is smallest means to comparing two numbers
- comparing means taking one number and see if it is bigger than another
- taking a number means to take one match in the iteration
- taking a match means saving the current iteration in a variable
- saving the current match in a variable means getting the number of matches first
- getting the number of matches means creating a variable for each match
- then you can save the match in the variable
- seeing which number is smallest means to check if it is bigger than another.
- if it is smaller, compare IT to the next numbers
- repeat process
