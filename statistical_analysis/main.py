import util
from probabilify import Probabilify
from statify import Statify

# # test the proability distribution of rolling two dice
# dice = Probabilify([1, 2, 3, 4, 5, 6])
# dice.define_sample_space(observations=2, replacement=True)
# # print(dice.sample_space)
# # probability distribution of rolling two dice and summing them
# Y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# def prob_func(x, y):
#     return sum(x) == y
#
#
# prob_dist = dice.get_probability_distribution(Y, prob_func)
# print(prob_dist)
#
# # print the expected value of the probability distribution
# print(dice.expected_value(Y, prob_func))
#
#
# # each of 3 balls are randomly placed into one of tree bowls. Find the probability
# # distribution for Y = number of empty bowls.
# balls = Probabilify([1, 2, 3])
#
# # define the sample space
# balls.define_sample_space(observations=3, replacement=True)
# # print(balls.sample_space)
#
# # define Y = number of empty bowls
# Y = [0, 1, 2]
#
# # define the probability function
# def prob_func(x, y):
#     # count how many different values are in x (the sample space) and compare
#     # it to y (the number of empty bowls)
#     return (3 - len(set(x))) == y
#
# # get the probability distribution
# prob_dist = balls.get_probability_distribution(Y, prob_func)
# print(prob_dist)
#
# # mean of the probability distribution
# print(balls.expected_value(Y, prob_func))

print(Probabilify.dbinom(8, 50, .3))

