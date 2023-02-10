import itertools
import random

from src.statify import Statify


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
        combos = 1
        for value in values:
            combos *= self.data.count(value)
        return combos

    def nCp(self, n, p):
        """
        Calculates the number of combinations of n things taken p at a time
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of combinations
        """
        # calculate the number of combinations
        combos = self.factorial(n) / (
                self.factorial(p) * self.factorial(n - p))
        return combos

    def nCp_with_replacement(self, n, p):
        """
        Calculates the number of combinations of n things taken p at a time with replacement
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of combinations
        """
        # calculate the number of combinations
        combos = self.factorial(n + p - 1) / (
                self.factorial(p) * self.factorial(n - 1))
        return combos

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

    def nPr_with_replacement(self, n, p):
        """
        Calculates the number of permutations of n things taken p at a time with replacement
        :param n: the number of things
        :param p: the number of things taken at a time
        :return: the number of permutations
        """
        # calculate the number of permutations
        permutations = n ** p
        return permutations

    def nPn(self, n: list, p):
        """
        the number of ways of partitioning  n distinct objects into k distinct
        groups containing n_1, n_2, ..., n_k objects respectively, where each
        object appears in exactly one group. N = n! / (n_1! * n_2! * ... * n_k!)
        :param n:  the number of objects
        :param p:  the number of groups
        :return:  the number of ways of partitioning n objects into k groups
        """
        # calculate the number of ways of partitioning n objects into k groups
        denominator = 1
        for i in n:
            denominator *= self.factorial(i)
        permutations = self.factorial(sum(n)) / denominator
        return permutations

    # method to return the probability of a given value
    def probability(self, value, trials=1):
        """
        CaCalculates the probability a value or set of values will be picked  from
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

    def get_sample_space(self,
                         observations,
                         outcomes=None,
                         replacement=False,
                         duplicates=True,
                         display=True):
        """
        Calculates the sample space for a given number of observations and outcomes

        :param observations: the number of observations
        :param outcomes: list of possible outcomes
        :param replacement: whether the observations are taken with replacement
        :param duplicates: whether the observations can contain duplicates
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

        if display:
            # add a new line every 10 items
            for i in range(0, len(sample_space), 10):
                print(sample_space[i:i + 10])
            # print the total number of outcomes
            print(f'Cardinality of sample space S is : {len(sample_space)}')

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
                                    count += (1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1
                    else:
                        outcome_list = list(outcome)
                        # remove the ? from the list
                        for i in range(len(outcome_list)):
                            if outcome_list[i].find('?') > -1:
                                outcome_list[i] = outcome_list[i].replace('?', '')
                        for sample in sample_space:
                            if all([x in str(sample) for x in outcome_list if
                                    x != '?']):
                                if not replacement:
                                    # verify that sample is not already in already_found
                                    count += (1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1

                else:
                    for sample in sample_space:
                        if all([x in sample for x in outcome if x != '?']):
                            if not replacement:
                                count += (1 if sample not in already_found else 0)
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
                                    count += (1 if sample not in already_found else 0)
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
                                    count += (1 if sample not in already_found else 0)
                                    already_found.append(sample)
                                else:
                                    count += 1
                else:
                    for sample in sample_space:
                        if all([x in sample for x in outcome if x != '?']):
                            if not replacement:
                                # verify that sample is not already in already_found
                                count += (1 if sample not in already_found else 0)
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
                                display=True):
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
            probability = self.__probability_of_outcome(sample_space,
                                                        outcome,
                                                        keep_position,
                                                        replacement)

        if display:
            print(f'Probability of {outcome} is {probability}')
        return probability
