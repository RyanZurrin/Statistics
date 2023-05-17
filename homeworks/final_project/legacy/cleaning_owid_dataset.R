str(owid)

# interested in the following columns from owid:
# diabetes_prevalence, cardiovasc_death_rate, total_deaths, total_cases, population_density, median_age
# make a dataframe containing all the values where none of the columns are null or NA, so if any of the columns are null or NA, remove the row
# Select columns
selected_cols <- owid[,c("iso_code", "continent", "location", "date", 'diabetes_prevalence', 'cardiovasc_death_rate', 'total_deaths', 'total_cases', 'population_density',"population", 'median_age')]

# Remove rows with missing values
cleaned_owid <- selected_cols[complete.cases(selected_cols),]

# Display the structure of the cleaned dataframe
str(cleaned_owid)

# Order the data by location and date in descending order
ordered_data <- cleaned_owid %>% arrange(location, desc(date))

# Keep only the latest row for each location
latest_data_owid <- ordered_data %>% group_by(location) %>% slice(1)

# Display the structure of the resulting dataframe
str(latest_data)

# save the latest_data_owid dataframe to a csv file
write.csv(latest_data_owid, file = "../datasets/latest_data_owid.csv")
