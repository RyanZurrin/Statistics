# set working directory
# setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')
setwd('D:/src/python/Statistics/homeworks/final_project')
getwd()

# import the cdc_90519_DS1.csv file into a dataframe
cdc <- read.csv('datasets/cdc_90519_DS1.csv', header=TRUE)

# import the Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv
cdc_conditions <- read.csv('datasets/Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv', header=TRUE)

# load the owid-covid-data.csv file
latest_owid <- read.csv('datasets/latest_data_owid.csv', header=TRUE)

# import the covid.csv file into a dataframe
kaggle_preexisting <- read.csv('datasets/covid.csv', header=TRUE)

# load the aggregated_data.csv file
google_aggregated <- read.csv('datasets/aggregated_data.csv', header=TRUE)

# load the health_data.csv file
google_health_ <- read.csv('datasets/health_data.csv', header=TRUE)


