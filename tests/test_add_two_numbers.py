import pytest

from leetcode.add_two_numbers.answer import add_two_numbers, ListNode

examples = [
    {
        "input": {
            "num_a": ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
            "num_b": ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4))),
        },
        "output": ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8))),
    },
    {
        "input": {
            "num_a": ListNode(val=0),
            "num_b": ListNode(val=0),
        },
        "output": ListNode(val=0),
    },
    {
        "input": {
            "num_a": ListNode(
                val=9,
                next=ListNode(
                    val=9,
                    next=ListNode(
                        val=9,
                        next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))),
                    ),
                ),
            ),
            "num_b": ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))),
        },
        "output": ListNode(
            val=8,
            next=ListNode(
                val=9,
                next=ListNode(
                    val=9,
                    next=ListNode(
                        val=9,
                        next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1)))),
                    ),
                ),
            ),
        ),
    },
]


@pytest.mark.parametrize("test_input, expected_output", [(d["input"], d["output"]) for d in examples])
def test_add_two_numbers_examples(test_input, expected_output):
    num_a = test_input["num_a"]
    num_b = test_input["num_b"]

    assert add_two_numbers(num_a, num_b) == expected_output
