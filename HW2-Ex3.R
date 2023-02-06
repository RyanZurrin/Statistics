
## Set the working directory to the folder that contains the data
setwd("~/Library/Mobile Documents/com~apple~CloudDocs/UMB/2022-23/Teaching/345/Week 2/HW2/")

# Note: this is not really needed. It's just so that in the next command read.table, 
# you can specify the file to be read just by its name (and not provide the entire file path).
# By default, R looks for files to import or execute in the working directory

## Import the COVID data
covid <- read.table("world-covid-2023-02-03.txt", sep = "\t", comment.char = "", header = TRUE, 
	na.strings = c("N/A ", ""))

# sep = "\t" specifies that the fields in the file are separated by tabulations
# comment.char = "" tells R there's no character to indicate that a comment will follow
# (The default is comment.char = "#" but here we turn this off)
# header = TRUE specifies that the first line of the file contains the variables' names, not data values
# na.strings = c("N/A ", "") identifies missing values as "N/A " or just empty fields

## Examine the structure of the new data frame
str(covid)

## View the first few (6) lines of the data frame
head(covid)

## Data cleanup: remove the trailing whitespaces in country names
covid$Country <- trimws(covid$Country)

## Data cleanup: get rid of the first column of indices (not needed)
covid <- covid[,-1]

## Check the clean data frame
str(covid)
head(covid)
tail(covid) # last few lines



