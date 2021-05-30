"""Length of Longest Substring."""


def length_of_longest_substring(s: str) -> int:
    """Length of longest substring.

    Runtime: 40 ms, faster than 87.53% of Python online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 13.5 MB, less than 85.81% of Python online submissions for Longest Substring Without Repeating Characters.
    """

    length = 0

    # start at -1 to account for zero index on i
    last_match = -1

    chars = {}

    for i, char in enumerate(s):
        try:
            if last_match < chars[char]:
                last_match = chars[char]
        except KeyError:
            pass
        chars[char] = i
        length = max(i - last_match, length)
    return length
