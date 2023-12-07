from typing import List, Optional


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _increment_branch_sum(sums: List[int], total: int, node: Optional[BinaryTree] = None):
    if node:
        inc_total = total + node.value
        is_leaf = node.left is None and node.right is None
        if is_leaf:
            sums.append(inc_total)
        else:
            _increment_branch_sum(node=node.left, sums=sums, total=inc_total)
            _increment_branch_sum(node=node.right, sums=sums, total=inc_total)


def branch_sums(root: Optional[BinaryTree] = None):
    """

    Complexity:

    Time: O(n)
    Space: O(n)

    """
    sums = list()
    _increment_branch_sum(node=root, sums=sums, total=0)
    return sums
