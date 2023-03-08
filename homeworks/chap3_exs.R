
#################################################
## Exercises 3.52, 3.58, 3.115, and 3.117 
## of the textbook on the binomial distribution 
## and the hypergeometric distribution
#################################################




#######
# 3.52 
#######

# Fixed number (20) of Bernoulli trials (taster/not taster), 
# all independent and with same success rate (p=0.7)
# Count # successes (=#tasters) in sample --> binomial r.v.

n <- 20 # sample size
p <- .7 # proportion of "tasters"

## Part a: P(Y >= 17)
pbinom(16,n,p,lower.tail=FALSE) 

## Part b: P(Y < 15)
pbinom(14,n,p) 



#######
# 3.58
#######
 
# n = 20 fish (fixed sample size), 
# Bernoulli trials (success: survival, failure: death)
# Independent trials (survival of one fish does not affect others)
# Same probability of survival (p = 100% - 20% = 80%)
# Of interest: Y = # surviving fish 
# --> Binomial distribution with parameters n = 20 and p = 0.8
 
n <- 20
p <- 0.8

## Part a: probability that exactly 14 survive
y <- 14
choose(n,y) * p^y * (1-p)^(n-y) # by hand
dbinom(y,n,p) # using built-in functions

## Part b: probability that at least 10 survive
sum(dbinom(10:20,n,p)) # a bit clunky, but it works
1 - pbinom(9,n,p) # P(Y >= 10) = 1 - P(Y <= 9)
pbinom(9,n,p,lower.tail=FALSE) # P(Y >= 10) = P(Y > 9)

# All three methods are valid 

## Part c: probability that at most 16 survive
pbinom(16,n,p)

## Part d: mean and variance of the number that survive
(mu <- n*p)
(sigma2 <- n*p*(1-p))

# The parentheses are used to print the result at the same time 
# as this result is assigned. Compare with 
mu <- n*p



########
# 3.115 
########

# N=6 transistors, r=2 defectives, n=3 sampled
# Y = # defectives
# 1) Finite population, 2) binary characteristic (defective/not defective),
# 3) sampling w/o replacement, 4) count # successes (here, # defectives).
# --> Y has a hypergeometric distribution


y <- 0:2 # possible values of Y 
# Note: although 3 transistors are sampled, only 2 are defective in the radio,
# which is why the value Y=3 is not possible. 
r <- 2 # number of defectives 
n <- 3 # sample size
N <- 6 # population size

## Calculate probability distribution by hand
p <- choose(r,y) * choose(N-r,n-y) / choose(6,3)

## Using built-in functions
p2 <- dhyper(y,r,N-r,n)

## Make sure the two calculations yield the same result
identical(p,p2) # test for strict equality
all.equal(p,p2) # allow numerical equality within machine error tolerance
 
## Plot 
# With function 'barplot'
barplot(p, names.arg=y, space=0, col="lightblue", 
	xlab="y", ylab="p(y)", main="Probability histogram")

# With function 'rect'
ybreaks <- seq(from=-0.5, to=2.5, by=1)
# Set up new empty plot
plot(0, 0, xlim=range(ybreaks), ylim=c(0,max(p)), 
	type="n", xaxt="n", yaxt="n", xlab="y", ylab="p(y)")
# Add rectangles
rect(xleft=ybreaks[1:3], ybottom=rep(0,3), 
	xright=ybreaks[2:4], ytop=p, col=3)
# Add axis ticks and title
axis(1, at=y)
axis(2, at=seq(0,0.6,by=0.2)) 
title("Probability histogram")




########
# 3.117 
########

## 1) Random sample from finite population, 2) fixed sample size, 
## 3) sampling w/o replacement, 4) count "successes" in sample 
## --> hypergeometric distribution

m <- 18 # successes (properly drilled gearboxes)
n <- 2  # failures
k <- 5  # sample size


## Probability that all 5 sampled gearboxes are properly drilled
dhyper(5,m,n,k)

## Direct calculation (event-composition method)
# First sampled drill is working, 2nd is, ... , and 5th is
# p = (18/20) * (17/19) * (16/18) * (15/17) * (14/16)
prod((18:14)/(20:16))

# And, as a fraction: 
library(MASS)
fractions(prod((18:14)/(20:16))) 






