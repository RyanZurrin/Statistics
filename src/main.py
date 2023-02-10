from statify import Statify
from probabilify import Probabilify


# dice1 = [1, 2, 3, 4, 5, 6]
# dice2 = [1, 2, 3, 4, 5, 6]
# die = Probabilify(dice1)
# # probability of rolling a even number
# evens = [2, 4, 6]
# print(die.probability(evens))
# # probablity a 1 ginven that an odd number was rolled
# odds = [1, 3, 5]
#
# cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
#          'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
#          'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
#          'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS'
#          ]
# deck = Probabilify(cards)
# # differenct combos to dray 2 cards from a deck
# print("combinations of cards from a deck of cards")
# print(deck.combinations())
# # probability of drawing a heart
# hearts = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
# print(deck.probability(hearts))
# # if drawing two cards from a deck what is the probability of drawing a ace and face card
# aces_faces = ['AH', 'AD', 'AC', 'AS', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QS', 'KH', 'KD', 'KC', 'KS']
# # print(deck.at_most_one_joint(aces_faces, 2))
#
# # print the total permutations of a deck of cards
# print("total permutations of a deck of cards")
# print(deck.permutations())
#
# print the total permutations of a deck of cards with replacement


# A vehicle arriving at an intersection can turn right, turn left, or continue straight ahead.
# The experiment consists of observing the movement of a single vehicle through the intersection.
# a. List the sample space for this experiment.
# b. Assuming that all sample points are equally likely, find the probability that the vehicle turns.
print("total direction two cars can turn form stop light")
# print(die.permutations())
directions = ['R', 'L', 'S']
direction = Probabilify(directions)
# probability car will turn
num_cars = 2
ss = direction.get_sample_space(observations=num_cars, replacement=True)
# probablilty at only one car will turn left
turns = [('L', 'R'), ('S', 'L'), ('L', 'S'), ('R', 'L')]
print(direction.probability_of_outcomes(ss, turns, keep_position=True, replacement=False))





# # outcomes = [('A', 'B', 'A', 'A'), ('B', 'B', 'B', 'B')]
# positions = 2
# rankings = Probabilify(wines)
# print("permutations of wines")
# print(rankings.permutations())
# ss = rankings.get_sample_space(observations=positions, replacement=True,
#                                duplicates=True)
# print(ss)
# print(len(ss))
# print(rankings.probability_of_outcomes(ss, outcomes, keep_position=True))
#
# # chose 2 out of 4, with replacement
# print("chose 2 out of 4, with replacement")
# print(rankings.nCp(4, 2))

# # Problibilify is my own term for turning the word probability into a verb of action potential
# # Probabilify is a class that takes a list of objects and turns it into a probability object

# Crete a die object with 6 sides
# dice1 = [1, 2, 3, 4, 5, 6]
# # Turn the dice into a probabilify object
# dice = Probabilify(dice1)
# # build a sample space of 2 rolls
# rolls = 2
# ss = dice.get_sample_space(observations=rolls, replacement=True)
#
# # probability of rolling two dice such that the total is 10 or greater
# outcomes = [(6, 4), (6, 5), (6, 6), (5, 5), (5, 6), (4, 6)]
# dice.probability_of_outcomes(ss, outcomes, keep_position=True)
#
#
#Three patients enter the hospital and randomly choose stations 1, 2, or 3 for service.
# Then, the sample space S contains the following
# patients = ['A', 'B', 'C']
# stations = [1, 2, 3]
# # # Create a list of the possible outcomes
# p = Probabilify(patients)
# ss = p.get_sample_space(observations=3, replacement=True)
#


#
# A = Statify()
# B = Statify()
#
#
# print(A.mean())
# print(B.mean())
# print(A.median())
# print(B.median())
# print(A.mode())
# print(B.mode())
# print(A.midpoint())
# print(B.midpoint())
# print(A.standard_deviation())
# print(B.standard_deviation())
# A.display_data()
# B.display_data()
# print(A.covariance(B))
# print(A.correlation_coefficient(B))
#
# C = A + B
# C.display_data()
# print(C.mean())
# print(C.median())
# print(C.mode())
# print(C.midpoint())
# print(C.standard_deviation())
# print(C.covariance(B))
# print(C.correlation_coefficient(B))
# print(C.covariance(A))
# print(C.correlation_coefficient(A))
#
# A.histogram()
# B.histogram()
# C.histogram()
# A.box_plot()
# B.box_plot()
# C.box_plot()
#
# # load the csv from statify\P2-Demographic-Data.csv
# D = Statify('statify\P2-Demographic-Data.csv')
# # D.display_data()
# D.summary()
# D.histogram(key='Birth rate')
#
#
