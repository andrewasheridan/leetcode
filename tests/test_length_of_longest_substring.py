import pytest

from leetcode.length_of_longest_substring.answer import length_of_longest_substring

examples = [
    {
        "input": {
            "s": "abcabcbb",
        },
        "output": 3,
    },
    {
        "input": {
            "s": "bbbbb",
        },
        "output": 1,
    },
    {
        "input": {
            "s": "pwwkew",
        },
        "output": 3,
    },
]


@pytest.mark.parametrize("test_input, expected_output", [(d["input"], d["output"]) for d in examples])
def test_two_sums_examples(test_input, expected_output):
    s = test_input["s"]

    assert length_of_longest_substring(s) == expected_output
