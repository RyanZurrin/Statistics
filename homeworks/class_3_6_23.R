data(iris)
?iris

str(iris)
# view the sepal.length vs petal.length using ggplot
library(ggplot2)
ggplot(iris, aes(x=Sepal.Length, y=Petal.Length)) + geom_point()
# add color to the plot
ggplot(iris, aes(x=Sepal.Length, y=Petal.Length, color=Species)) + geom_point()

# print histogram of sepal.length
hist(iris$Sepal.Length)
# print histogram of petal.length
hist(iris$Petal.Length)

# import the processed.clevleast dataset
getwd()
setwd('D:/src/PycharmProjects/Statistics/homeworks')
# read the processed.cleveland.data file
cleveland <- read.csv('processed.cleveland.data', header=FALSE)
str(cleveland)
hist(cleveland$V1)
summary(cleveland$V2)
table(cleveland$V2)
hist(cleveland$V14)
n <- length(cleveland$V14)
barplot(table(cleveland$V14)/n)

wine <- read.csv('wine.data', sep=',', header=FALSE)
str(wine)
 	# 1) Alcohol
 	# 2) Malic acid
 	# 3) Ash
	# 4) Alcalinity of ash
 	# 5) Magnesium
	# 6) Total phenols
 	# 7) Flavanoids
 	# 8) Nonflavanoid phenols
 	# 9) Proanthocyanins
	# 10)Color intensity
 	# 11)Hue
 	# 12)OD280/OD315 of diluted wines

# add the column names to the wine dataset
colnames(wine) <- c('Class', 'Alcohol', 'Malic.acid', 'Ash', 'Alcalinity.of.ash', 'Magnesium', 'Total.phenols', 'Flavanoids', 'Nonflavanoid.phenols', 'Proanthocyanins', 'Color.intensity', 'Hue', 'OD280.OD315.of.diluted.wines', 'Proline')
str(wine)

# use ggplot to print a 4d plot of Alcohol vs Color.intensity vs flavanoids vs Class
library(ggplot2)
ggplot(wine, aes(x=Alcohol, y=Color.intensity, z=Flavanoids, color=Class)) + geom_point()
library(plotly)
ggplotly(ggplot(wine, aes(x=Alcohol, y=Color.intensity, z=Flavanoids, color=Class)) + geom_point())
ggplot(wine, aes(x=Alcohol, y=Color.intensity, color=Class)) + geom_point()

# use plotly to print a 4d plot of Alcohol vs Color.intensity vs flavanoids vs Class
library(plotly)
ggplotly(ggplot(wine, aes(x=Alcohol, y=Color.intensity, z=Flavanoids, color=Class)) + geom_point())

qnorm(0.975)
