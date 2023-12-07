def non_constructible_change(coins):
    """
    Complexity:

    Time: O(n)
    Space: O(1) because the sort is made in place
    """
    if not coins:
        return 1

    coins.sort()
    current_possible_change = 0
    for coin in coins:
        if coin > (current_possible_change + 1):
            return current_possible_change + 1
        current_possible_change += coin

    return current_possible_change + 1
