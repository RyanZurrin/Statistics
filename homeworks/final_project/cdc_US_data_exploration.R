# check working directory
getwd()
# set working directory
# setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')
setwd('D:/src/python/Statistics/homeworks/final_project')

# import the cdc_90519_DS1.csv file into a dataframe
cdc <- read.csv('datasets/cdc_90519_DS1.csv', header=TRUE)

# print the structure of the dataframe
str(cdc)

# print the summary of the dataframe
summary(cdc)

# make a dataframe of pre-existing conditions
preexisting_conditions <- cdc[,c(1, 2, 7, 11, 15, 19, 23, 27)]
colnames(preexisting_conditions) <- c("county", "state", "any_condition", "obesity", "heart_disease", "COPD", "diabetes", "CKD")
str(preexisting_conditions)
summary(preexisting_conditions)