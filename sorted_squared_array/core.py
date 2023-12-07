"""
Write a function that takes in a non-empty array of integers that are sorted int ascending order and returns a new array
of the same length with squares of the original integers also sorted in ascending order.
"""


def sorted_squared_array(array):
    """
    Complexity:

    Time: O(n)
    Space: O(n)
    """
    squared = []
    small_idx = 0
    big_idx = -1
    while len(squared) < len(array):
        smallest = array[small_idx]
        biggest = array[big_idx]
        if abs(biggest) > abs(smallest):
            value = biggest * biggest
            big_idx += -1
        else:
            value = smallest * smallest
            small_idx += 1

        squared.insert(0, value)

    return squared
