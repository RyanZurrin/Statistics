import os, sys
import random
from pprint import pprint

sys.path.append(os.path.realpath((os.path.dirname(__file__) + '/../')))
from src.probabilify import Probabilify
from src.util.rprint import rprint
from src.statify import Statify

# dice1 = [1, 2, 3, 4, 5, 6]
# die = Probabilify(dice1)
#
# # get the total combinations of rolling two dice
# print("total combinations of rolling two dice")
# print(die.combinations(choose=2, with_replacement=True, allow_duplicates=True))
# print("total combinations of a die")
# print(die.combinations())
#
# # # probability of rolling a even number
# # evens = [2, 4, 6]
# # print(die.probability(evens))
# # # probablity a 1 ginven that an odd number was rolled
# # odds = [1, 3, 5]
#
# cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH',
#          'QH', 'KH',
#          'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
#          'QD', 'KD',
#          'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC',
#          'QC', 'KC',
#          'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS',
#          'QS', 'KS'
#          ]
# deck = Probabilify(cards)
# # # differenct combos to dray 2 cards from a deck
# print("combinations of cards from a deck of cards")
# print(deck.combinations(choose=5))

# # probability of drawing a heart
# hearts = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
# print(deck.probability(hearts))
# # if drawing two cards from a deck what is the probability of drawing a ace and face card
# aces_faces = ['AH', 'AD', 'AC', 'AS', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QS', 'KH', 'KD', 'KC', 'KS']
# # print(deck.at_most_one_joint(aces_faces, 2))
#
# print the total permutations of a deck of cards
# print("total permutations of a deck of cards")
# print(deck.permutations())
#
# print the total permutations of a deck of cards with replacement


# A vehicle arriving at an intersection can turn right, turn left, or continue straight ahead.
# The experiment consists of observing the movement of a single vehicle through the intersection.
# a. List the sample space for this experiment.
# b. Assuming that all sample points are equally likely, find the probability that the vehicle turns.
# print("total direction two cars can turn form stop light")
# # print(die.permutations())
# directions = ['R', 'L', 'S']
# direction = Probabilify(directions)
# # probability car will turn
# num_cars = 2
# ss = direction.get_sample_space(observations=num_cars, replacement=True)
# # probablilty at only one car will turn left
# turns = [('L', 'R'), ('S', 'L'), ('L', 'S'), ('R', 'L')]
# print(direction.probability_of_outcomes(ss, turns, keep_position=True, replacement=False))


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
# print(rankings.nCr(4, 2))

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
# Three patients enter the hospital and randomly choose stations 1, 2, or 3 for service.
# Then, the sample space S contains the following
# patients = ['A', 'B', 'C']
# stations = [1, 2, 3]
# # # Create a list of the possible outcomes
# p = Probabilify(patients)
# ss = p.get_sample_space(observations=3, replacement=True)
#

# Every person's blood type is  either A, B, AB, or O.
# In addition, each individual either has the Rhesus (Rh+) factor or does not (Rh-).
#  A medical technician records a person's blood type and Rh factor. List the sample space for this experiment.
# blood_types = ['A', 'B', 'AB', 'O']
# rh_factors = ['+', '-']
# blood = Probabilify(blood_types)
# print(blood.power_set())
# print(blood.sample_space)
# rh = Probabilify(rh_factors)
# print(rh.power_set())
# print(rh.sample_space)
# ss = blood.intersection(rh)
# print(ss)
# test = blood * rh
# print(test)
#
#
# # create an experiment of a coin flip
# def coin_flip():
#     coin = ['H', 'T']
#     # randomize the coin flip
#     random.shuffle(coin)
#     return coin[0]


# resutls = Probabilify.simulate_experiment(coin_flip, 10000, display=False)
# results = Probabilify(resutls)
# print(results.probability_of_outcomes(results.sample_space, 'H'))

