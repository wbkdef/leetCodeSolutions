"""
From: https://leetcode.com/problems/sort-list/
"""

from __future__ import annotations

import itertools as it
from typing import Optional
import functools
import textwrap
import dataclasses


# Definition for singly-linked list.
@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: ListNode = None
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(f" original list is [[{ll_to_list(head)}]]")

        n = head
        prev = ListNode(None, head)

        num_merges = 2
        segment_length = 1
        while num_merges > 1:
            tail = prev
            n = tail.next
            num_merges = 0
            while n is not None:
                num_merges += 1
                head_left_segment, n = self.split_segment_rest(n, segment_length)
                head_right_segment, n = self.split_segment_rest(n, segment_length)
                # print()
                # print(f" head_left_segment is [[{ll_to_list(head_left_segment)}]]")
                # print(f" head_right_segment is [[{ll_to_list(head_right_segment)}]]")
                start, end = \
                    self.merge_sorted_segments(head_left_segment, head_right_segment)
                assert end.next is None
                tail.next = start
                tail = end
            # print(f" list after segment_length {segment_length} merge is "
            #       f"[[{ll_to_list(prev.next)}]]")
            segment_length *= 2

        return prev.next

    def split_segment_rest(self, head, segment_length)  ->  tuple[ListNode, Optional[ListNode]]:
        n = head
        for i in range(segment_length-1):
            if n is None:
                return head, None
            n = n.next
        if n is None:
            return head, None
        nn = n.next
        n.next = None
        return head, nn

    def merge_sorted_segments(self, head_left_segment, head_right_segment):
        prev = ListNode(None, None)
        n = prev

        while head_left_segment is not None or head_right_segment is not None:
            if head_left_segment is None:
                add_from = "right"
            elif head_right_segment is None:
                add_from = "left"
            elif head_left_segment.val < head_right_segment.val:
                add_from = "left"
            else:
                add_from = "right"

            if add_from == "left":
                n.next = head_left_segment
                n = head_left_segment
                head_left_segment = head_left_segment.next
            else:
                assert add_from == "right"
                n.next = head_right_segment
                n = head_right_segment
                head_right_segment = head_right_segment.next

        assert n.next is None
        return prev.next, n


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
    print(f"\n res is [[\n{res}\n]]")
    assert res == [1, 2, 3, 4]

    res = ll_to_list(Solution().sortList(list_to_ll([-1,5,3,4,0])))
    print(f"\n res is [[\n{res}\n]]")
    assert res == [-1,0,3,4,5]

    res = ll_to_list(Solution().sortList(list_to_ll([])))
    print(f"\n res is [[\n{res}\n]]")
    assert res == []

    print(f"all done")
