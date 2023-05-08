# load the google dataset located at "https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv\" into a dataframe

aggregated_data <- read.csv('https://storage.googleapis.com/covid19-open-data/v3/latest/aggregated.csv', header=TRUE)

health_data <- read.csv('https://storage.googleapis.com/covid19-open-data/v3/latest/epidemiology.csv', header=TRUE)

# save the aggregated_data dataframe to a csv file
write.csv(aggregated_data, file = "../datasets/aggregated_data.csv")

# save the health_data dataframe to a csv file
write.csv(health_data, file = "../datasets/health_data.csv")
