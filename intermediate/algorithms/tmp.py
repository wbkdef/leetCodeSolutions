#https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum1 = 0
        sum2 = 0
        m1 = 1
        m2 = 1

        print(l1)

        while True:
            sum1 += m1 * l1.val

            if l1.next is None:
                break
            l1 = l1.next
            m1 = m1 * 0.1

        while True:
            sum2 += m2 * l2.val

            if l2.next is None:
                break
            l2 = l2.next
            m2 = m2 * 0.1

        mmax = min([m1, m2])

        val = int(round(sum1 / m1) + round(sum2 / m2))

        val = [int(x) for x in str(val)]

        out = ListNode(val=val[0], next=None)
        for v in val[1:]:
            out = ListNode(v, out)
        return out