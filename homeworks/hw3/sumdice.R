#########
# Part 1
#########


# Simulate the following experiment: roll two balanced dice 
# and record the sum of the two dice. Repeat the simulation
# many times to find the approximate probability that the sum 
# of the two dice is 7


## Method 1
nsim <- 1e4
nsuccess <- 0
for (i in 1:nsim) {
	dice <- sample(1:6, 2, replace = TRUE)
	sumdice <- sum(dice)
	if (sumdice == 7) { 
		nsuccess <- nsuccess + 1 
	}
}
propsuccess <- nsuccess / nsim


## Method 2 (much faster)
nsim <- 1e4
dice <- matrix(sample(1:6, 2 * nsim, replace = TRUE), nsim, 2)
sumdice <- rowSums(dice)
propsuccess <- mean(sumdice == 7)


# Note: you can calculate the execution time of each method by 
# enclosing the lines of each method in system.time({   })
# For example, 
# system.time({ 
#	print("Hello World")
#	Sys.sleep(1) 
# }) 


#########
# Part 2
#########


## In the same random experiment, calculate the probability 
## of the sum being k for k = 2, 3, ..., 12

die1 <- 1:6
die2 <- 1:6
noutcomes <- length(die1) * length(die2) # 36
sumdice <- outer(die1, die2, "+")
prob <- matrix(nrow = 11, ncol = 2)
prob[,1] <- 2:12
for (k in 2:12) {
	prob[k-1,2] <- sum(sumdice == k) / noutcomes
}
# Faster than the for loop: 
# prob[,2] <- table(sumdice) / noutcomes

# Recall: all 36 outcomes, that is, all combinations (i,j) of die result
# for i = 1,..., 6 and j = 1, ..., 6, are equally likely 
# Therefore the probability of an event is simply the number of 
# outcomes that realize this event divided by the total number of possible outcomes

## View the probability table
colnames(prob) <- c("k", "probk")
prob

## Check that the sum of probabilities equals 1
sum(prob[,2])



#########
# Part 3
#########

## Compare the theoretical probabilities of the possible values 
## of the sum (of th two dice) to simulation results

dice <- matrix(sample(1:6, 2 * nsim, replace = TRUE), nsim, 2)
sumdice <- rowSums(dice)
## Make sure that all values 1,...,12 have been attained at least once
set.equal(sumdice, 2:12) 
prob <- cbind(prob, table(sumdice) / nsim)
colnames(prob) <- c("k", "theory", "simul")
round(prob,3)


