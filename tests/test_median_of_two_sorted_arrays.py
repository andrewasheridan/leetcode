import pytest

from leetcode.median_of_two_sorted_arrays.answer import median_of_two_sorted_arrays

examples = [
    {
        "input": {
            "nums1": [1, 3],
            "nums2": [2],
        },
        "output": 2.0,
    },
    {
        "input": {
            "nums1": [1, 2],
            "nums2": [3, 4],
        },
        "output": 2.5,
    },
    {
        "input": {
            "nums1": [1, 1, 2, 3, 4],
            "nums2": [3, 4, 5, 6, 7, 8, 9],
        },
        "output": 4.0,
    },
    {
        "input": {
            "nums1": [2],
            "nums2": [],
        },
        "output": 2,
    },
    {
        "input": {
            "nums1": [1, 1, 1, 2, 3, 4],
            "nums2": [2, 2, 3, 4, 5],
        },
        "output": 2,
    },
    {
        "input": {
            "nums1": [1, 2],
            "nums2": [3, 4, 5],
        },
        "output": 3,
    },
]


@pytest.mark.parametrize("test_input, expected_output", [(d["input"], d["output"]) for d in examples])
def test_median_of_two_sorted_arrays_examples(test_input, expected_output):
    nums1 = test_input["nums1"]
    nums2 = test_input["nums2"]

    assert median_of_two_sorted_arrays(nums1, nums2) == expected_output
