# Let 𝑛 ≥ 3 be an integer. Suppose there are two urns U and V. Urn U contains 2 white balls and 𝑛
# black balls. Urn V contains 𝑛 white balls and 2 black balls. One urn is selected at random, and
# then 2 balls are drawn without replacement from this urn. If 2 black balls are drawn, what is the
# probability that they come from urn U?

# create function to calculate the probability distribution of the number of black balls drawn
# from the urn with 2 white balls and n black balls
# sample(x, size, replace = False, prob = NULL)
n <- 10
y <- 0:2
py <- c(n^2-n+2, 8*n, n^2-n+2) / 2 / (n+2) / (n + 1)
u <- rep(c("w", "b"), c(2, n))
v <- rep(c("w", "b"), c(n, 2))
EY <- sum(py * y)

urn <- rep(c("w", "b"), c(2, n))
if (urn == "u") {
  balls <- sample("u", 2)
  y <- sum(balls == "b")
} else {
  balls <- sample(urn, 2)
  y <- sum(balls == "b")
}