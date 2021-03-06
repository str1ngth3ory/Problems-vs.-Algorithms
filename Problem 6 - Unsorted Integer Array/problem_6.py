def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        raise ValueError('Input cannot be empty list.')

    min_int = ints[0]
    max_int = ints[0]

    for i in ints:
        if min_int > i:
            min_int = i
        if max_int < i:
            max_int = i

    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [1]  # Edge case 1 -  a list containing just one element
random.shuffle(l)
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

l = []
get_min_max(l)
# Edge case 2 - Raise value error, error message:'Input cannot be empty list.'
