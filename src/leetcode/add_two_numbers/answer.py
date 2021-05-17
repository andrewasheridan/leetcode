"""Add two numbers."""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @property
    def vals(self) -> list[int]:
        vals = [self.val]
        node = self
        while node.next is not None:
            node = node.next
            vals.append(node.val)
        return vals

    def __repr__(self):
        return f"ListNode(vals={self.vals})"

    def __eq__(self, other):
        return self.vals == other.vals


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Add two numbers.

    Runtime: 68 ms, faster than 72.40% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 14.5 MB, less than 11.63% of Python3 online submissions for Add Two Numbers.
    """

    def decompose_listnode(list_node: ListNode) -> int:
        vals: list[str] = [str(list_node.val)]
        while list_node.next is not None:
            list_node = list_node.next
            vals.append(str(list_node.val))
        return int(f"".join(reversed(vals)))

    val_a = decompose_listnode(l1)
    val_b = decompose_listnode(l2)

    vals: list[int] = [int(val) for val in str(val_a + val_b)]
    vals.reverse()

    list_node = output = ListNode(vals[0])
    for val in vals[1:]:
        list_node.next = ListNode(val=val)
        list_node = list_node.next

    return output
