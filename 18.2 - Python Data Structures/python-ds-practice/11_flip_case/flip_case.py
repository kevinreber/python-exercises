def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()
    output = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()    # swapcase() changes case of element
        output += ltr

    return output

    # Alternate phrasing: a bit clever, same runtime, and harder to
    # read:

    # to_swap = to_swap.lower()
    #
    # fixed = [
    #     (char.swapcase() if char.lower() == to_swap else char)
    #     for char in phrase
    # ]
    #
    # return "".join(fixed)


print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
