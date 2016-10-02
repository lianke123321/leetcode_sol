# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = 0
        result = ListNode(0)
        s = result
        while l1 or l2 or temp:
            s.val = temp
            if l1:
                s.val += l1.val
                l1 = l1.next
            if l2:
                s.val += l2.val
                l2 = l2.next
            temp, s.val = divmod(s.val, 10)
            if l1 or l2 or temp:
                s.next = ListNode(0)
                s = s.next
        return result

    def addTwoNumbers_self(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr, carry = head, 0
        while l1 or l2 or carry > 0:
            if l1 and l2:
                total = l1.val + l2.val + carry
                curr.val = total % 10
                carry = total / 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val + carry
                curr.val = total % 10
                carry = total / 10
                l1 = l1.next
            elif l2:
                total = l2.val + carry
                curr.val = total % 10
                carry = total / 10
                l2 = l2.next
            else:
                curr.val = carry
                carry = 0

            # check if there are more nodes in l1 and l2
            if l1 or l2 or carry > 0:
                curr.next = ListNode(0)
                curr = curr.next
        return head
