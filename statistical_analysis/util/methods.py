import itertools
import time
from pprint import pprint
import progressbar
import resource

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
    t0 = time.perf_counter()

    # add progress bar to show how many permutations have been checked
    progress = progressbar.ProgressBar()
    widgets = [
        ' [', progressbar.Timer(), '] ',
        progressbar.Bar(),
        ' (', progressbar.ETA(), ') ',
        ]


    # remove any spaces and make all the letters lowercase inplace
    string = string.replace(' ', '').lower()

    words_dict = load_words_from_file('words.txt')
    # check the permutations while they are being generated and if they are a
    # word in the dictionary then add them to the list of words if not then
    # discard them so that larger names can be processed

    # make all possible permutations of the string of characters using itertools and use a progress bar to show how many permutations have been checked
    words = [
        ''.join(permutation) for i in progress(range(1, len(string) + 1))
        for permutation in itertools.permutations(string, i)
        if ''.join(permutation) in words_dict
    ]



    # words = [
    #     ''.join(permutation) for i in range(1, len(string) + 1)
    #     for permutation in itertools.permutations(string, i)
    #     if ''.join(permutation) in words_dict
    # ]

    # now remove duplicates and sort alphabetically
    words = sorted(list(set(words)))

    if display:
        # print the list of words so that there is a new line every 15 words
        for i in range(0, len(words), 15):
            print(words[i:i + 15])
        print("Total permutations: {}".format(len(words)))
        print("Total words: {}".format(len(words)))

    t1 = time.perf_counter()
    print("Time taken: {}".format(t1 - t0))
    memMB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    print("Memory used: {} MB".format(memMB))

    return words


string = 'David Giblin Jr'

make_words_from_string(string, display=True)
