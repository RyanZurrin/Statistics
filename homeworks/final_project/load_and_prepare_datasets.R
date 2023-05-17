# set working directory
setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')
# setwd('D:/src/python/Statistics/homeworks/final_project')
getwd()

# import the covid.csv file into a dataframe
cleaned_preexisting <- read.csv('datasets/kaggle_preexisting.csv', header=TRUE)

kaggle_preexisting <- read.csv('datasets/covid.csv', header=TRUE)

# adding gender column
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))


# Creating a new binary variable 'died'. If 'date_died' is '9999-99-99' (representing not dead),
# 'died' is set to 0. Otherwise, 'died' is set to 1 (indicating the patient died).
kaggle_preexisting$died <- ifelse(kaggle_preexisting$date_died == '9999-99-99', 0, 1)

# Creating a new data frame 'kaggle_numeric' that only contains numeric columns from the
# 'kaggle_preexisting' data frame. This can be useful for analysis involving only numeric data.
kaggle_numeric <- kaggle_preexisting %>%
  select_if(is.numeric)


# Using sapply to apply the 'is.numeric' function to each column in 'kaggle_preexisting',
# creating a new data frame 'numeric_data' that only includes columns where the function returns TRUE
# (i.e., columns that contain numeric data).
numeric_data <- kaggle_preexisting[sapply(kaggle_preexisting, is.numeric)]

# Repeating the above process with the 'cleaned_preexisting' data frame to create
# a new data frame 'numeric_cleaned' that only includes columns with numeric data.
numeric_cleaned <- cleaned_preexisting[sapply(cleaned_preexisting, is.numeric)]
