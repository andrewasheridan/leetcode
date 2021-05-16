"""Two Sum."""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Two sum.

    Runtime: 44 ms, faster than 81.95% of Python3 online submissions for Two Sum.
    Memory Usage: 14.3 MB, less than 71.33% of Python3 online submissions for Two Sum.
    """

    for i, num_a in enumerate(nums):
        offset = i + 1
        for j, num_b in enumerate(nums[offset:], start=offset):
            if num_a + num_b == target:
                return [i, j]
    raise ValueError("Unable to determine nums")
