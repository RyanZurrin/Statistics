# set working directory
# setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')
setwd('D:/src/python/Statistics/homeworks/final_project')
getwd()

# import the covid.csv file into a dataframe
cleaned_preexisting <- read.csv('datasets/kaggle_preexisting.csv', header=TRUE)

kaggle_preexisting <- read.csv('datasets/covid.csv', header=TRUE)