# find the probability of of flipping exactlyi two heads on three coin flips
# coin = ['H', 'T']
# coin = Probabilify(coin)
# ss = coin.get_sample_space(observations=3, replacement=True)
# outcomes = [('H', 'H', 'T'), ('H', 'T', 'H'), ('T', 'H', 'H')]
# print(coin.probability_of_outcomes(ss, outcomes, keep_position=True))

# find the probability of rolling doubles on two 6 sided dice
dice = [1, 2, 3, 4, 5, 6]
dice = Probabilify(dice)
ss = dice.get_sample_space(observations=3, replacement=True, display=False)
# event A is all three rolls have the same value
event_A = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6)]
# event B is all three nubmer are different
unique_values = []
for sample in ss:
    test = set(sample)
    if len(test) == 3:
        unique_values.append(sample)
event_B = unique_values
# event C is the number are either in increasing or decreasing order
increasing = []
decreasing = []
for sample in ss:
    if sample[0] < sample[1] < sample[2]:
        increasing.append(sample)
    elif sample[0] > sample[1] > sample[2]:
        decreasing.append(sample)
event_C = increasing + decreasing
print('length of event C', len(event_C))
print(event_C)
# loop through the sample space and print out every tine the values in are unique
# get the probability of event A
dice.probability_of_outcomes(ss, event_A, keep_position=True)
# get the probability of event B
dice.probability_of_outcomes(ss, event_B, keep_position=True)
# get the probability of event C
dice.probability_of_outcomes(ss, event_C, keep_position=True)


# outcomes = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
# print(dice.probability_of_outcomes(ss, outcomes, keep_position=True))

# The Wood types available are  holly, elm, maple, and wenge. The core materials
# on offer are phoenix feather, unicorn hair, and dragon scale and raven feather and thestral tail.
#
# wood_types = ['holly', 'elm', 'maple', 'wenge']
# core_materials = ['phoenix feather', 'unicorn hair', 'dragon scale',
#                   'raven feather', 'thestral tail']
# wood = Probabilify(wood_types)
# core = Probabilify(core_materials)
# wands = wood * core
# wands.sample_space = wands.remove_sample(('elm', 'dragon scale'))
# wands.display_data()
# wands.display_sample_space()


#  new secretary has been given n computer passwords, only one of
# which will permit access to a computer file. Because the secretary has no idea which password is
# correct, he chooses one of the passwords at random and tries it. If the password is incorrect, he
# discards it and randomly selects another password from among those remaining, proceeding in
# this manner until he finds the correct password.
# a) What is the probability that he obtains the right password on the first try?
# b) What is the probability that he obtains the correct password on the second try? The third
# try?
# c) A security system has been set up so that if three incorrect passwords are tried before the
# correct one, the computer file is locked and access to it denied. If n = 7, what is the
# probability that the secretary will gain access to the file?

# n = 7
# passowrds = []
# for i in range(n):
#     passowrds.append(str(i))
#
# passwords = Probabilify(passowrds)
# ss = passwords.get_sample_space(observations=1, replacement=True, flatten=True)
#
# # a) What is the probability that he obtains the right password on the first try?
# print(passwords.probability_of_outcomes(ss, "1", keep_position=True))
#
# # b) What is the probability that he obtains the correct password on the second try? The third
# # try?
# print(passwords.probability_of_outcomes(ss, "1", keep_position=True))
#
# # c) A security system has been set up so that if three incorrect passwords are tried before the
# # correct one, the computer file is locked and access to it denied. If n = 7, what is the
# # probability that the secretary will gain access to the file?
# ss = passwords.get_sample_space(observations=3, replacement=False)
# possible_outcomes = [("1", '?', '?'), ('?', "1", '?'), ('?', '?', "1")]
# print(passwords.probability_of_outcomes(ss, possible_outcomes,
#                                         keep_position=True))

# A : “positive diagnostic test”, i.e. test indicates disease
# B : “having a given disease”
# Probability of positive test given disease (sensitivity): P(A|B) = 0.9
# Probability of negative test given no disease (specificity): P(A|B) = 0.9
# Prevalence of disease in population: P(B) = 0.01
# Using Bayes’ rule, the probability of having the disease given a positive diagnostic test is

