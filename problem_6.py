def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1:
        return (None, None)
    min = ints[0]
    max = ints[0]
    for elem in ints:
        if elem < min:
            min = elem
        elif elem > max:
            max = elem
    return (min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 500)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 499) == get_min_max(l)) else "Fail")