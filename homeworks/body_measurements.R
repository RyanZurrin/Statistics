install.packages("tidyverse")
install.packages("readr")
install.packages("dplyr")
install.packages("ggplot2")

library(tidyverse)
library(readr)
library(dplyr)
library(ggplot2)

# look at the working directory
getwd()
# set the working directory
setwd('D:/src/PycharmProjects/Statistics/homeworks')

body <- read.csv("Body_Measurements _ original_CSV.csv", header=TRUE)
summary(body)

attach(body)
head(Waist)

hist(Waist)

# plot a relative frequency histogram of Waist
hist(Waist, freq=FALSE)

# get mean of Waist
mean(Waist)

# get sigma of Waist
sd(Waist)

# set sample mean and sigma to fit data to normal distribution
mu <- mean(Waist)
sigma <- sd(Waist)

# create a normal distribution with mean and sigma
x <- seq(min(Waist), max(Waist), length.out=100)
y <- dnorm(x, mean=mu, sd=sigma)

# plot normal distribution
plot(x, y, type="l", lwd=2, col="red")
# plot using curve on top of histogram
curve(dnorm(x, mean=mu, sd=sigma), from=min(Waist), to=max(Waist), add=TRUE, col="blue", lwd=2)



# find a normal distribution that fits the data using any of the data points
mu <- mean(Waist)
sigma <- sd(Waist)
xbar <- mean(Waist)
# gamma function has alpha and beta parameters let us define them using mean and sigma
s2.adj <- mean((Waist-xbar)^2)
alphahat <- xbar^2/s2.adj
print(alphahat)
betahat <- s2.adj/xbar
curve(dgamma(x, shape=alphahat, scale=betahat), from=min(Waist), to=max(Waist),
      add=TRUE, col="green", lwd=2)
## nonparametric method
lines(density(Waist), col="purple", lwd=2)

## plot waist vs hips
plot(Waist, Hips, xlab="Waist", ylab="Hips", main="Waist vs Hips")
## corelation between waist and hips
cor(Waist, Hips)

cormat <- cor(body)


view(cormat)

# plot the histogram of Waist to Hip ratio
hist(Waist/Hips)

detach(body)