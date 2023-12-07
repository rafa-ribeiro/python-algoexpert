def generate_document(characters, document):
    """
    Complexity:

    - Time: O(n+m)
    - Space: O(c)

    Where:
    - n is the number of characters
    - m is the number of letters in document
    - c is the number of unique characters in the characters string
    """

    if not document:
        return True

    char_freq = dict()
    for ch in characters:
        freq = char_freq.get(ch, 0)
        char_freq[ch] = freq + 1

    for letter in document:
        amount = char_freq.get(letter, 0)
        if amount == 0:
            return False

        char_freq[letter] = amount - 1

    return True
