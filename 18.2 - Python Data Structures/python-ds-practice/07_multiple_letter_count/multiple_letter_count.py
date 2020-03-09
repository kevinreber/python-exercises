def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    counter = {}
    for letter in phrase:
        # dictionary.get('key_to_look_for', default value)
        counter[letter] = counter.get(letter, 0) + 1
    return counter


print(multiple_letter_count('Yay'))
print(multiple_letter_count('yay'))
