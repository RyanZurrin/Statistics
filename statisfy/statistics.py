import random

import matplotlib.pyplot as plt
import pandas as pd
import tabulate


class Statify(object):

    def __init__(self, data=None,
                 population=False,
                 size=10000,
                 upper_limit=100,
                 lower_limit=0):
        """ Initialize the Statify object
        :param data:  data to be used for calculations
        :param population:  True if data is a population, False if data is a sample
        :param size:  size of the data to be generated
        :param upper_limit:  upper limit of the data to be generated
        :param lower_limit:  lower limit of the data to be generated
        """
        # check if data is a list or table or path to csv file
        if data is None:
            self.generate_data(size, upper_limit, lower_limit)
        elif isinstance(data, list):
            self._data = data
        elif isinstance(data, pd.DataFrame):
            self._data = data
        elif isinstance(data, str):
            self._data = pd.read_csv(data)
        elif isinstance(data, Statify):
            self._data = data._data
        else:
            raise TypeError('data must be a list, table or path to csv file')

        self.population = population

    def mean(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            # use the key to calculate mean of df
            return self._data[key].mean()
        return sum(self._data) / len(self._data)

    def median(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].median()
        sorted_data = sorted(self._data)
        size = len(self._data)
        if size % 2 == 0:
            return (sorted_data[size // 2] + sorted_data[size // 2 - 1]) / 2
        return sorted_data[size // 2]

    def mode(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].mode()
        return max(set(self._data), key=self._data.count)

    def midpoint(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return (self._data[key].max() + self._data[key].min()) / 2
        return (max(self._data) + min(self._data)) / 2

    def standard_deviation(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].std()
        mean = self.mean()
        # if population is True set n to 0 else set n to 1
        n = 0 if self.population else 1
        return ((sum((x - mean) ** 2 for x in self._data)) /
                (len(self._data) - n)) ** 0.5

    def variance(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].var()
        return self.standard_deviation() ** 2

    def z_score(self, x, key=False):
        if isinstance(self._data, pd.DataFrame):
            return (self._data[key] - self._data[key].mean()) / self._data[
                key].std()
        return (x - self.mean()) / self.standard_deviation()

    def covariance(self, other, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].cov(other.data[key])
        mean_x, mean_y = self.mean(), other.mean()
        return sum((x - mean_x) * (y - mean_y) for x, y in
                   zip(self._data, other.data)) / (len(self._data) - 1)

    def correlation_coefficient(self, other, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].corr(other.data[key])
        return self.covariance(other) / (
                self.standard_deviation() * other.standard_deviation())

    # calculate the quartiles
    def Q0(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(0)
        return min(self._data)

    def Q1(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(0.25)
        n = len(self._data)
        if n % 2 == 0:
            lower_half = self._data[:n // 2]
        else:
            lower_half = self._data[:n // 2 + 1]
        return Statify(lower_half).median()

    def Q2(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(0.5)
        n = len(self._data)
        sorted_data = sorted(self._data)
        if n % 2 == 0:
            return (sorted_data[n // 2] + sorted_data[n // 2 - 1]) / 2
        return sorted_data[n // 2]

    def Q3(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(0.75)
        n = len(self._data)
        if n % 2 == 0:
            return (self._data[n // 2 - 1] + self._data[n // 2]) / 2
        return self._data[n // 2]

    def Q4(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(1)
        return max(self._data)

    def IQR(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile(0.75) - self._data[key].quantile(
                0.25)
        return self.Q3() - self.Q1()

    def quantile(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].quantile([0, 0.25, 0.5, 0.75, 1])
        return self.Q0(), self.Q1(), self.Q2(), self.Q3(), self.Q4()

    def display_data(self):
        if isinstance(self._data, pd.DataFrame):
            print(tabulate.tabulate(self._data, headers='keys',
                                    tablefmt='psql'))
        else:
            print(self._data)

    def generate_data(self, size, upper_limit, lower_limit):
        # generate random data
        self._data = [random.randint(lower_limit, upper_limit) for _ in
                      range(size)]

    def histogram(self, key=False, bins=10, display=True):
        if isinstance(self._data, pd.DataFrame):
            hist = self._data[key].hist(bins=bins)
        else:
            hist = plt.hist(self._data, bins=bins)
        if display:
            plt.show()
        return hist

    def box_plot(self, key=False, display=True):
        if isinstance(self._data, pd.DataFrame):
            box = self._data[key].plot.box()
        else:
            box = plt.boxplot(self._data)
        if display:
            plt.show()
        return box

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __add__(self, other):
        if isinstance(other, Statify):
            return Statify(
                [x + y for x, y in zip(self._data, other._data)])
        return Statify(self._data + other.data)

    def __sub__(self, other):
        if isinstance(other, Statify):
            return Statify(
                [x - y for x, y in zip(self._data, other._data)])
        return Statify([x - y for x, y in zip(self._data, other.data)])

    def __mul__(self, other):
        if isinstance(other, Statify):
            return Statify(
                [x * y for x, y in zip(self._data, other._data)])
        return Statify([x * y for x, y in zip(self._data, other.data)])

    def __truediv__(self, other):
        if isinstance(other, Statify):
            return Statify(
                [x / y for x, y in zip(self._data, other.data)])
        return Statify([x / y for x, y in zip(self._data, other.data)])

    def __repr__(self):
        return "StatisticMethods({})".format(self._data)

    def __str__(self):
        return "StatisticMethods({})".format(self._data)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index):
        if isinstance(self._data, pd.DataFrame):
            return self._data.iloc[index]
        return self._data[index]
