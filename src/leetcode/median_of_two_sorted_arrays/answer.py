"""Median of two sorted arrays."""


def median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """Median of two sorted arrays.

    Runtime: 180 ms, faster than 22.89% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.2 MB, less than 68.31% of Python3 online submissions for Median of Two Sorted Arrays.

    """
    x, y = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    m, n = len(x), len(y)
    number_of_elements = m + n
    even_number_of_elements = number_of_elements % 2 == 0
    half_count = number_of_elements // 2

    lower = 0
    higher = m - 1

    while True:

        i_x = (lower + higher) // 2
        i_y = half_count - i_x - 2

        x_left = x[i_x] if i_x >= 0 else float("-infinity")
        y_left = y[i_y] if i_y >= 0 else float("-infinity")

        x_right = x[i_x + 1] if (i_x + 1) < m else float("infinity")
        y_right = y[i_y + 1] if (i_y + 1) < n else float("infinity")

        partitions_correct = x_left <= y_right and y_left <= x_right

        if not partitions_correct:
            if x_left > y_right:
                higher = i_x - 1
            else:
                lower = i_x + 1
            continue

        if even_number_of_elements:
            return 0.5 * (max(x_left, y_left) + min(x_right, y_right))
        return min(x_right, y_right)
