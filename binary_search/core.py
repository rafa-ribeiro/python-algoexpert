"""

Complexity:

Time: O(log n)
Space: O(1)

"""


def binary_search(array, target):
    size = len(array)
    start = 0
    end = size - 1

    while start <= end:
        m = (start + end) // 2

        if target == array[m]:
            return m

        if target > array[m]:
            start = m + 1
        else:
            end = m - 1

    return -1
