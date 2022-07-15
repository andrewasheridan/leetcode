"""Median of two sorted arrays."""


def median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """Median of two sorted arrays.

    Runtime: 99 ms, faster than 91.13% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.1 MB, less than 96.62% of Python3 online submissions for Median of Two Sorted Arrays.

    """
    merged = sorted(nums1 + nums2)
    count = len(merged)
    midpoint = int(count // 2)
    if count % 2 != 0:
        return merged[midpoint]
    return 0.5 * (merged[midpoint] + merged[midpoint - 1])
