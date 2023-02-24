import random
from pprint import pprint


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

    def __repr__(self):
        return f'TrieNode({self.children}, {self.is_end_of_word})'

    def __str__(self):
        return f'TrieNode({self.children}, {self.is_end_of_word})'

    def __eq__(self, other):
        return self.children == other.children and self.is_end_of_word == other.is_end_of_word

    def __ne__(self, other):
        return self.children != other.children or self.is_end_of_word != other.is_end_of_word

    def __hash__(self):
        return hash((self.children, self.is_end_of_word))

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, key):
        return self.children[key]

    def __setitem__(self, key, value):
        self.children[key] = value

    def __delitem__(self, key):
        del self.children[key]

    def __len__(self):
        return len(self.children)

    def __contains__(self, item):
        return item in self.children

    def __reversed__(self):
        return reversed(self.children)

    def __lt__(self, other):
        return self.children < other.children

    def __le__(self, other):
        return self.children <= other.children

    def __gt__(self, other):
        return self.children > other.children

    def __ge__(self, other):
        return self.children >= other.children


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def __len__(self):
        return self._count_words(self.root)

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
        p_crawl.is_end_of_word = True

    def search(self, key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]
        return p_crawl is not None and p_crawl.is_end_of_word

    def starts_with(self, prefix, display=False):
        """
        :returns a list of words that start with the prefix
        :param prefix:
        :param display: if True, print the words that start with the prefix
        :return:
        """
        p_crawl = self.root
        length = len(prefix)
        for level in range(length):
            index = self._char_to_index(prefix[level])
            if not p_crawl.children[index]:
                return []
            p_crawl = p_crawl.children[index]

        if display:
            # print the words that start with the prefix
            self._print_trie(p_crawl, prefix)

        return self._get_words(p_crawl, prefix)

    def _count_words(self, node):
        count = 0
        if node.is_end_of_word:
            count += 1
        for child in node.children:
            if child:
                count += self._count_words(child)
        return count

    def print_trie(self):
        self._print_trie(self.root, '')

    def _print_trie(self, node, word):
        if node.is_end_of_word:
            print(word)
        for i, child in enumerate(node.children):
            if child:
                self._print_trie(child, word + chr(i + ord('a')))

    def _get_words(self, p_crawl, prefix):
        words = []
        if p_crawl.is_end_of_word:
            words.append(prefix)
        for i, child in enumerate(p_crawl.children):
            if child:
                words += self._get_words(child, prefix + chr(i + ord('a')))
        return words

    def words(self):
        return self._get_words(self.root, '')



class TrieWordFinder(Trie):
    def __init__(self, string, display=True, dict_path='words.txt'):
        super().__init__()
        self._string = string
        self._display = display
        self._dict_path = dict_path
        self._store_words()

    def _store_words(self):
        # add words to the trie as ther are read from the file
        with open(self._dict_path) as f:
            for word in f:
                # if word has ' or - in it, remove it before inserting
                if "'" in word or '-' in word or ' ' in word or '.' in word:
                    word = word.replace("'", '')
                    word = word.replace('-', '')
                    word = word.replace(' ', '')
                    word = word.replace('.', '')
                self.insert(word.strip())



if __name__ == '__main__':
    # trie = Trie()
    # words = open('words.txt', 'r').read().splitlines()
    # # add 500 random words to the trie with a upper limit if index 194000
    # for word in random.sample(words, 500):
    #     trie.insert(word)
    # # print the trie
    # trie.print_trie()
    # #
    # # print the number of words that start with 'cat'
    # print("Number of words that start with 'tra':", len(trie.starts_with('st')))
    # print(trie.starts_with('st'))

    # test the trie word finder
    trie_word_finder = TrieWordFinder('ryanzurrin')
    stl = trie_word_finder.starts_with('st')
    print(len(stl))
    print(stl)
    print(len(trie_word_finder))
