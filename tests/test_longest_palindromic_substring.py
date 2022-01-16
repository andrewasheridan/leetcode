from leetcode.longest_palindomic_substring.answer import longest_palindromic_substring


def test_longest_palindromic_substring():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("babad") in ("bab", "aba")
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("abb") == "bb"
