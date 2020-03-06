def print_upper_words(words):
    """
    Prints all words in list in upper case
    """

    for word in words:
        print(word.upper())


print(print_upper_words(['hello', 'hey', 'bye']))


def print_upper_words2(words):
    """
    Prints words that only start with the letter 'e' and 'E'
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


print(print_upper_words2(['ello', 'hey', 'Ever', 'eyes']))


def print_upper_words3(words, first_letters):
    """
    Prints words that start with any letter in list of first_letters
    """

    for word in words:
        for letter in first_letters:
            if word.startswith(letter):
                print(word.upper())


print(print_upper_words3(['ello', 'hey', 'Ever', 'Yoyo', 'yikes'], ["E", "Y"]))
