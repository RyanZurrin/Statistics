import itertools
from pprint import pprint


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


def is_word(word, words):
    """
    Check if word is in dictionary
    :param word: word to check
    :param words: dictionary of words
    :return: True if word is in dictionary
    """
    return word in words


def make_words_from_string(string, display=False):
    """
    Make a list of all permutations of a string of characters and then check if
    each permutation is a word in the dictionary of words and return the list of
    words that are in the dictionary
    :param string: string of characters
    :return: list of words that are in the dictionary

    """
    words = load_words_from_file('words.txt')
    permutations = []
    # make all possible permutations of the string of characters using itertools
    for i in range(1, len(string) + 1):
        permutations.extend(list(itertools.permutations(string, i)))
    # convert the list of tuples to a list of strings
    permutations = [''.join(permutation) for permutation in permutations]
    words = [
        permutation for permutation in permutations if is_word(
            permutation, words)
    ]

    # now remove duplicates and sort alphabetically
    words = sorted(list(set(words)))

    if display:
        # print the list of words so that there is a new line every 15 words
        for i in range(0, len(words), 15):
            print(words[i:i + 15])
        print("Total permutations: {}".format(len(permutations)))
        print("Total words: {}".format(len(words)))
    # check if each permutation is a word in the dictionary of words


# test the mwke_words_from_string function

string = 'ryanzurrin'
make_words_from_string(string, display=True)
