"""
From: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
PC:KEYsg9c:
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"({self.val})->{self.next}"


def list_to_ll(lst: list):
    if not lst:
        return None
    node = head = ListNode(lst[0])
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    return head


def ll_to_list(head: Optional[ListNode])  ->  list:
    if not head:
        return []
    node = head
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        remainder = new_head.next
        new_head.next = head
        head.next = self.swapPairs(remainder)

        return new_head


if __name__ == "__main__":
    ll = list_to_ll([1, 2, 3, 4])
    print(ll)
    print(ll_to_list(ll))
    res = Solution().swapPairs(ll)
    assert ll_to_list(res) == [2, 1, 4, 3]

    res = Solution().swapPairs(list_to_ll([1, 2, 3]))
    assert ll_to_list(res) == [2, 1, 3]

    res = Solution().swapPairs(list_to_ll([1]))
    assert ll_to_list(res) == [1]

    res = Solution().swapPairs(list_to_ll([]))
    assert ll_to_list(res) == []

    print(f"All done")