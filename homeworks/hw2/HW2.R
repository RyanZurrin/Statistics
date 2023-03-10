## Import the COVID dat
getwd()
setwd("D:/src/python/Statistics/homeworks/hw2")
covid <- read.table("world-covid-2023-02-03.txt", sep = "\t", comment.char = "", header = TRUE,
					na.strings = c("N/A ", ""))

str(covid)

head(covid)
tail(covid)

covid$Country <- trimws(covid$Country)

covid <- covid[,-1]
str(covid)
dim(covid)
head(covid)
tail(covid)

summary(covid)
typeof(covid)
# make a df of the covid data
covid_df = read.csv('world-covid-2023-02-03.txt', sep = '\t')
# use ggplot to visualize the data
?ggplot

cPlot = ggplot(data=covid)
# add aesthetics and geom
cPlot = cPlot + aes(x=Total.Deaths, y=Active.Cases)
cPlot = cPlot + geom_point()
cPlot
# how many rows does the data have?
nrow(covid)
# how many columns does the data have?
ncol(covid)
# how mnay dimensions does the data have?
dim(covid)
# using the function plot, create a scatter plot of the population size
# versus the total number of cases. After viewing the two variables on a linear
# scale, plot them again on a logarithmic scale using the agrument log = "xy"
# comment on the relationship between the two variables

plot(covid$Population, covid$Total.Cases)
plot(covid$Population, covid$Total.Cases, log = "xy")

# there is a clear relationship between the two variables. As the population size
# increases, the total number of cases increases. The relationship is linear.

# get the linear regression model for the two variables
lm(covid$Total.Cases ~ covid$Population)
# get the linear regression model for the two variables on a log scale
fit <- lm(log(covid$Total.Cases) ~ log(covid$Population))
# get the linear equation for the two variables
summary(fit)
y = '1.52669 + 0.71460x + 1.881'
# create a histogram of the number of tests per million people. Comment on its
# shape. Then plot the histogram of the logarithm in base 10 of the same variable.
# How do the two histograms compare?
hist(covid$Tests.1M.pop)
hist(log10(covid$Tests.1M.pop))
# these two histograms are very different looking. The first histogram is skewed
# to the right big time while the second histogram is more normal looking but just
# a little skewed to the left.

# which country  has the highest ratio of active cases over popultation size?
# HINT: divide the first corresponding column by the second and use which.max
# to find the index of the maximum value
str(covid)
covid$Active.Cases
covid$Population
covid$Active.Cases/covid$Population
which.max(covid$Active.Cases/covid$Population)
var = covid[which.max(covid$Active.Cases/covid$Population),]
ggplot(data=covid) + aes(x=Active.Cases, y=Population) + geom_point()
filter = covid$Active.Cases/covid$Population
filter
# add color to the plot and size based on the number of tests per million people
gp = ggplot(data=covid) + aes(x=Active.Cases, y=Population, color=Country, size=filter) + geom_point()
# add log scale to the x and y axis
gp = gp + scale_x_log10() + scale_y_log10()
gp

