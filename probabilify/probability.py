from statistics import *

from statisfy import Statify


# class to turn data into a probability object, given a data set
# this class will let us ask questions about the data to help
# us understand how probable certaoin events are
class Probabilify(Statify):

    def __init__(self, data):
        super().__init__(data)
        self.__data = data

    # method to return the probability of an event
    def probability(self, event):
        # get the number of times the event occurs
        occurrences = self.__data.count(event)
        # get the total number of events
        total = len(self.__data)
        # return the probability
        return occurrences / total

    # method to return the probability of an event given another event
    def conditional_probability(self, event, given):
        # get the number of times the event occurs
        occurrences = self.__data.count(event)
        # get the number of times the given event occurs
        given_occurrences = self.__data.count(given)
        # return the probability
        return occurrences / given_occurrences
