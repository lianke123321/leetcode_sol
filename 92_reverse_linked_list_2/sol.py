# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(m - 1):
            slow = slow.next
        newHead = slow
        slow = slow.next
        for i in range(n):
            fast = fast.next
        newTail = fast.next
        if fast == slow:
            return head
        fast.next = None
        last = None
        cur = slow  # currentNode
        while cur:
            temp = cur.next  # nextNode
            cur.next = last
            last = cur
            cur = temp
        newHead.next = last
        slow.next = newTail
        return dummy.next

    def reverseBetween_self(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        i = 0
        curr = dummy
        last = None
        before_reverse = None
        first_reverse = None
        while curr:
            if i < m - 1:
                curr = curr.next
            elif i == m - 1:
                before_reverse = curr
                curr = curr.next
            elif i == m:
                first_reverse = curr
                last = curr
                curr = curr.next
            elif i == n:
                before_reverse.next = curr
                next = curr.next
                curr.next = last
                last = curr
                curr = next

                first_reverse.next = curr
                break
            else:
                next = curr.next
                curr.next = last
                last = curr
                curr = next

            i += 1

        return dummy.next
