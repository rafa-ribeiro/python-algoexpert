from typing import Sequence

from binary_search.core import binary_search


def parse_list(_items: str, _separator) -> Sequence:
    return _items.strip().rsplit(_separator)


if __name__ == "__main__":
    separator = input("Enter the list's separator (default is blank space): ") or " "
    items = input("Enter an ordered list [int, string] separated by black space: ")
    array = parse_list(items, separator)
    target = input("Enter the item to search for: ")

    print(f"List: {array}")
    print(f"Search for item = {target}")

    target_idx = binary_search(array=array, target=target)
    message = f"Target found on index = {target_idx}" if target_idx >= 0 else "Target not found"
    print(message)
