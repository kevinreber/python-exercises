def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    output = [item for item in lst if item]  # if item exists, add to new array

    return output


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
