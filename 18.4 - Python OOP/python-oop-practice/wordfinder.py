"""Word Finder: finds random words from a dictionary."""

"""
Some notes:

1. You’ll need to learn how to read files in Python — you can look at the documentation at http://python.org as a good place to start
2. When Python reads files line-by-line, it still keeps the “newline” character at the end of each line. Make sure you take that off so that when you find a random word, you return it as “cat”, not “cat\n”
3. You can make a list of words yourself, or use the words.txt file in the starter code — if you’re not on Windows, your computer already has a giant list of English words! On OSX, this is at /usr/share/dict/words"""




import random
class WordFinder:
    """
    Finds random words from dictionary

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    """

    def __init__(self, src):
        self.src = src
        self.words = self.list_of_words()
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder src={self.src} words_read={len(self.words)} word_list={self.words}>"

    def list_of_words(self):
        """Returns words in self.src into a list with no white space"""
        file = open(self.src)
        words = [word.strip() for word in file]
        return words

    def random(self):
        """Returns random word from self.words"""
        return random.choice(self.words)


"""Subclass of WordFinder"""


class SpecialWordFinder(WordFinder):
    """
    Special Word Finder that removes blank lines and comment lines with '#'

    >>> swf = SpecialWordFinder("complex.txt")
    9 words read

    >>> swf.parse_list()
    4 words read
    ['kale', 'parsnips', 'apple', 'mango']

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    """

    def __init__(self, words):
        """Get list of words from parent class"""
        super().__init__(words)

    # def __repr__(self):
    #     return f"<SpecialWordFinder original_list={self.words} new_list={self.new_list}>"

    def parse_list(self):
        """Removes blank lines and comment lines with '#'"""

        self.words = [
            word.strip() for word in self.words if word.strip() and not word.startswith('#')]

        print(f"{len(self.words)} words read")
        return self.words
