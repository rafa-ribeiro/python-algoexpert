"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of
the first onde.
"""


def is_valid_subsequence(array, sequence):
    """
    Complexity:

    Time: O(n)
    Space: O(1)
    """
    ai = 0
    si = 0

    while si < len(sequence) and ai < len(array):
        if array[ai] == sequence[si]:
            si += 1
        ai += 1

    return si == len(sequence)


def is_valid_subsequence_2(array, sequence):
    si = 0

    for item in array:
        if si == len(sequence):
            break
        if item == sequence[si]:
            si += 1

    return si == len(sequence)
