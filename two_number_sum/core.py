"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any
two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
If no two numbers sum up to the target sum, the function should return an empty array.
"""


def two_number_sum(array, target_sum):
    """
    Complexity:

    Time: O(n)
    Space: O(n)
    """
    pairs = {}

    for num in array:
        diff = target_sum - num

        if diff not in pairs:
            pairs[diff] = num
            pairs[num] = diff
        else:
            return [diff, pairs[diff]]

    return []
