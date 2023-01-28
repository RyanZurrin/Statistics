import matplotlib.pyplot as plt
import pandas as pd


class StatisticMethods(object):

    def __init__(self, data, population=False):
        self.data = data
        self.population = population

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        size = len(self.data)
        if size % 2 == 0:
            return (sorted_data[size // 2] + sorted_data[size // 2 - 1]) / 2
        return sorted_data[size // 2]

    def mode(self):
        return max(set(self.data), key=self.data.count)

    def standard_deviation(self):
        mean = self.mean()
        # if population is True set n to 0 else set n to 1
        n = 0 if self.population else 1
        return ((sum((x - mean) ** 2 for x in self.data)) /
                (len(self.data) - n)) ** 0.5

    def variance(self):
        return self.standard_deviation() ** 2

    def z_score(self, x):
        return (x - self.mean()) / self.standard_deviation()

    def covariance(self, other):
        mean_x, mean_y = self.mean(), other.mean()
        return sum((x - mean_x) * (y - mean_y) for x, y in zip(self.data, other.data)) / (len(self.data)-1)

    def correlation_coefficient(self, other):
        return self.covariance(other) / (self.standard_deviation() * other.standard_deviation())

    # calculate the quartiles
    def Q0(self):
        return min(self.data)

    def Q1(self):
        n = len(self.data)
        if n % 2 == 0:
            lower_half = self.data[:n // 2]
        else:
            lower_half = self.data[:n // 2 + 1]
        return StatisticMethods(lower_half).median()

    def Q2(self):
        n = len(self.data)
        sorted_data = sorted(self.data)
        if n % 2 == 0:
            return (sorted_data[n // 2] + sorted_data[n // 2 - 1]) / 2
        return sorted_data[n // 2]

    def Q3(self):
        n = len(self.data)
        if n % 2 == 0:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2
        return self.data[n // 2]

    def Q4(self):
        return max(self.data)

    def IQR(self):
        return self.Q3() - self.Q1()

    def quantile(self):
        return self.Q0(), self.Q1(), self.Q2(), self.Q3(), self.Q4()

    def __add__(self, other):
        return StatisticMethods(self.data + other.data)

    def __sub__(self, other):
        return StatisticMethods([x - y for x, y in zip(self.data, other.data)])

    def __mul__(self, other):
        return StatisticMethods([x * y for x, y in zip(self.data, other.data)])

    def __truediv__(self, other):
        return StatisticMethods([x / y for x, y in zip(self.data, other.data)])

    def __repr__(self):
        return "StatisticMethods({})".format(self.data)

    def __str__(self):
        return "StatisticMethods({})".format(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

