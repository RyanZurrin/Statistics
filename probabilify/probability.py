import itertools
from itertools import combinations
from statistics import *

from statisfy import Statify
import tensorflow as tf
import tensorflow_probability as tfp


# class to turn data into a probability object, given a data set
# this class will let us ask questions about the data to help
# us understand how probable certaoin events are

class Probabilify(Statify):

    def __init__(self, data):
        super().__init__(data)
        self.__data = data

    # method to return the data
    @property
    def data(self):
        """
        :return: the data
        """
        return self.__data

    def count(self, values):
        """
        Counts the number of times a value or set of values appear in the data set
        :param values: the value or set of values to be counted
        :return: the number of times the value or set of values appear in the data set
        """
        # if the values are not a list, make them a list
        if not isinstance(values, list):
            values = [values]
        # count the number of times the values appear in the data set
        count = 0
        for value in values:
            count += self.data.count(value)
        return count

    def factorial(self, n):
        """
        Calculates the factorial of a number
        :param n: the number
        :return: the factorial of the number
        """
        # calculate the factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    def permutations(self, values=None):
        """
        Calculates the number of permutations of a set of values
        :param values: the set of values
        :return: the number of permutations
        """
        # if values is not given, use the data set
        if values is None:
            values = self.data
        # if the values are not a list, make them a list
        if not isinstance(values, list):
            values = [values]
        # calculate the number of permutations which is the length of the data set
        # factorial.
        permutations = self.factorial(len(self.data))
        return permutations

    def combinations(self, values=None):
        """
        Calculates the number of combinations of a set of values
        :param values: the set of values
        :return: the number of combinations
        """
        # if values is not given, use the data set
        if values is None:
            values = self.data
        # if the values are not a list, make them a list
        if not isinstance(values, list):
            values = [values]
        # calculate the number of combinations
        combinations = 1
        for value in values:
            combinations *= self.data.count(value)
        return combinations

    def nCp(self, n, p):
        """
        Calculates the number of combinations of n things taken p at a time
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of combinations
        """
        # calculate the number of combinations
        combinations = self.factorial(n) / (
                self.factorial(p) * self.factorial(n - p))
        return combinations

    def nCp_with_replacement(self, n, p):
        """
        Calculates the number of combinations of n things taken p at a time with replacement
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of combinations
        """
        # calculate the number of combinations
        combinations = self.factorial(n + p - 1) / (
                self.factorial(p) * self.factorial(n - 1))
        return combinations

    def nPr(self, n, p):
        """
        Calculates the number of permutations of n things taken p at a time
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of permutations
        """
        # calculate the number of permutations
        permutations = self.factorial(n) / self.factorial(n - p)
        return permutations

    def nPr_with_replacement(n, p):
        """
        Calculates the number of permutations of n things taken p at a time with replacement
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of permutations
        """
        # calculate the number of permutations
        permutations = n ** p
        return permutations

    # method to return the probability of a given value
    def probability(self, value, trials=1):
        """
        CaLculates the probablity a value or set of values will be picked  from
        the data set over a given number of trials
        :param value:  the value or set of values to be picked
        :param trials: the number of trials to be run
        :return: the probability of the value or set of values being picked
        """
        # get the number of times the value or values appear in the data set
        count = self.count(value)
        # calculate the probability
        probability = count / (len(self.data) * trials)
        return probability

    def get_sample_space(self, observations, outcomes=None, replacement=False):
        """
        Calculates the sample space for a given number of observations and outcomes
        :param replacement:
        :param outcomes: list of possible outcomes
        :param observations: the number of observations
        :return: the sample space
        """
        #
        # Example:
        # Consider a situation where cars entering an intersection each could turn
        # right, turn left, or go straight.
        # An experiment consists of observing two vehicles moving through the intersection.
        # How many sample points are there in the sample space?
        # There are 3 possible outcomes for the first car and 3 possible outcomes for the second car.
        # The sample space is the set of all possible outcomes for the experiment.
        # The sample space for this experiment is {(right, right), (right, left), (right, straight),
        # (left, right), (left, left), (left, straight), (straight, right), (straight, left),
        # (straight, straight)}.
        # There are 9 sample points in the sample space.

        # get the sample space: given outcomes of 'L', 'R', 'S' and 2 observations, the sample space is
        # [('L', 'L'), ('L', 'R'), ('L', 'S'), ('R', 'L'), ('R', 'R'), ('R', 'S'), ('S', 'L'), ('S', 'R'), ('S', 'S')]
        # if replacement is True, the sample space is
        if outcomes is None:
            outcomes = self.data

        sample_space = []
        for i in range(observations):
            sample_space.append(outcomes)

        if replacement:
            sample_space = list(itertools.product(*sample_space))
        else:
            sample_space = list(itertools.combinations(outcomes, observations))
        return sample_space

        # if replacement:
        #     sample_space = list(itertools.combinations(outcomes, observations))
        # else:
        #     sample_space = list(
        #         itertools.product(outcomes, repeat=observations))
        #
        # return sample_space

    # for i in range(observations):
    #     sample_space.append(outcomes)
    # sample_space = list(itertools.product(*sample_space))
    # # remove duplicates
    # sample_space = list(set(sample_space))
    # return sample_space
