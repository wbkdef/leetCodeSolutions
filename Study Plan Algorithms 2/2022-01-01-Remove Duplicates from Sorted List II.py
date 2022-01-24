"""
From: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
PC:KEYpjPb:
"""

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = current = ListNode("NA", head)
        to_delete = None

        while current:
            if current.next is None:
                break
            elif to_delete is not None and current.next.val == to_delete:
                current.next = current.next.next
                continue
            elif current.next.next is not None\
                    and current.next.val == current.next.next.val:
                to_delete = current.next.val
                continue
            else:
                current = current.next

        return sentinel.next



def list_to_ll(lst: list):
    if not lst:
        return None
    node = head = ListNode(lst[0])
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    return head

def ll_to_list(head: Optional[ListNode]) -> list:
    if not head:
        return []
    node = head
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


if __name__ == "__main__":
    res = Solution().deleteDuplicates(list_to_ll([1,2,3,3,4,4,5]))
    assert ll_to_list(res) == [1, 2, 5]

    res = Solution().deleteDuplicates(list_to_ll([1,1,1,2,3]))
    assert ll_to_list(res) == [2, 3]

    res = Solution().deleteDuplicates(list_to_ll([1,2,3]))
    assert ll_to_list(res) == [1, 2, 3]

    res = Solution().deleteDuplicates(list_to_ll([3]))
    assert ll_to_list(res) == [3]

    res = Solution().deleteDuplicates(list_to_ll([]))
    assert ll_to_list(res) == []

    print(f"all done")
