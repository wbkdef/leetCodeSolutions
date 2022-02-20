"""
From: https://leetcode.com/problems/sort-list/

"""

from __future__ import annotations

import itertools as it
from typing import Optional
import functools
import textwrap


# Definition for singly-linked list.
class ListNode:
    val: int = 0
    next: ListNode = None
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = head
        prev = ListNode(None, head)

        # length = 0
        # while n:
        #     length += 1
        #     n = n.next

        segment_len = 1
        n_start_next_segment = head

        # Identify the starts of the segments
        n = n_left = n_start_next_segment
        for i in range(segment_len):
            if n is None:
                break
            n = n.next
        n_right = n
        for i in range(segment_len):
            if n is None:
                break
            n = n.next
        n_start_next_segment = n

        # merge left and right
        delta_left = delta_right = 0
        while True:
            if delta_left < segment_len:
                if n_right is None \
                        or delta_right == segment_len \
                        or n_left.val <= n_right.val:
                    prev.next = n_left
                    n_left = n_left.next
                    delta_left += 1
                    continue

            if delta_right < segment_len and n_right is not None:
                if delta_left == segment_len or n_left.val > n_right.val:
                    prev.next = n_right
                    n_right = n_right.next
                    delta_right += 1
                    continue

            break





    # def sortList_(self, head: Optional[ListNode], length: int) -> Optional[ListNode]:
    #     assert length >= 0
    #     if length == 0:
    #         assert head is None
    #         return head
    #     if length == 1:
    #         assert head.next == None
    #         return head
    #     assert length > 1





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
    res = ll_to_list(Solution().sortList(list_to_ll([4,2,1,3])))
    assert len(res) == [1, 2, 3, 4]
    print(f"\n res is [[\n{res}\n]]")

    res = ll_to_list(Solution().sortList(list_to_ll([-1,5,3,4,0])))
    assert len(res) == [-1,0,3,4,5]
    print(f"\n res is [[\n{res}\n]]")

    res = ll_to_list(Solution().sortList(list_to_ll([])))
    assert len(res) == []
    print(f"\n res is [[\n{res}\n]]")

    print(f"all done")
