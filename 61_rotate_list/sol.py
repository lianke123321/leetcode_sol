# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        newHead = head
        tail = head
        length = 1  # number of nodes
        while tail.next:  # get the number of nodes in the list
            tail = tail.next
            length += 1
        tail.next = head
        k = k % length
        if k:
            for i in range(length - k):
                tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead

    def rotateRight_self(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # first round: get the number of nodes
        # and the last node
        if not head or k == 0:
            return head

        num = 0
        curr = head
        last = None
        while curr:
            num += 1
            if not curr.next:
                last = curr
            curr = curr.next

        # then get the true k
        k = k % num

        if k == 0:
            return head

        # do the rotation
        curr = head
        for i in range(num - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        last.next = head
        return new_head