# rs1 = passwords.srswr(4)
# print(rs1)
#
# rs2 = passwords.srswor(4)
# print(rs2)
#
# # An experiment consists of tossing a pair of dice.
# # a. Use the combinatorial theorems to determine the number of sample points in the sample space
# # .
# # b. Find the probability that the sum of the numbers appearing on the dice is equal to 7 .
#
# dice = [1, 2, 3, 4, 5, 6]
# dice = Probabilify(dice)
# ss = dice.get_sample_space(observations=2, replacement=True)
# outcomes = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
# print(dice.probability_of_outcomes(ss, outcomes, keep_position=True))

# How many different seven-digit telephone numbers can be formed if the first digit cannot be zero?

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# numbers = Probabilify(numbers)
# ss = numbers.get_sample_space(observations=7, replacement=True, display=False)
# print(len(ss))
# print((9 * 10 ** 6))
# outcomes = [('0', '?', '?', '?', '?', '?', '?')]
# # vae = numbers.probability_of_outcomes(ss, outcomes,  display=False)
# # print(vae)
#
#
# # A fleet of nine taxis is to be dispatched to three airports in such a way that three
# # go to airport A, five go to airport B, and one goes to airport C. In how many distinct ways can this be accomplished?
# print(Probabilify.nPk(17, [2, 5, 10]))
# #
# # Ten teams are playing in a basketball tournament. In the first round, the teams are randomly assigned to games 1,2,3,4 and
# #  In how many ways can the teams be assigned to the games?
# print(Probabilify.nPk(10, [2, 2, 2, 2, 2]))
#
# # If  2n teams are to be assigned to games 1,2,..,n
# # in how many ways can the teams be assigned to the games if n = 3?
# print(Probabilify.nPk(2 ** 3, [2, 2, 2]))

# Students attending the University of Florida can select from 130 major areas of study. A student's major is identified in the registrar's records with a two-or three-letter code (for example, statistics majors are identified by STA, math majors by MS). Some students opt for a double major and complete the requirements for both of the major areas before graduation. The registrar was asked to consider assigning these double majors a distinct two-or three-letter code so that they could be identified through the student records' system.
# a. What is the maximum number of possible double majors available to University of Florida
# students?
# b. If any two-or three-letter code is available to identify majors or double majors, how many major codes are available?
# c. How many major codes are required to identify students who have either a single major or a double major?
# d. Are there enough major codes available to identify all single and double majors at the University of Florida?
# print("Problem 2.49")
# # a
# print(Probabilify.nCr(130, 2))
#
# # b, there are 26 letters in the alphabet, and there are _ _ or _ _ _ combinations
# val1 = rprint(26 ** 2 + 26 ** 3)
#
# # c
# val2 = rprint(130 + 130 * (130 - 1) / 2)
# print('val1+val2=', val1 + val2)
#
# # d
# print(130 + 130 * (130 - 1) / 2 < 26 ** 2 + 26 ** 3)

# A local fraternity is conducting a raffle where 50 tickets are to be sold-one per customer. There are three prizes to be awarded. If the four organizers of the raffle each buy one ticket, what is the probability that the four organizers win
# a. all of the prizes?
# b. exactly two of the prizes?
# c. exactly one of the prizes?
# d. none of the prizes?
# print("Problem 2.50")
# # a
# print(Probabilify.nCr(4, 3) / Probabilify.nCr(50, 3))
#
# # b
# print(Probabilify.nCr(4, 2) * Probabilify.nCr(46, 1) / Probabilify.nCr(50, 3))
#
# # c
# print(Probabilify.nCr(4, 1) * Probabilify.nCr(46, 2) / Probabilify.nCr(50, 3))
#
# # d
# print(Probabilify.nCr(46, 3) / Probabilify.nCr(50, 3))

