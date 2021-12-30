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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_nodes = 0
        node = head
        while node:
            node = node.next
            n_nodes += 1

        if n == n_nodes:
            return head.next

        node = head
        for i in range(n_nodes - n - 1):
            node = node.next
        node.next = node.next.next

        return head


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


if __name__ == "__main__":
    ll = list_to_ll([1, 2, 3, 4, 5])
    print(ll)
    print(ll_to_list(ll))
    res = Solution().removeNthFromEnd(ll, 2)
    assert ll_to_list(res) == [1,2,3,5]

    ll = list_to_ll([1, 2, 3, 4, 5])
    res = Solution().removeNthFromEnd(ll, 4)
    assert ll_to_list(res) == [1,3,4,5]

    ll = list_to_ll([1, 2, 3, 4, 5])
    res = Solution().removeNthFromEnd(ll, 1)
    assert ll_to_list(res) == [1,2,3,4]

    ll = list_to_ll([1, 2, 3, 4, 5])
    res = Solution().removeNthFromEnd(ll, 5)
    assert ll_to_list(res) == [2,3,4,5]

    ll = list_to_ll([1])
    res = Solution().removeNthFromEnd(ll, 1)
    assert ll_to_list(res) == []

    print(f"All done")