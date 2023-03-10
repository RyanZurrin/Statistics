import pprint
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
        elif isinstance(data, dict):
            self._data = data
        elif isinstance(data, tuple):
            self._data = data
        elif isinstance(data, set):
            self._data = data
        else:
            raise TypeError('Invalid data type')

        self.population = population

    def mean(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            # use the key to calculate mean of df
            return self._data[key].mean()
        elif isinstance(self._data, dict):
            # return the mean of the values in the dict
            return sum(self._data.values()) / len(self._data)
        elif isinstance(self._data, tuple):
            # return the mean of the values in the tuple
            return sum(self._data) / len(self._data)
        # if it is a list of tuples
        elif isinstance(self._data, list) and isinstance(self._data[0], tuple):
            # iterate through the list of tuples and sum the values
            total = 0
            for t in self._data:
                total += sum(t)
            # return the mean of the values in the list of tuples
            return total / len(self._data)
        # if it is a list of lists
        elif isinstance(self._data, list) and isinstance(self._data[0], list):
            # iterate through the list of lists and sum the values
            total = 0
            for l in self._data:
                total += sum(l)
            # return the mean of the values in the list of lists
            return total / len(self._data)
        # if it is a list of dicts
        elif isinstance(self._data, list) and isinstance(self._data[0], dict):
            # iterate through the list of dicts and sum the values
            total = 0
            for d in self._data:
                total += sum(d.values())
            # return the mean of the values in the list of dicts
            return total / len(self._data)
        # if it is a list of sets
        elif isinstance(self._data, list) and isinstance(self._data[0], set):
            # iterate through the list of sets and sum the values
            total = 0
            for s in self._data:
                total += sum(s)
            # return the mean of the values in the list of sets
            return total / len(self._data)
        else:
            return sum(self._data) / len(self._data)

    def trimmed_mean(self, key=False, percent=0.1):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].mean()
        sorted_data = sorted(self._data)
        size = len(self._data)
        trimmed = int(size * percent)
        return sum(sorted_data[trimmed:-trimmed]) / (size - 2 * trimmed)

    def weighted_mean(self, key=False, weights=[]):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].mean()
        return sum([x * y for x, y in zip(self._data, weights)]) / sum(weights)

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

    def sum_of_squares(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].sum() ** 2
        return sum(x ** 2 for x in self._data)

    def display_data(self):
        if isinstance(self._data, pd.DataFrame):
            print(tabulate.tabulate(self._data, headers='keys',
                                    tablefmt='psql'))
        else:
            print(tabulate.tabulate(self._data, tablefmt='psql'))

    def summary(self):
        # print the summary of the data, if df then each column has a summary
        if isinstance(self._data, pd.DataFrame):
            print(self._data.describe())
        else:
            print('Min: ', min(self._data))
            print('Q1: ', self.Q1())
            print('Median: ', self.median())
            print('Mean: ', self.mean())
            print('Midpoint: ', self.midpoint())
            print('Q3: ', self.Q3())
            print('Max: ', max(self._data))

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

    def scatter_plot(self, other, key=False, display=True):
        if isinstance(self._data, pd.DataFrame):
            scatter = self._data.plot.scatter(x=key, y=other.data[key])
        else:
            scatter = plt.scatter(self._data, other.data)
        if display:
            plt.show()
        return scatter

    def line_plot(self, key=False, display=True):
        if isinstance(self._data, pd.DataFrame):
            line = self._data[key].plot.line()
        else:
            line = plt.plot(self._data)
        if display:
            plt.show()
        return line

    def bar_plot(self, key=False, display=True):
        if isinstance(self._data, pd.DataFrame):
            bar = self._data[key].plot.bar()
        else:
            bar = plt.bar(self._data)
        if display:
            plt.show()
        return bar

    def pie_plot(self, key=False, display=True):
        if isinstance(self._data, pd.DataFrame):
            pie = self._data[key].plot.pie()
        else:
            pie = plt.pie(self._data)
        if display:
            plt.show()
        return pie

    def frequency_table(self, key=False):
        if isinstance(self._data, pd.DataFrame):
            return self._data[key].value_counts()
        return pd.Series(self._data).value_counts()

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
