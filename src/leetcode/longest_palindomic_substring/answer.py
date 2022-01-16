"""Longest Palindromic Substring."""


def longest_palindromic_substring(s: str) -> str:
    """Get the longest palindromic substring.

    Runtime: 120 ms, faster than 97.84% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 14.3 MB, less than 81.11% of Python3 online submissions for Longest Palindromic Substring.

    """

    def is_palindrome(_str: str) -> bool:
        return _str == _str[::-1]

    if is_palindrome(s):
        return s

    window_len = 1
    palindrome_start = 0

    for i in range(1, len(s)):
        window_size = i - window_len
        window_stop = i + 1

        if window_size >= 0 and is_palindrome(s[window_size:window_stop]):
            palindrome_start = window_size
            window_len += 1

        elif window_size >= 1 and is_palindrome(s[window_size - 1 : window_stop]):
            palindrome_start = window_size - 1
            window_len += 2

    return s[palindrome_start : palindrome_start + window_len]


if __name__ == "__main__":
    longest_palindromic_substring("abb")
