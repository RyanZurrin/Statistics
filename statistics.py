import matplotlib.pyplot as plt
import pandas as pd
import tabulate


class StatisticMethods(object):

    def __init__(self, data, population=False):
        # check if data is a list or table or path to csv file
        if isinstance(data, list):
            self.data = data
        elif isinstance(data, pd.DataFrame):
            self.data = data
        elif isinstance(data, str):
            self.data = pd.read_csv(data)
        elif isinstance(data, StatisticMethods):
            self.data = data.data
        else:
            raise TypeError('data must be a list, table or path to csv file')

        self.population = population

    def mean(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            # use the key to calculate mean of df
            return self.data[key].mean()
        return sum(self.data) / len(self.data)

    def median(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].median()
        sorted_data = sorted(self.data)
        size = len(self.data)
        if size % 2 == 0:
            return (sorted_data[size // 2] + sorted_data[size // 2 - 1]) / 2
        return sorted_data[size // 2]

    def mode(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].mode()
        return max(set(self.data), key=self.data.count)

    def midpoint(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return (self.data[key].max() + self.data[key].min()) / 2
        return (max(self.data) + min(self.data)) / 2

    def standard_deviation(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].std()
        mean = self.mean()
        # if population is True set n to 0 else set n to 1
        n = 0 if self.population else 1
        return ((sum((x - mean) ** 2 for x in self.data)) /
                (len(self.data) - n)) ** 0.5

    def variance(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].var()
        return self.standard_deviation() ** 2

    def z_score(self, x, key=False):
        if isinstance(self.data, pd.DataFrame):
            return (self.data[key] - self.data[key].mean()) / self.data[
                key].std()
        return (x - self.mean()) / self.standard_deviation()

    def covariance(self, other, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].cov(other.data[key])
        mean_x, mean_y = self.mean(), other.mean()
        return sum((x - mean_x) * (y - mean_y) for x, y in
                   zip(self.data, other.data)) / (len(self.data) - 1)

    def correlation_coefficient(self, other, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].corr(other.data[key])
        return self.covariance(other) / (
                self.standard_deviation() * other.standard_deviation())

    # calculate the quartiles
    def Q0(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(0)
        return min(self.data)

    def Q1(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(0.25)
        n = len(self.data)
        if n % 2 == 0:
            lower_half = self.data[:n // 2]
        else:
            lower_half = self.data[:n // 2 + 1]
        return StatisticMethods(lower_half).median()

    def Q2(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(0.5)
        n = len(self.data)
        sorted_data = sorted(self.data)
        if n % 2 == 0:
            return (sorted_data[n // 2] + sorted_data[n // 2 - 1]) / 2
        return sorted_data[n // 2]

    def Q3(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(0.75)
        n = len(self.data)
        if n % 2 == 0:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2
        return self.data[n // 2]

    def Q4(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(1)
        return max(self.data)

    def IQR(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile(0.75) - self.data[key].quantile(
                0.25)
        return self.Q3() - self.Q1()

    def quantile(self, key=False):
        if isinstance(self.data, pd.DataFrame):
            return self.data[key].quantile([0, 0.25, 0.5, 0.75, 1])
        return self.Q0(), self.Q1(), self.Q2(), self.Q3(), self.Q4()

    def display_data(self):
        if isinstance(self.data, pd.DataFrame):
            print(tabulate.tabulate(self.data, headers='keys',
                                    tablefmt='psql'))
        else:
            print(self.data)

    def __add__(self, other):
        if isinstance(other, StatisticMethods):
            return StatisticMethods(
                [x + y for x, y in zip(self.data, other.data)])
        return StatisticMethods(self.data + other.data)

    def __sub__(self, other):
        if isinstance(other, StatisticMethods):
            return StatisticMethods(
                [x - y for x, y in zip(self.data, other.data)])
        return StatisticMethods([x - y for x, y in zip(self.data, other.data)])

    def __mul__(self, other):
        if isinstance(other, StatisticMethods):
            return StatisticMethods(
                [x * y for x, y in zip(self.data, other.data)])
        return StatisticMethods([x * y for x, y in zip(self.data, other.data)])

    def __truediv__(self, other):
        if isinstance(other, StatisticMethods):
            return StatisticMethods(
                [x / y for x, y in zip(self.data, other.data)])
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
        if isinstance(self.data, pd.DataFrame):
            return self.data.iloc[index]
        return self.data[index]
