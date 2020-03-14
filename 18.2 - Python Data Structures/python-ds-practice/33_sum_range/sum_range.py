def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    total = 0

    if end is None:
        end = len(nums)

    # sum(iterable, start)
    # sum() Parameters
    # iterable - iterable (list, tuple, dict, etc).
    #   The items of the iterable should be numbers.
    # start (optional) - this value is added to the sum of items of the iterable.
    #   The default value of start is 0 (if omitted)

    total = sum(nums[start:end + 1])
    return total


nums = [1, 2, 3, 4]

print(sum_range(nums))
print(sum_range(nums, 1))
print(sum_range(nums, end=2))
print(sum_range(nums, 1, 3))
