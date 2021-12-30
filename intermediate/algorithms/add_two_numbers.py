# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_digit_carry(self, *numbers):
        print(numbers)
        s = sum(numbers)
        carry = s // 10
        digit = s % 10
        return digit, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return None
        res_parent = ListNode(None)
        curr = res_parent
        carry = 0
        while l1 is not None or l2 is not None:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            carry, digit = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return res_parent.next


# if __name__ == '__main__':
#     l1 = [2, 4, 3]
#     l2 = [5, 6, 4]
#     res = Solution().addTwoNumbers(l1, l2)
#     assert res == [7, 0, 8]


# A nice solution from leetcode:
class Solution_ANS(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next