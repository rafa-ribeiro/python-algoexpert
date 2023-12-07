from typing import Sequence

from binary_search.core import binary_search


def parse_list(_items: str) -> Sequence:
    return _items.strip().split(" ")


if __name__ == "__main__":
    items = input("Enter an ordered list [int, string] separated by black space:")
    array = parse_list(items)
    target = input("Enter the item to search for:")

    print(f"List: {array}")
    print(f"Search for item = {target}")

    target_idx = binary_search(array=array, target=target)
    message = f"Target found on index = {target_idx}" if target_idx > 0 else "Target not found"
    print(message)
