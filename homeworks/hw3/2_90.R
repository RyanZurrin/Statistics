###################
# Exercise 2.90
# Parachute jumps 
###################


p <- 1/50 # probability of injury on one jump

# Simulate the outcome of two jumps 
injury <- sample(c(TRUE,FALSE), size=2, replace=TRUE, prob=c(p,1-p))
anyInjury <- any(injury)

# Display simulation results
injury
anyInjury

# Replicate the simulation many times, say, 100,000 times
N <- 1e5
# Simulate 200,000 jumps
injury <- sample(c(TRUE,FALSE), size=2*N, 
	replace=TRUE, prob=c(p,1-p))
# Reshape the result as a 100,000 by 2 matrix
dim(injury) <- c(N,2)

# For each row, determine if any injury occured in the two jumps
anyInjury <- logical(N)  
for (i in 1:N) anyInjury[i] <- any(injury[i,])
# anyInjury <- apply(injury,1,any) 
# same thing but faster using R function 'apply'

# Apply the Law of Large Numbers to estimate the probability 
# of an injury in two jumps
estimatedProbInjury <- mean(anyInjury) 

# True probability of an injury 
trueProbInjury <- 1 - (1-p)^2  # also equal to 2*p - p^2 ...  

# How do the estimate and true probability agree? 
c(estimate=estimatedProbInjury, true=trueProbInjury)




