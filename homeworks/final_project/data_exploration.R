# check working directory
getwd()
# set working directory
setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')

# import the cdc_90519_DS1.csv file into a dataframe
cdc <- read.csv('cdc_90519_DS1.csv', header=TRUE)

# print the structure of the dataframe
str(cdc)

# print the summary of the dataframe
summary(cdc)

# print the first 10 rows of the dataframe
head(cdc, 10)

# load the WHO-COVID-19-global-data.csv file
who <- read.csv('WHO-COVID-19-global-data.csv', header=TRUE)

# load the WHO-COVID-19-global-table-data.csv file
who_table <- read.csv('WHO-COVID-19-global-table-data.csv', header=TRUE)

# print the structure of the dataframe
str(who_table)

# print the structure of the dataframe
str(who)

# load the owid-covid-data.csv file
owid <- read.csv('owid-covid-data.csv', header=TRUE)

# print the structure of the dataframe
str(owid)

# load the vaccination-data.csv file
vaccination <- read.csv('vaccination-data.csv', header=TRUE)

# print the structure of the dataframe
str(vaccination)

# print total_deaths of owid
owid$total_deaths