import pytest

from leetcode.two_sum.answer import two_sum

examples = [
    {
        "input": {
            "nums": [2, 7, 11, 15],
            "target": 9,
        },
        "output": [0, 1],
    },
    {
        "input": {
            "nums": [3, 2, 4],
            "target": 6,
        },
        "output": [1, 2],
    },
    {
        "input": {
            "nums": [3, 3],
            "target": 6,
        },
        "output": [0, 1],
    },
]


@pytest.mark.parametrize("test_input, expected_output", [(d["input"], d["output"]) for d in examples])
def test_two_sums_examples(test_input, expected_output):
    nums = test_input["nums"]
    target = test_input["target"]

    assert sorted(two_sum(nums, target)) == sorted(expected_output)
