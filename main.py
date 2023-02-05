from statisfy import Statify
from probabilify import Probabilify

dice = [1, 2, 3, 4, 5, 6]
die = Probabilify(dice)
# probability of rolling a even number
evens = [2, 4, 6]
print(die.probability(evens))
# probablity a 1 ginven that an odd number was rolled
odds = [1, 3, 5]

cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS'
         ]
deck = Probabilify(cards)
# probability of drawing a heart
hearts = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
print(deck.probability(hearts))
# if drawing two cards from a deck what is the probability of drawing a ace and face card
aces_faces = ['AH', 'AD', 'AC', 'AS', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QS', 'KH', 'KD', 'KC', 'KS']
# print(deck.at_most_one_joint(aces_faces, 2))

# print the total permutations of a deck of cards
print(deck.permutations())

wines = ['A', 'B', 'C']
outcome = ('?', 'A', '?')
outcome2 = ('A', '?', '?')
positions = 3
rankings = Probabilify(wines)
ss = rankings.get_sample_space(observations=positions, replacement=True, duplicates=False)
print(ss)
print(len(ss))
print(rankings.probability_of_outcome(ss, outcome, keep_position=True))
print(rankings.probability_of_outcome(ss, outcome2, keep_position=True))


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
# # load the csv from statisfy\P2-Demographic-Data.csv
# D = Statify('statisfy\P2-Demographic-Data.csv')
# # D.display_data()
# D.summary()
# D.histogram(key='Birth rate')
#

