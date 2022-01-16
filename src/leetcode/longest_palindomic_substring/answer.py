"""Longest Palindromic Substring."""


def longest_palindromic_substring(s: str) -> str:
    """Get the longest palindromic substring.

    Runtime: 8392 ms, faster than 7.41% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 82.6 MB, less than 5.32% of Python3 online submissions for Longest Palindromic Substring.

    lol heckaslow
    """

    def is_palindrome(_str: str) -> bool:
        return _str == _str[::-1]

    # maybe the whole thing is a palindrome
    if is_palindrome(s):
        return s

    substrings: dict[len, list[str]] = {}
    for i in range(1 + len(s)):
        for j in range(i, 1 + len(s)):
            substring = s[i:j]
            if substring and is_palindrome(substring):
                substrings.setdefault(len(substring), []).append(substring)

    max_len = max(substrings)
    return substrings[max_len][0]


if __name__ == "__main__":
    longest_palindromic_substring("abb")
