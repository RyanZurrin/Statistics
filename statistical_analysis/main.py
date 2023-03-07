import util
from probabilify import Probabilify
from statify import Statify

# test the proability distribution of rolling two dice
dice = Probabilify([1, 2, 3, 4, 5, 6])
dice.define_sample_space(observations=2, replacement=True)
print(dice.sample_space)
# probability distribution of rolling two dice and summing them
Y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def prob_func(x, y):
    return sum(x) == y


prob_dist = dice.get_probability_distribution(Y, prob_func)
print(prob_dist)

# print the expected value of the probability distribution
print(dice.expected_value())

# print the mean of the sample space
print(dice.mean())