# There are 4 blood types: A, B, AB, and O, and two rhesus factors: + and -.
# How many possible combinations of blood type and rhesus factor are there?

# print(Probabilify.nCr(4, 1) * Probabilify.nCr(2, 1))

# What is the difference beteen an arangement and a combination of elements?
# An arrangement is a permutation of elements, while a combination is a selection of elements.
# using the letters A, B, C, D, and E, how many arrangements of 5 letters are possible and how many combinations of 5 letters are possible?

# letters = ['A', 'B', 'C', 'D', 'E']
# letters = Probabilify(letters)
# ss = letters.get_sample_space(observations=5, replacement=True, display=False)
# print(len(ss))
# print(Probabilify.nCr(5, 5))

# 10 performers are cometing in a singing contest. They are ranked by a jury by order
# of best perfromances. The top 3 performers are awarded prizes. How many ways are there to rank the 10 performers?
# print('performance " ', Probabilify.nPr(10, 3))

# 3 blue balls, 5 red balls in an urn
# urn = ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R']
# urn = Probabilify(urn)
# ss = urn.get_sample_space(observations=2, replacement=False, display=True)
# # probability of drawing 2 blue balls
# print(urn.probability_of_outcomes(ss, [('B', 'B')]))

#  in a room of 20 people what is probability of 2 people not sharing a birthday?
# 365 days in a year, 20 people, 364 days to choose from
# print(1 - Probabilify.nCr(364, 19) / Probabilify.nCr(365, 20))
#
# print(Probabilify.nCr(10, 5))
# print(Probabilify.nCr(10, 5, replacement=True))
# print(Probabilify.nPr(10, 5))
#
# dice1 = [1, 2, 3, 4, 5, 6]
# die = Probabilify(dice1)
# evens = [2, 4, 6]
# print(die.probability(evens))

# a balanced cound is tossed 4 times
# coin_sides = ['H', 'T']
# coin = Probabilify(coin_sides)
# ss = coin.get_sample_space(observations=4, replacement=True)
# # let even A be the even that both the first and last toss show the same side
#
# # let event B be the even that Heads appears in exactly 2 tosses
# # [('H', 'H', 'H', 'H'), ('H', 'H', 'H', 'T'), ('H', 'H', 'T', 'H'), ('H', 'H', 'T', 'T'), ('H', 'T', 'H', 'H'), ('H', 'T', 'H', 'T'), ('H', 'T', 'T', 'H'), ('H', 'T', 'T', 'T'), ('T', 'H', 'H', 'H'), ('T', 'H', 'H', 'T')]
# # [('T', 'H', 'T', 'H'), ('T', 'H', 'T', 'T'), ('T', 'T', 'H', 'H'), ('T', 'T', 'H', 'T'), ('T', 'T', 'T', 'H'), ('T', 'T', 'T', 'T')]
# event_A = [('H', 'H', 'H', 'H'),  ('H', 'H', 'T', 'H'),  ('H', 'T', 'H', 'H'),  ('H', 'T', 'T', 'H'), ('T', 'H', 'H', 'T'),
#            ('T', 'H', 'T', 'T'),  ('T', 'T', 'H', 'T'), ('T', 'T', 'T', 'T')
#            ]
# event_B = [
#     ('H', 'H', 'T', 'T'), ('H', 'T', 'H', 'T'), ('H', 'T', 'T', 'H'),
#     ('T', 'H', 'H', 'T'),
#     ('T', 'H', 'T', 'H'), ('T', 'T', 'H', 'H')
# ]  # 6/16 = 3/8
# # Calculate P(A intersect B) and P(A union B)
# probA = coin.probability_of_outcomes(ss, event_A, keep_position=True)
# probB = coin.probability_of_outcomes(ss, event_B)
#
# p_AintersectB = coin.intersect(event_A, event_B, ss)
# p_AorB = probA + probB - coin.intersect(event_A, event_B, ss)
# print('p_AintersectB=', p_AintersectB)
# print('p_AorB=', p_AorB)
