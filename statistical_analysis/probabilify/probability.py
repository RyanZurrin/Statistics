import itertools
import math
import random
from pprint import pprint
from rpy2 import robjects as ro
from tabulate import tabulate

from statistical_analysis.statify import Statify


# class to turn data into a probability object, given a data set
# this class will let us ask questions about the data to help
# us understand how probable certaoin events are

class Probabilify(Statify):

    def __init__(self, data):

        self.__data = data
        # create the sample space from the data set
        self.sample_space = self.create_sample_space()
        self.probability_distribution = self.__create_probability_distribution()
        super().__init__(self.sample_space)

    def __add__(self, other):
        """
        Union of two sample spaces ('+' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for +: 'Probabilify' and '{}'".format(
                    type(other)))
        return self.union(other)

    def __sub__(self, other):
        """
        Intersection of two sample spaces ('-' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for -: 'Probabilify' and '{}'".format(
                    type(other)))
        # create a new sample space
        sample_space = list(set(self.sample_space) - set(other.sample_space))
        # create a new Probabilify object
        new_prob = Probabilify(sample_space)
        return new_prob

    def __mul__(self, other):
        """
        Cartesian product of two sample spaces ('*' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for *: 'Probabilify' and '{}'".format(
                    type(other)))
        # create a new sample space
        return self.cartesian_product(other)

    def __truediv__(self, other):
        """
        Difference of two sample spaces ('/' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for /: 'Probabilify' and '{}'".format(
                    type(other)))
        # create a new sample space
        sample_space = list(set(self.sample_space) - set(other.sample_space))
        # create a new Probabilify object
        new_prob = Probabilify(sample_space)

    def __pow__(self, other):
        """
        Power set of a sample space ('**' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for **: 'Probabilify' and '{}'".format(
                    type(other)))
        return self.power(other)

    # overload the ^ operator
    def __xor__(self, other):
        """
        symmetric difference of two sample spaces ('^' operator)
        """
        # if the other object is not a Probabilify object, raise an error
        if not isinstance(other, Probabilify):
            raise TypeError(
                "unsupported operand type(s) for ^: 'Probabilify' and '{}'".format(
                    type(other)))
        # create a new sample space
        sample_space = list(set(self.sample_space) ^ set(other.sample_space))
        # create a new Probabilify object
        new_prob = Probabilify(sample_space)
        return new_prob

    # method to return the data
    @property
    def data(self):
        """
        :return: the data
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        :param data: the data
        """
        self.__data = data

    def __create_probability_distribution(self):
        """
        Creates a probability distribution from the sample space
        """
        # create a dictionary to store the probability distribution
        probability_distribution = {}
        # loop through the sample space
        for sample in self.sample_space:
            # get the probability of the sample
            probability = self.probability_of_outcomes(self.sample_space,
                                                       sample)
            # add the sample and probability to the dictionary
            probability_distribution[sample] = probability
        # return the probability distribution
        return probability_distribution

    def get_probability_distribution(self, Y, prob_fx):
        """
        Creates a probability distribution from the sample space
        """
        prob_dist = {}
        for y in Y:
            prob_dist[y] = 0
            for x in self.sample_space:
                if prob_fx(x, y):
                    prob_dist[y] += 1
        for y in Y:
            prob_dist[y] /= len(self.sample_space)

        return prob_dist

    def LOTUS(self, other):
        """
        LOTUS of two sample spaces
        :param other: the other sample space
        :return: the LOTUS of the two sample spaces
        """
        # create a new sample space
        sample_space = list(set(self.sample_space) | set(other.sample_space))
        # create a new Probabilify object
        new_prob = Probabilify(sample_space)
        return new_prob

    def expected_value(self, Y=None, prob_fx=None):
        """
        Calculates the expected value of the data set
        :return: the expected value of the data set
        """
        # calculate the expected value from the sample space
        if Y is None:
            Y = self.sample_space
        if prob_fx is None:
            prob_fx = self.probability_of_outcomes
        prob_dist = self.get_probability_distribution(Y, prob_fx)
        expected_value = 0
        for y in Y:
            # print("y: {}, prob_dist[y]: {}".format(y, prob_dist[y]))
            expected_value += y * prob_dist[y]
        return expected_value

    def remove_sample(self, sample):
        """
        Removes a sample from the sample space in place
        :param sample: the sample to be removed
        :return: the new sample space
        """
        print("Removing sample: {}".format(sample))
        # remove the sample from the sample space
        self.sample_space.remove(sample)
        return self.sample_space

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

    def create_sample_space(self):
        """
        Creates a sample space for the data set
        :return: the sample space
        """
        # create the sample space
        sample_space = list(itertools.product(self.data, repeat=1))
        # if the data is only a list of values make sure the sample space is a list of
        # values and not a list of tuples
        return sample_space

    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a number
        :param n: the number to be factored
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

    def combinations(self,
                     choose=1,
                     values=None,
                     with_replacement=False,
                     allow_duplicates=False):
        """
        Calculates the number of combinations of a set of values, for instance

        :param choose: the number of values to be chosen
        :param values: the set of values
        :param with_replacement: whether or not to allow the same value to be chosen
        more than once
        :param allow_duplicates: whether or not to allow duplicate values in the
        data set
        :return: the number of combinations
        """
        # if values is not given, use the data set
        if values is None:
            values = self.data
        if not allow_duplicates:
            # if the values are not a list, make them a list
            if not isinstance(values, list):
                values = [values]
            # if the number of values to be chosen is greater than the number of
            # values in the data set, raise an error
            if choose > len(values):
                raise ValueError(
                    "choose cannot be greater than the number of values in the data set")
            # calculate the number of combinations
            if with_replacement:
                combinations = self.nCr(len(values), choose, replacement=True)
            else:
                combinations = self.nCr(len(values), choose)
        else:
            combinations = len(values) ** choose
        return combinations

    @staticmethod
    def nCr(n, r, replacement=False):
        """
        Calculates the number of combinations of n things taken p at a time
        :param n: the number of things
        :param r: the number of things taken at a time
        :param replacement: whether or not to allow the same thing to be chosen
        :return: the number of combinations
        """
        if replacement:
            combos = Probabilify.factorial(n + r - 1) / (
                    Probabilify.factorial(r) * Probabilify.factorial(n - 1))
        else:
            combos = Probabilify.factorial(n) / (
                    Probabilify.factorial(r) * Probabilify.factorial(n - r))
        return combos

    @staticmethod
    def nPr(n, r, replacement=False):
        """
        Calculates the number of permutations of n things taken p at a time
        :param n: the number of things
        :param r: the number of things taken at a time
        :param replacement: whether or not to allow the same thing to be chosen
        :return: the number of permutations
        """
        if replacement:
            permutations = n ** r
        else:
            permutations = Probabilify.factorial(n) / Probabilify.factorial(
                n - r)
            return permutations

    @staticmethod
    def nPk(n, k: list):
        """
        the number of ways of partitioning  n distinct objects into k distinct
        groups containing k_1, k_2, ..., k_i objects respectively, where each
        object appears in exactly one group. N = n! / (k_1! * k_2! * ... * k_i!)
        :param n:  the number of objects
        :param k:  groups, where the total of all groups is n
        :return:  the number of ways of partitioning n objects into k groups
        """
        denominator = 1
        for i in k:
            denominator *= Probabilify.factorial(i)
        nPk = Probabilify.factorial(n) / denominator
        return nPk

    # method to return the probability of a given value
    def probability(self, value, data=None, trials=1):
        """
        CaCalculates the probability a value or set of values will be picked  from
        the data set over a given number of trials

        :param value:  the value or set of values to be picked
        :param data:  the data set to be used
        :param trials: the number of trials to be run
        :return: the probability of the value or set of values being picked
        """
        # if data is not given, use the data set
        if data is None:
            data = self.data
        # if the value is not a list, make it a list
        if not isinstance(value, list):
            value = [value]
        # if the data is not a list, make it a list
        if not isinstance(data, list):
            data = [data]
        # if the value is not in the data set, raise an error
        if not all(x in data for x in value):
            raise ValueError("value must be in the data set")
        # calculate the probability
        probability = len(value) / len(data)
        return probability

    def define_sample_space(self,
                            observations,
                            outcomes=None,
                            replacement=False,
                            duplicates=True,
                            flatten=False,
                            display=False):
        """
        Calculates the sample space for a given number of observations and outcomes
        and sets the samples space of the object to the new sample space

        :param observations: the number of observations
        :param outcomes: list of possible outcomes
        :param replacement: whether the observations are taken with replacement
        :param duplicates: whether the observations can contain duplicates
        :param flatten:  whether to flatten the sample space
        :param display: whether to display the sample space
        :return: the sample space
        """
        if outcomes is None:
            outcomes = self.data

        sample_space = []
        for i in range(observations):
            sample_space.append(outcomes)

        if replacement:
            sample_space = list(itertools.product(*sample_space))
        else:
            sample_space = list(itertools.combinations(outcomes, observations))

        if duplicates is False:
            sample_space = [x for x in sample_space if len(set(x)) == len(x)]

        if flatten:
            sample_space = [x for y in sample_space for x in y]

        if display:
            # add a new line every 10 items
            for i in range(0, len(sample_space), 10):
                print(sample_space[i:i + 10])
            # print the total number of outcomes
            print(f'Cardinality of sample space S is : {len(sample_space)}')

        self.sample_space = sample_space
        # update super class
        super().__init__(sample_space)
        # set the probability distribution
        self.probability_distribution = self.__create_probability_distribution()

        return sample_space

    def random_sample(self, observations, outcomes=None, replacement=False):
        """
        Returns a random sample from the sample space

        :param observations: the number of observations
        :param outcomes: list of possible outcomes
        :param replacement: whether the observations are taken with replacement
        :return: the sample space
        """
        sample_space = self.get_sample_space(observations, outcomes,
                                             replacement)
        sample = random.choice(sample_space)
        return sample

    def srswr(self, n):
        """
        Simple Random Sample With Replacement
        :param n: the number of observations
        :return: the sample
        """
        sample = [random.choice(self.data) for i in range(n)]
        return sample

    def srswor(self, n):
        """
        Simple Random Sample Without Replacement
        :param n: the number of observations
        :return: the sample
        """
        sample = random.sample(self.data, n)
        return sample

    @staticmethod
    def __probability_of_outcome(sample_space,
                                 outcome,
                                 keep_position=False,
                                 replacement=False,
                                 already_found=None):
        """
        Calculates the probability of a given outcome, can use ? as a wildcard in
        the outcome strings

        :param sample_space: the sample space
        :param outcome: the outcome
        :param keep_position: whether to keep the position outcome
        :param replacement: whether the observations are taken with replacement
        :return: the probability of the outcome
        """
        if keep_position is False:
            if str(outcome).find('?') > -1:
                count = 0
                index = str(outcome).find('?', 0)
                if index > 0:
                    # get the value before the ?
                    value = str(outcome)[index - 1]
                    isValidChar = value.isalnum()
                    if not isValidChar:
                        for sample in sample_space:
                            # find all places variable value appears in the sample
                            if all([x in sample for x in outcome if x != '?']):
                                if not replacement:
                                    count += (
                                        1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1
                    else:
                        outcome_list = list(outcome)
                        # remove the ? from the list
                        for i in range(len(outcome_list)):
                            if outcome_list[i].find('?') > -1:
                                outcome_list[i] = outcome_list[i].replace('?',
                                                                          '')
                        for sample in sample_space:
                            if all([x in str(sample) for x in outcome_list if
                                    x != '?']):
                                if not replacement:
                                    # verify that sample is not already in already_found
                                    count += (
                                        1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1

                else:
                    for sample in sample_space:
                        if all([x in sample for x in outcome if x != '?']):
                            if not replacement:
                                count += (
                                    1 if sample not in already_found else 0)
                                already_found.append(sample)
                            else:
                                count += 1
                probability = count / len(sample_space)
            else:
                probability = sample_space.count(outcome) / len(sample_space)
        else:
            if str(outcome).find('?') > -1:
                count = 0
                index = str(outcome).find('?', 0)
                if index > 0:
                    # get the value before the ?
                    value = str(outcome)[index - 1]
                    isValidChar = value.isalnum()
                    if not isValidChar:
                        for sample in sample_space:
                            flags = [False] * len(outcome)
                            for i in range(len(outcome)):
                                if outcome[i] == sample[i]:
                                    flags[i] = True
                                elif outcome[i] == '?':
                                    flags[i] = True
                                else:
                                    flags[i] = False
                            if all(flags):
                                if not replacement:
                                    # verify that sample is not already in already_found
                                    count += (
                                        1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1

                    else:
                        outcome_list = list(outcome)
                        # remove the ? from the list
                        for i in range(len(outcome_list)):
                            if outcome_list[i].find('?') > -1:
                                outcome_list[i] = outcome_list[i].replace('?',
                                                                          '')
                        for sample in sample_space:
                            if all([x in str(sample) for x in outcome_list if
                                    x != '?']):
                                if not replacement:
                                    # verify that sample is not already in already_found
                                    count += (
                                        1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1
                else:
                    for sample in sample_space:
                        if all([x in sample for x in outcome if x != '?']):
                            if not replacement:
                                # verify that sample is not already in already_found
                                count += (
                                    1 if sample not in already_found else 0)
                                already_found.append(sample)
                            else:
                                count += 1
                probability = count / len(sample_space)
            else:
                # calculate the probability
                probability = sample_space.count(outcome) / len(sample_space)
        return probability, already_found

    def probability_of_outcomes(self,
                                sample_space,
                                outcome,
                                keep_position=False,
                                replacement=False,
                                display=False):
        """
        Calculates the probability of a given outcomes, can use ? as a wildcard in
        the outcome strings
        :param sample_space: the sample space
        :param outcome:  the outcome
        :param keep_position:  whether position is important
        :param display: whether to display the probability
        :param replacement: whether the observations are taken with replacement
        :return:  the probability of the outcome
        """
        outcomes = []
        if isinstance(outcome, list):
            probability = 0
            for out in outcome:
                cur_prob, outcomes = self.__probability_of_outcome(sample_space,
                                                                   out,
                                                                   keep_position,
                                                                   replacement,
                                                                   outcomes)
                probability += cur_prob
        else:
            probability, outcomes = self.__probability_of_outcome(sample_space,
                                                                  outcome,
                                                                  keep_position,
                                                                  replacement)

        if display:
            pprint(f'Probability of {outcome} is {probability}')
        return probability

    def union(self, other: 'Probabilify') -> 'Probabilify':
        """
        Returns the union of two probability spaces

        :param other: the other probability space
        :return: the union of the two probability spaces
        """
        union = Probabilify([x for x in self.sample_space if
                             x not in other.sample_space] + other.sample_space)
        union.sample_space = [x for y in union.sample_space for x in y]
        return union

    def combination(self, other: 'Probabilify') -> 'Probabilify':
        """
        Returns the combination of two probability spaces

        :param other: the other probability space
        :return: the combination of the two probability spaces
        """
        combination = Probabilify(
            [x + y for x in self.sample_space for y in other.sample_space])
        combination.sample_space = [x for y in combination.sample_space for x in
                                    y]
        return combination

    def intersection(self, other: 'Probabilify') -> 'Probabilify':
        """
        Returns the intersection of two probability spaces

        :param other: the other probability space
        :return: the intersection of the two probability spaces
        """
        intersection = Probabilify(
            [x for x in self.sample_space if x in other.sample_space])
        intersection.sample_space = [x for y in intersection.sample_space for x
                                     in y]
        return intersection

    def intersect(self, seta, setb, ss=None, return_intersection=False):
        """
        get the set of intersection values from seta and setB and then find
        the percent of that intersection of the sample space
        :param seta:
        :param setb:
        :param ss: the sample space
        :param return_intersection: whether to return the intersection
        :return:
        """
        print('seta', seta)
        print('setb', setb)
        if isinstance(seta, list):
            seta = set(seta)
        if isinstance(setb, list):
            setb = set(setb)
        intersection = list(seta.intersection(setb))
        print('intersection', intersection)
        count = 0
        # find the % of sample space the intersection consists of
        if return_intersection:
            return intersection
        if ss is None:
            ss = self.sample_space
        print('sample space', ss)
        for sample in ss:
            if sample in intersection:
                count += 1
        return count / len(ss)

    def complement(self) -> 'Probabilify':
        """
        Returns the complement of the probability space

        :return: the complement of the probability space
        """
        complement = Probabilify(
            [x for x in self.sample_space if x not in self.sample_space])
        complement.sample_space = [x for y in complement.sample_space for x in
                                   y]
        return complement

    # create a method to calculate P(A|B)
    def prob_A_given_B(self, A, B):
        """
        Returns the probability of A given B

        :param A: the probability space A
        :param B: the probability space B
        :return: the probability of A given B
        """
        return self.intersection(A).intersection(B).probability_of_outcomes(
            self.intersection(A).intersection(B).sample_space,
            self.intersection(A).intersection(B).sample_space)

    def conditional(self, other: 'Probabilify') -> 'Probabilify':
        """
        Returns the conditional probability of the two probability spaces

        :param other: the other probability space
        :return: the conditional probability of the two probability spaces
        """
        conditional = Probabilify(
            [x for x in self.sample_space if x in other.sample_space])
        conditional.sample_space = [x for y in conditional.sample_space for x in
                                    y]
        return conditional

    def cartesian_product(self, other):
        """
        Returns the cartesian product of the two probability spaces

        :param other: the other probability space
        :return: the cartesian product of the two probability spaces
        """
        cartesian_product = Probabilify(
            [x + y for x in self.sample_space for y in other.sample_space])
        cartesian_product.sample_space = [x for y in
                                          cartesian_product.sample_space for x
                                          in y]
        return cartesian_product

    def power_set(self):
        """
        Returns the power set of the sample space
        """
        # create a list of all the subsets of the sample space
        subsets = []
        # turn the subspace into a flattend list
        flattened = [item for sublist in self.sample_space for item in sublist]
        # create a list of all the subsets of the flattened list
        for i in range(len(flattened) + 1):
            subsets.append(list(itertools.combinations(flattened, i)))
        # return the list of subsets
        return subsets

    def power(self, other):
        """
        Returns the power of the two probability spaces

        :param other: the other probability space
        :return: the power of the two probability spaces
        """
        temp = self + other
        subsets = temp.power_set()
        power = Probabilify(subsets)
        power.sample_space = [x for y in power.sample_space for x in y]
        return power

    @staticmethod
    def simulate_experiment(experiment, trials, display=False):
        """
        Simulates an experiment
        :param experiment: the experiment to simulate
        :param trials: the number of trials to simulate
        :return: the results of the experiment
        """
        results = []
        for i in range(trials):
            results.append(experiment())

        if display:
            print(f'Experiment results: {results}')
        return results

    def display_sample_space(self):
        """
        Displays the sample space with pretty formatting and tabulate
        """
        print(tabulate(self.sample_space, tablefmt='psql'))

    def bayes_rule(self, event_a, event_b):
        """
        Calculate the probability of event A given event B
        P(B|A) = (P(A|B) · P(B)) / P(A)

        :param event_a: event A
        :param event_b: event B
        :return: probability of event A given event B

        """
        # calculate P(A|B)
        p_a_given_b = self.probability_of_outcomes(self.sample_space, event_a,
                                                   keep_position=True)
        # calculate P(B)
        p_b = self.probability_of_outcomes(self.sample_space, event_b,
                                           keep_position=True)
        # calculate P(A)
        p_a = self.probability_of_outcomes(self.sample_space, event_a,
                                           keep_position=True)
        # calculate P(B|A)
        p_b_given_a = (p_a_given_b * p_b) / p_a
        return p_b_given_a

    @staticmethod
    def pbinom(q, size, prob, lower_tail=True, log_p=False):
        """
        Returns the binomial distribution
        :param q: the number of successes
        :param size: the number of trials
        :param prob: the probability of success
        :param lower_tail: whether to return the lower tail
        :param log_p: whether to return the log of the probability
        :return: the binomial distribution
        """
        # call the R binomial distribution using rpy2
        return ro.r['pbinom'](q, size, prob, lower_tail, log_p)

    @staticmethod
    def dbinom(q, size, prob, log=False):
        """
        Returns the binomial distribution
        :param q: the number of successes
        :param size: the number of trials
        :param prob: the probability of success
        :param log: whether to return the log of the probability
        :return: the binomial distribution
        """
        # call the R binomial distribution using rpy2
        return ro.r['dbinom'](q, size, prob, log)

    @staticmethod
    def pnorm(q, mean=0, sd=1, lower_tail=True, log_p=False):
        """
        Returns the normal distribution
        :param q: the number of successes
        :param mean: the mean of the normal distribution
        :param sd: the standard deviation of the normal distribution
        :param lower_tail: whether to return the lower tail
        :param log_p: whether to return the log of the probability
        :return: the normal distribution
        """
        # call the R normal distribution using rpy2
        return ro.r['pnorm'](q, mean, sd, lower_tail, log_p)

    @staticmethod
    def dnorm(q, mean=0, sd=1, log=False):
        """
        Returns the normal distribution
        :param q: the number of successes
        :param mean: the mean of the normal distribution
        :param sd: the standard deviation of the normal distribution
        :param log: whether to return the log of the probability
        :return: the normal distribution
        """
        # call the R normal distribution using rpy2
        return ro.r['dnorm'](q, mean, sd, log)

    @staticmethod
    def ppois(q, lambda_, lower_tail=True, log_p=False):
        """
        Returns the poisson distribution
        :param q: the number of successes
        :param lambda_: the number of trials
        :param lower_tail: whether to return the lower tail
        :param log_p: whether to return the log of the probability
        :return: the poisson distribution
        """
        # call the R poisson distribution using rpy2
        return ro.r['ppois'](q, lambda_, lower_tail, log_p)

    @staticmethod
    def dpois(q, lambda_, log=False):
        """
        Returns the poisson distribution
        :param q: the number of successes
        :param lambda_: the number of trials
        :param log: whether to return the log of the probability
        :return: the poisson distribution
        """
        # call the R poisson distribution using rpy2
        return ro.r['dpois'](q, lambda_, log)

    @staticmethod
    def pgeom(q, prob, lower_tail=True, log_p=False):
        """
        Returns the geometric distribution
        :param q: the number of successes
        :param prob: the probability of success
        :param lower_tail: whether to return the lower tail
        :param log_p: whether to return the log of the probability
        :return: the geometric distribution
        """
        # call the R geometric distribution using rpy2
        return ro.r['pgeom'](q, prob, lower_tail, log_p)

    @staticmethod
    def dgeom(q, prob, log=False):
        """
        Returns the geometric distribution
        :param q: the number of successes
        :param prob: the probability of success
        :param log: whether to return the log of the probability
        :return: the geometric distribution
        """
        # call the R geometric distribution using rpy2
        return ro.r['dgeom'](q, prob, log)

    @staticmethod
    def phyper(q, m, n, k, lower_tail=True, log_p=False):
        """
        Returns the hypergeometric distribution
        :param q: the number of successes
        :param m: the number of successes in the population
        :param n: the number of failures in the population
        :param k: the number of draws
        :param lower_tail: whether to return the lower tail
        :param log_p: whether to return the log of the probability
        :return: the hypergeometric distribution
        """
        # call the R hypergeometric distribution using rpy2
        return ro.r['phyper'](q, m, n, k, lower_tail, log_p)

    @staticmethod
    def dhyper(q, m, n, k, log=False):
        """
        Returns the hypergeometric distribution
        :param q: the number of successes
        :param m: the number of successes in the population
        :param n: the number of failures in the population
        :param k: the number of draws
        :param log: whether to return the log of the probability
        :return: the hypergeometric distribution
        """
        # call the R hypergeometric distribution using rpy2
        return ro.r['dhyper'](q, m, n, k, log)
