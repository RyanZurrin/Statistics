import unittest
# append the parent directory to the path
import sys, os

sys.path.append(os.path.realpath((os.path.dirname(__file__) + '/../')))
from src.probabilify import Probabilify

dice1 = [1, 2, 3, 4, 5, 6]
cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH',
         'QH', 'KH',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
         'QD', 'KD',
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC',
         'QC', 'KC',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS',
         'QS', 'KS'
         ]
wines = ['A', 'B']
outcomes = [('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B')]


# test the factorial function with a list of numbers
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        factorials = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        for number, factorial in zip(numbers, factorials):
            self.assertEqual(Probabilify.factorial(number), factorial)


# test the permutations function with a list of numbers
class TestPermutations(unittest.TestCase):
    # total permutations of a deck of cards and a die
    deck = Probabilify(cards)
    die = Probabilify(dice1)

    def test_die_permutations(self):
        self.assertEqual(Probabilify.permutations(self.die), 720)

    def test_deck_permutations(self):
        self.assertEqual(Probabilify.permutations(self.deck),
                         80658175170943878571660636856403766975289505440883277824000000000000)


# test the combinations function with a list of numbers
class TestCombinations(unittest.TestCase):
    # total combinations of a deck of cards and a die
    deck = Probabilify(cards)
    die = Probabilify(dice1)

    def test_die_combinations(self):
        self.assertEqual(Probabilify.combinations(self.die, choose=2), 15)
        self.assertEqual(Probabilify.combinations(self.die, choose=2,
                                                  with_replacement=True), 21)

    def test_deck_combinations(self):
        self.assertEqual(Probabilify.combinations(self.deck, choose=5), 2598960)


# test the probability of rolling a even number on a die
class TestProbability(unittest.TestCase):
    def test_probability_of_events(self):
        die = Probabilify(dice1)
        evens = [2, 4, 6]
        self.assertEqual(die.probability(evens), 0.5)


# test nCr
class TestNcr(unittest.TestCase):
    def test_ncr(self):
        self.assertEqual(Probabilify.nCr(10, 5), 252.0)
        self.assertEqual(Probabilify.nCr(10, 5, replacement=True), 2002.0)
        self.assertEqual(Probabilify.nCr(5, 3), 10)
        self.assertEqual(Probabilify.nCr(5, 3, replacement=True), 35)
        self.assertEqual(Probabilify.nCr(5, 4), 5)
        self.assertEqual(Probabilify.nCr(5, 4, replacement=True), 70)
        self.assertEqual(Probabilify.nCr(5, 5), 1)
        self.assertEqual(Probabilify.nCr(5, 5, replacement=True), 126)


if __name__ == '__main__':
    unittest.main()
