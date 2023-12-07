"""
Write a function that takes in a list of unique strings and returns a list of semordnilap (palindrome) pairs.
"""


def semordnilap(words):
    """
    Complexity:

    - Time: O(n * m) -> N número de elementos em words | M tamanho da maior string dentro de words
    - Space: O(n * m)

    """
    reverses = set([w for w in words])
    palindromes = []

    for word in words:
        rev = reverse(word)
        if rev in reverses and rev != word:
            palindromes.append([word, rev])
            reverses.remove(word)
            reverses.remove(rev)

    return palindromes


def reverse(word):
    rev = word[::-1]  # a good way to reverse a string in Python
    return rev
