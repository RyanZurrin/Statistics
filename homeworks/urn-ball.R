
## Problem: n urns labeled 1,...,n. 
## Urn k contains k white balls and (n-k) red balls (k=1,...,n).
## Select one urn at random and draw 2 balls from that urn w/o replacement.


#####################################
# FUNCTIONS TO CALCULATE THEORETICAL 
# PROBABILITIES AND EXPECTED VALUES
#####################################


# Function that returns probability distribution and expected value of 
# the number Y of red balls 
probs <- function(n)
{
	y <- 0:2 # number of red balls
	py <- c((n-2)/(3*n), (n+4)/(3*n), (n-2)/(3*n)) # associated probabilities
	EY <- sum(py * y) # expected value
	list(y=y, p=py, E=EY)
}


## Simulate the random experiment many times 
## and return the value of Y for each simulation

# Version 1: simple code with a 'for' loop
simulate1 <- function(n, N = 1e5)
{
	## Create numeric vector that will contain simulated values of Y 
	y <- numeric(N) # could also be y <- integer(N)
	
	## Simulation loop
	for (i in 1:N)
	{
		## Select urn 
		k <- sample(n, 1)
		
		## Draw 2 balls from urn w/o replacement
		balls <- sample(x = rep(c("red","white"),c(n-k,k)), size = 2)
		
		## Count red balls
		y[i] <- sum(balls == "red")
	}
		
	return(y)
}

# Version 2: vectorize operations more 
simulate2 <- function(n, N = 1e5)
{
	## Select urn for each simulation
	urn <- sample(n, N, replace = TRUE)
	
	## Select 2 balls for each simulation
	# Without loss of generality assume that in urn k, the "first k" balls are white
	balls <- replicate(N, sample(n, 2, replace = FALSE)) 
	
	## Count number of red balls for each simulation
	y <- (balls[1,] > urn) + (balls[2,] > urn)  	
	return(y)
}


# Version 3: fully vectorized code
simulate3 <- function(n, N = 1e5)
{
	## Select urn for each simulation
	urn <- sample(n, N, replace = TRUE)
		
	## Directly simulate number of red balls from the hypergeometric distribution
	y <- rhyper(N, n-urn, urn, 2)
	
	return(y)
}


##########################################################################################################


#######
# TEST 
#######

n <- 100
vals <- probs(n)
barplot(vals$p, names.arg = vals$y, space = 0, col = 3:5, 
	xlab = "Value", ylab = "Probability")
title("Probability histogram of number of red balls")
cat("Theoretical quantities for n =",n,"\nValues:",vals$y,"\nProbabilities:",vals$p, 
	"\nExpected value:",vals$E)

# What seems to be the value of E(Y) for all n? 



## Simulations
system.time(y <- simulate1(n)) # 1.859s
system.time(y <- simulate2(n)) # 0.830s
system.time(y <- simulate3(n)) # 0.015s 

## Relative frequency table
N <- length(y)
print(table(y)/N)

## Compare to theoretical values
tab <- matrix(,2,3)
tab[1,] <- table(y)/N
tab[2,] <- vals$p
colnames(tab) <- vals$y
rownames(tab) <- c("observed","theory")
print(tab, digits = 3)

# Same for expected value
ybar <- mean(y)
cat("Mean value of Y\nObserved:", ybar,"\nExpected:",vals$E)








