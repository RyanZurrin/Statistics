import itertools
import math
import time
import argparse
import tqdm

WORDS_PATH = 'words.txt'
# use argspars to take in the string and path to dictionary of words
parser = argparse.ArgumentParser()
parser.add_argument('string', help='string of characters')
# path to dictionary of words uses default words.txt
parser.add_argument('-p', '--path', help='path to dictionary of words',
                    default=WORDS_PATH)
args = parser.parse_args()


class WordFinder:

    def __init__(self, target_word, dict_path="words.txt"):
        self.target_word = target_word
        self.dict_path = dict_path
        self.words_dict = self.load_words_from_file(dict_path)
        self.counter = self.total_arrangements(len(target_word))
        self.words = self.make_words_from_string(target_word, display=False)

    @staticmethod
    def load_words_from_file(file_path):
        """
        Load words from file into a dictionary for O(1) lookup
        : make all the letters in each word lowercase
        :param file_path: path to file
        :return: list of words
        """
        words = {}
        with open(file_path, 'r') as file:
            for line in file:
                words[line.strip().lower()] = True
        return words

    @staticmethod
    def is_word(word, words):
        """
        Check if word is in dictionary
        :param word: word to check
        :param words: dictionary of words
        :return: True if word is in dictionary
        """
        return word in words

    @staticmethod
    def nPr(n, r):
        """
        Calculate the number of permutations of n objects taken r at a time
        :param n: number of objects
        :param r: number of objects taken at a time
        :return: number of permutations
        """
        return int(math.factorial(n) / math.factorial(n - r))

    @staticmethod
    def total_arrangements(n):
        """
        Calculate the total number of arrangements of n objects so if a string has
        6 letters then the total would be:
        nP1 + nP2 + nP3 + nP4 + nP5 + nP6
        :param n: number of objects
        :return: total number of arrangements
        """
        total = 0
        for i in range(1, n + 1):
            total += WordFinder.nPr(n, i)
        return total

    @staticmethod
    def make_words_from_string(string, display=False):
        """
        Make a list of all permutations of a string of characters and then check if
        each permutation is a word in the dictionary of words and return the list of
        words that are in the dictionary
        :param string: string of characters
        :return: list of words that are in the dictionary

        """
        t0 = time.perf_counter()
        # remove all non-alphabetic characters and make all the letters lowercase
        string = ''.join([char for char in string if char.isalpha()]).lower()

        # print the number of arrangements that will be checked
        counter = WordFinder.total_arrangements(len(string))
        if display:
            print(f'Checking {counter} arrangements')

        # load the dictionary of words
        words_dict = WordFinder.load_words_from_file('words.txt')

        # add the permutations that are words to a list while generating them and
        # use a progress bar to show the progress
        words = []
        for i in range(1, len(string) + 1):
            for perm in tqdm.tqdm(itertools.permutations(string, i),
                                  total=WordFinder.nPr(len(string), i)):
                word = ''.join(perm)
                if WordFinder.is_word(word, words_dict):
                    words.append(word)

        words = sorted(list(set(words)))

        if display:
            # print the list of words so that there is a new line every 15 words
            for i in range(0, len(words), 15):
                print(words[i:i + 15])
            print("Total permutations checked: {}".format(counter))
            print("Total words found: {}".format(len(words)))

        t1 = time.perf_counter()
        print("Time taken: {}".format(t1 - t0))

        return words

    def get_words(self):
        return self.words


if __name__ == '__main__':
    word_finder = WordFinder(args.string, args.path)
    print(word_finder.get_words())
