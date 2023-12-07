"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any
two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
If no two numbers sum up to the target sum, the function should return an empty array.
"""


def two_number_sum_1(array, target_sum):
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


def two_number_sum_2(array, target_sum):
    nums = set(array)

    for num in array:
        diff = target_sum - num
        if diff in nums and diff is not num:
            return [diff, num]

    return []


def two_number_sum_3(array, target_sum):
    array.sort()
    sorted_arr = array

    left = 0
    right = len(array) - 1

    while left < right:
        l = sorted_arr[left]
        r = sorted_arr[right]
        target = l + r
        if target == target_sum:
            return [l, r]
        elif target < target_sum:
            left += 1
        else:
            right += -1

    return []
