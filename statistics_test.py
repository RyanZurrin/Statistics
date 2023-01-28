import unittest
from statistics import StatisticMethods

# create an artificial dataset to test the statistics methods
data = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28,
        9766.09, 10305.32, 14379.96, 10713.97, 15433.50, 8611.41]
data2 = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73,
         5821.12, 6976.93, 16618.61, 10054.37, 3803.96, 10713.97]
# create a StatisticMethods object
stat = StatisticMethods(data)
other = StatisticMethods(data2)


# test the mean method
class TestMean(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(stat.mean(), 10526.03)


# test the median method
class TestMedian(unittest.TestCase):
    def test_median(self):
        self.assertEqual(stat.median(), 9766.09)


# test the mode method
class TestMode(unittest.TestCase):
    def test_mode(self):
        self.assertEqual(stat.mode(), 8611.41)


# test the standard deviation
class TestStandardDeviation(unittest.TestCase):
    def test_stddev(self):
        self.assertEqual(stat.standard_deviation(), 2685.7000592924246)


# test the quantiles
class TestQuantiles(unittest.TestCase):
    def test_Q0(self):
        self.assertEqual(stat.Q0(), 7606.46)

    def test_Q1(self):
        self.assertEqual(stat.Q1(), 8611.41)

    def test_Q2(self):
        self.assertEqual(stat.Q2(), 9766.09)

    def test_Q3(self):
        self.assertEqual(stat.Q3(), 11496.28)

    def test_Q4(self):
        self.assertEqual(stat.Q4(), 15433.50)


# test the covariance
class TestCovariance(unittest.TestCase):
    def test_covariance(self):
        self.assertEqual(stat.covariance(StatisticMethods(other)),
                         2513900.4030499994)

# test the correlation coefficient
class TestCorrelationCoefficient(unittest.TestCase):
    def test_correlation_coefficient(self):
        self.assertEqual(stat.correlation_coefficient(StatisticMethods(other)),
                         0.20999083362665777)

# test the z score
class TestZScore(unittest.TestCase):
    def test_z_score(self):
        self.assertEqual(stat.z_score(8000.0), -0.9405480672571863)


if __name__ == '__main__':
    unittest.main()
