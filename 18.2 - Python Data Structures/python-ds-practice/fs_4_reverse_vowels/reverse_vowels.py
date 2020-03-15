def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    # vowels = set('aeiou')
    # s = list(s)
    # vowels_found = []
    # result = []

    # for letter in s:
    #     if letter.lower() in vowels:
    #         vowels_found.append(letter)
    #         result.append(' ')
    #     else:
    #         result.append(letter)

    # # Reverse vowels
    # vowels_reverse = vowels_found[::-1]

    # index = 0

    # for letter in result:
    #     print(letter)
    #     if letter == ' ':
    #         print(vowels_reverse[index])
    #         letter = vowels_reverse[index]
    #     # index += 1

    # print(result)

    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)


print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))
