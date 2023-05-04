# check working directory
getwd()
# set working directory
setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')

# import the cdc_90519_DS1.csv file into a dataframe
cdc <- read.csv('cdc_90519_DS1.csv', header=TRUE)
# load the WHO-COVID-19-global-data.csv file
who <- read.csv('WHO-COVID-19-global-data.csv', header=TRUE)
# load the WHO-COVID-19-global-table-data.csv file
who_table <- read.csv('WHO-COVID-19-global-table-data.csv', header=TRUE)
# load the owid-covid-data.csv file
owid <- read.csv('owid-covid-data.csv', header=TRUE)
# load the vaccination-data.csv file
vaccination <- read.csv('vaccination-data.csv', header=TRUE)

# print the structure of the dataframe
str(cdc)

# print the summary of the dataframe
summary(cdc)

# print the first 10 rows of the dataframe
head(cdc, 10)





# print the structure of the dataframe
str(who_table)

# print the structure of the dataframe
str(who)



# print the structure of the dataframe
str(owid)



# print the structure of the dataframe
str(vaccination)

# print total_deaths of owid
owid$total_deaths

# graph the correlation between pre-existing conditions and total_deaths
plot(owid$total_deaths, owid$cardiovasc_death_rate,
     main="Correlation between cardiovacular and total_deaths",
     xlab="total_deaths",
     ylab="cardiovasc_death_rate", pch=19
)

str(owid)


# graph the correlation between pre-existing conditions and total_deaths
plot(owid$total_deaths, owid$diabetes_prevalence,
     main="Correlation between pre-existing conditions and total_deaths",
     xlab="total_deaths",
     ylab="diabetes_prevalence", pch=19
)

# look at the owid dataframe
head(owid)

# Filter out missing or infinite values from both variables
cdc_filtered <- cdc[!is.na(cdc$TOTAL_DEATHS) & !is.infinite(cdc$TOTAL_DEATHS) &
                    !is.na(cdc$CARDIOVASCULAR) & !is.infinite(cdc$CARDIOVASCULAR),]

# Print the filtered data frame
print(cdc_filtered)
str(cdc)
# Set the x-axis limits to include all of the data
xlim <- range(cdc_filtered$TOTAL_DEATHS)

# Plot the filtered data with custom x-axis limits
plot(cdc_filtered$TOTAL_DEATHS, cdc_filtered$CARDIOVASCULAR,
     main="Correlation between pre-existing conditions and total_deaths",
     xlab="total_deaths",
     ylab="cardiovasc_death_rate", pch=19,
     xlim=xlim
)



