###########################
# SIMULATION OF COIN TOSS #
###########################



## Number of simulations
N = 1e4

## Simulate N tosses of a fair coin
toss = sample(x=c("H","T"),size=N,replace=TRUE)
# Note: it's not necessary to indicate argument names 
# if they are provided in the right order 
# sim = sample(c("H","T"),N,TRUE) # works too 

## Count the proportion of Heads (H) as a function of the number 
## of tosses (n=1,...,N)
propH = numeric(N)
for (n in 1:N)
	{ propH[n] = mean(toss[1:n] == "H") }
	
# Loops can be slow in R. A faster way to calculate the proportion 
# of heads is as follows: 
propH = cumsum(toss == "H")/(1:N)


###### 

## Compare computation times
system.time({
	for (n in 1:N)
	{ propH[n] = mean(toss[1:n] == "H") }
})
system.time(cumsum(toss == "H")/(1:N))

## For precise time benchmarks
install.packages("microbenchmark")
library(microbenchmark)
microbenchmark(cumsum(toss == "H")/(1:N))


###### 


## Plot the simulated proportions
plot(1:N, propH, xlab="Number of Trials", ylab="Proportion of Heads", type="l")

## Add theoretical probability of heads for one toss (0.5)
abline(h = 0.5, lty = 2)


