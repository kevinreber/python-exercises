def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowels = 'aeiou'
    vowel_count = {}

    for vowel in vowels:
        # .count() will count how many times vowel passed in occurs in phrase
        count = phrase.count(vowel)
        if count > 0:
            vowel_count[vowel] = count

    return vowel_count

    # phrase = phrase.lower()
    # counter = {}

    # for ltr in phrase:
    #     if ltr in VOWELS:
    #         counter[ltr] = counter.get(ltr, 0) + 1

    # return counter


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
